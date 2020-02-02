from github import Github


class GithubApi:
    """
    class for interacting with the github api

    """
    base_url = "https://api.github.com"
    version = "1.0.3"

    def __init__(self):
        """
        init function

        """
        self.github = Github(base_url=self.base_url)
        self.last_release = None
        self.release_url = None
        self.repo = None

    def update_available(self):
        """
        checks if there is a new release in the repository

        :return: True if there is a update otherwise False
        :rtype: bool
        """
        try:
            self.repo = self.github.get_repo("LXkennstenich/PyQt_YTDownloader")
            paginated_list = self.repo.get_releases()
            if paginated_list.totalCount > 0:
                for release in paginated_list:
                    if self.version != release.tag_name:
                        release_as_number = str(release.tag_name).strip('v')
                        release_as_number = int(release_as_number.replace('.', ''))
                        current_version_as_number = str(self.version).strip('v')
                        current_version_as_number = int(current_version_as_number.replace('.', ''))
                        if current_version_as_number < release_as_number:
                            self.last_release = str(release.tag_name)
                            self.release_url = str(release.html_url)
                            return True
        except Exception:
            return False
