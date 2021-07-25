from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .userprofile.user_info import user_info_router
from .userprofile.language_operations import language_operations_router

tags_metadata = [
    {
        "name": "Fast API demo",
        "description": "These are Fast API demo endpoints."
    },
    {
        "name": "Github User Operations",
        "description": "These operations fetches various information of the user's github profile."
    },
    {
        "name": "Languages used operations",
        "description": "These are responsible for computing language statistics based on users github profile."
    }
]

app = FastAPI(
    title="Github Stats",
    version="1.0.0",
    description="This API is integrated with github rest api to fetch user info and generate statistics",
    openapi_tags=tags_metadata,
    docs_url="/swagger",
    redoc_url="/"
)

app.include_router(user_info_router)
app.include_router(language_operations_router)

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


@app.get("/", tags=["Fast API demo"])
def read_root():
    return "This API is built using FAST API , which performs some operations using Github API"
