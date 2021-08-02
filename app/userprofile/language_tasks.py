from .config import user_repo_languages_used_url
from typing import List
import requests
from os import getenv


def generateAllLanguagesUsage(username: str, repo_names: List[str]):
    result = dict()
    total_lines = 0
    access_token = getenv("GITHUB_ACCESS_TOKEN")
    for repo_name in repo_names:
        params = {
            "access_token": access_token
        }
        request_url = user_repo_languages_used_url.format(username=username, repo_name=repo_name)
        response = requests.get(request_url,
                                params=params).json()

        print("***************")
        print(repo_name)

        for language in response:

            print("     ", language)

            language_name: str = language
            language_lines = response[language]
            total_lines += int(language_lines)

            if language_name.strip() not in result:
                result[language_name] = language_lines
            else:
                result[language_name] += int(language_lines)

        print("******************")

    print("Total lines of code in the repo -", total_lines)

    language_with_percentages = []
    for language in result:
        name = language
        lines = result[language]
        percentage = (lines * 100) / total_lines
        language_with_percentages.append(
            {
                "name": name,
                "total_lines": lines,
                "percentage": percentage
            }
        )

    return language_with_percentages
