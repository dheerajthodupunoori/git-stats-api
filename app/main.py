from fastapi import FastAPI, HTTPException, Response
from .userprofile.user_service import UserService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "This API is built using FAST API , which performs some operations using Github API"


@app.get("/getUserDetails/{username}")
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


@app.get("/getUserFollowers/{username}")
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


@app.get("/getUserGists/{username}")
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


@app.get("/getUserGist/{username}/{gist_id}")
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


@app.get("/getUserRepos/{username}")
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


@app.get("getUserRepoLanguages/{username}/{repo_name}")
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
