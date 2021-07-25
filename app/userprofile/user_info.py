from fastapi import APIRouter, HTTPException
from fastapi.openapi.models import Response
from ..userprofile.user_service import UserService

user_info_router = APIRouter(
    tags=["Github User Operations"],
    responses={404: {"description": "Not found"}},
)


@user_info_router.get("/getUserDetails/{username}")
def getUserDetails(username: str):
    try:
        userService = UserService(username)
        userDetails = userService.getUserDetails()
        print(userDetails)
        return userDetails
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=e,
        )


@user_info_router.get("/getUserFollowers/{username}")
def getUserFollowers(username: str):
    try:
        userService = UserService(username)
        followers = userService.getUserFollowers()
        return followers
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=e
        )


@user_info_router.get("/getUserGists/{username}")
def getUserGists(username: str):
    try:
        userService = UserService(username)
        if userService.isValidGithubUser():
            gists = userService.getUserGists()
            return gists
        else:
            print("user not found")
            return Response(status_code=404, content="Github user not found")

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=e
        )


@user_info_router.get("/getUserGist/{username}/{gist_id}")
def getUserGist(username: str, gist_id: str):
    try:
        userService = UserService(username)

        if userService.isValidGithubUser():
            gist = userService.getUserGist(gist_id)
            return gist
        else:
            return Response(status_code=404, content="Github user not found")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=e
        )


@user_info_router.get("/getUserRepos/{username}")
def getUserRepos(username: str):
    try:
        userService = UserService(username)

        if userService.isValidGithubUser():
            repos = userService.getUserRepos()
            return repos
        else:
            return Response(status_code=404, content="Github user not found")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=e
        )


@user_info_router.get("getUserRepoLanguages/{username}/{repo_name}")
def getUserRepoLanguages(username: str, repo_name: str):
    try:
        userService = UserService(username)

        if userService.isValidGithubUser():
            languages = userService.getUserRepoLanguages(repo_name)
            return languages
        else:
            return Response(status_code=404, content="Github user not found")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=e
        )
