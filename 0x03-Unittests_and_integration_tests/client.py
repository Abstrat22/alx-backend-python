#!/usr/bin/env python3

"""
A GitHub organization client that interacts with the GitHub API to retrieve organization data.
"""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """
    A GitHub organization client.
    """

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """
        Initialize the GithubOrgClient.

        Args:
            org_name (str): The name of the GitHub organization.
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Retrieve organization data from the GitHub API.

        Returns:
            Dict: The organization data.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the organization's public repositories.

        Returns:
            str: The URL for public repositories.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """
        Retrieve the payload of the organization's repositories.

        Returns:
            Dict: The payload containing the organization's repositories data.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """
        Retrieve a list of public repositories for the organization.

        Args:
            license (str): Optional. The license type of the repositories.

        Returns:
            List[str]: The list of public repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """
        Check if the repository has a specific license.

        Args:
            repo (Dict[str, Dict]): The repository data.
            license_key (str): The license type to check for.

        Returns:
            bool: True if the repository has the specified license, False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(
                repo,
                ("license", "key"),
            ) == license_key
        except KeyError:
            return False
        return has_license
