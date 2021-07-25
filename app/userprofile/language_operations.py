from fastapi import APIRouter

language_operations_router = APIRouter(
    tags=["Languages used operations"],
    responses={404: {"description": "Username or Repository not found."}},
)


@language_operations_router.get("/generateLanguagesUsageByPercentage/{username}/{repo_name}")
def generateLanguagesUsageByPercentage(username: str, repo_name: str):
    return {"username": username, "repo_name": repo_name}
