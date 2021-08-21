from ..userprofile.config import recent_activity_url
import requests
from os import getenv
from .event_factory import EventTypeFactory
from typing import Optional
import traceback
from .recent_activity_custom_exceptions import InvalidGithubEventType


class RecentActivityService:

    def __init__(self, username: str, limit: Optional[int] = 20):
        self.limit = limit
        self.username = username
        print("created recent activity service.")

    def getRecentActivity(self):
        result = dict()

        try:
            access_token = getenv("GITHUB_ACCESS_TOKEN")
            params = {
                "access_token": access_token
            }
            request_url = recent_activity_url.format(
                username=self.username
            )

            print("Fetching recent activity from github.")

            response = requests.get(request_url, params=params).json()

            print("completed fetching recent activity.")

            for event in response:

                if event.get("type") not in result:
                    result[event.get("type")] = []

                new_event = dict()

                new_event["id"] = event.get("id")
                new_event["type"] = event.get("type")
                new_event["created_at"] = event.get("created_at")
                new_event["avatar_url"] = event.get("avatar_url")

                repo = event.get("repo")

                if repo is not None:
                    new_event["repo_id"] = repo.get("id")
                    new_event["repo_name"] = repo.get("name").split("/")[1]
                    new_event["repo_url"] = repo.get("url")

                event_type_factory = EventTypeFactory(event.get("type"), event.get("payload"))

                payload = event_type_factory.createEventInstance()

                print("got the event object.")

                event_payload = payload.getEventPayload()

                new_event["payload"] = event_payload

                result[event.get("type")].append(new_event)

            return result
        except InvalidGithubEventType as invalid_github_event:
            raise invalid_github_event
        except Exception as error:
            traceback.print_exc()
            raise error
