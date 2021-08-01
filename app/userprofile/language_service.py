from typing import Dict, Optional
from .config import user_repo_languages_used_url
import requests


class Language:

    def __init__(self, username: str, repo_name: Optional[str] = None):
        self.username = username
        self.repo_name = repo_name

    def computeLanguagesUsedInPercentages(self):
        try:
            languages_by_percentage = []
            request_url = user_repo_languages_used_url.format(username=self.username, repo_name=self.repo_name)
            print(request_url)
            response = requests.get(request_url).json()
            total_lines = sum(response.values())
            print("Total lines of code in repo {repo_name} are {lines}".
                  format(repo_name=self.repo_name,lines=total_lines))

            for language in response:
                language_name = language
                language_lines = response[language]
                language_percentage = (language_lines*100)/total_lines
                languages_by_percentage.append({
                    "name": language_name,
                    "lines": language_lines,
                    "percentage": language_percentage
                })

            return languages_by_percentage
        except Exception as error:
            raise error
