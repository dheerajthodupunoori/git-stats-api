from fastapi import APIRouter, HTTPException
from ..userprofile.user_service import UserService
from typing import Optional
from .recent_activity_service import RecentActivityService

recent_activity_router = APIRouter(
    tags=["Recent Activity"]
)


@recent_activity_router.get("/getRecentActivity",
                            description="This path operation will retrieve the top n recent activity of the user in "
                                        "his/her github account",
                            )
def getRecentActivity(username: str, limit: Optional[int] = 20):

    try:
        recent_activity = dict()
        user_service = UserService(username)

        if user_service.isValidGithubUser():
            print("getting recent activity service instance")
            recent_activity_service = RecentActivityService(username)
            recent_activity = recent_activity_service.getRecentActivity()

        return recent_activity
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=error
        )
