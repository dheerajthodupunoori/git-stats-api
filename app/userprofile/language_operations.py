from fastapi import APIRouter
from .language_service import Language
from .user_service import UserService
from .language_tasks import generateAllLanguagesUsage

language_operations_router = APIRouter(
    tags=["Languages used operations"],
    responses={404: {"description": "Username or Repository not found."}},
)


@language_operations_router.get("/generateLanguagesUsageByPercentage/{username}/{repo_name}",
                                description="This API route will generate the languages used in "
                                            "a specific repository in percentages.")
def generateLanguagesUsageByPercentage(username: str, repo_name: str):
    user_service = UserService(username)
    if user_service.isValidGithubUser():
        user_repos = user_service.getUserRepos()
        repo_names = {repo["name"] for repo in user_repos}
        if repo_name.strip() in repo_names:
            language_service = Language(username, repo_name)
            response = language_service.computeLanguagesUsedInPercentages()
        else:
            return {"message":"Invalid repo name provided"}
    else:
        return {"message": "Invalid github username"}
    return response


@language_operations_router.get("/generateOverallLanguagePercentage/{username}",
                                description="This API route will generate the languages"
                                            " used in percentage based on all the repositories"
                                            " in the users github profile.")
def generateOverallLanguagePercentage(username: str):

    user_service = UserService(username)
    if user_service.isValidGithubUser():
        user_repos = user_service.getUserRepos()
        repo_names = {repo["name"] for repo in user_repos}
        response = generateAllLanguagesUsage(username, repo_names)
    else:
        return {"message": "Invalid Github username"}
    return response
