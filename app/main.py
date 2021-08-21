from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .userprofile.user_info import user_info_router
from .userprofile.language_operations import language_operations_router
from app.emailoperations.email_routes import email_operations_router
from fastapi.staticfiles import StaticFiles
from app.recentactivity.recent_activiy_routes import recent_activity_router


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
    },
    {
        "name": "Recent Activity",
        "description": "These path operations are responsible for generating the recent activity of the users github "
                       "account. "
    }
]

app = FastAPI(
    title="Github Stats",
    version="1.0.0",
    description="This API is integrated with github rest api to fetch user info and generate statistics.",
    openapi_tags=tags_metadata,
    docs_url="/swagger",
    redoc_url="/"
)

app.include_router(user_info_router)
app.include_router(language_operations_router)
app.include_router(recent_activity_router)

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

app.mount("/about", StaticFiles(directory="app/static", html=True), name="info")

tags_metadata_for_email_api = [
    {
        "name": "Email Operations",
        "description": "These routes are responsible for sending emails from the user to the admin of this API."
    }
]

email_api = FastAPI(
    title="Github Stats email operations",
    openapi_tags=tags_metadata_for_email_api,
    description="This API is responsible for handling email operations for Git Stats API.",
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc"
)
email_api.include_router(email_operations_router)

app.mount("/email", email_api)


@app.get("/", tags=["Fast API demo"])
def read_root():
    return "This API is built using Python FAST API , which performs some operations using Github API."
