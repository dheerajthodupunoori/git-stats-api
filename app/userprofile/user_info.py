from fastapi import APIRouter, HTTPException, Path
from fastapi.openapi.models import Response
from ..userprofile.user_service import UserService

user_info_router = APIRouter(
    tags=["Github User Operations"],
)


@user_info_router.get("/getUserDetails/{username}",
                      description="This API route will fetch the user details.",
                      status_code=200)
def getUserDetails(username: str = Path(..., min_length=2,
                                        title="Github username",
                                        description="This is the github username")):
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


@user_info_router.get("/getUserFollowers/{username}",
                      description="This API route will fetch all the user followers.",
                      status_code=200)
def getUserFollowers(username: str = Path(..., min_length=2,
                                          title="Github username",
                                          description="This is the github username")):
    try:
        userService = UserService(username)
        followers = userService.getUserFollowers()
        return followers
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=e
        )


@user_info_router.get("/getUserGists/{username}",
                      description="This API route will fetch all the user gists.")
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


@user_info_router.get("/getUserGist/{username}/{gist_id}",
                      description="This API route will fetch a specific gist , given the gist id")
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


@user_info_router.get("/getUserRepos/{username}",
                      description="This API route will fetch the user repositories")
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


@user_info_router.get("/getUserRepoLanguages/{username}/{repo_name}",
                      description="This API route will fetch the languages used in a specific repository.")
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
