from abc import ABC, abstractmethod
from .enums import GithubEventDescription


class EventType(ABC):

    # def __init__(self, event_type: str, event: dict):
    #     self.event_type = event_type
    #     self.event = event

    @abstractmethod
    def getEventPayload(self):
        pass


class PushEvent(EventType):

    def __init__(self, event: dict):
        self.push_event_payload = event

    def getEventPayload(self):
        try:
            payload = dict()
            payload["event_description"] = GithubEventDescription.PushEvent.value
            payload["number_of_commits"] = self.push_event_payload.get("size")
            return payload

        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class CreateEvent(EventType):

    def __init__(self, event: dict):
        self.create_event_payload = event

    def getEventPayload(self):
        try:

            payload = dict(
                event_description=GithubEventDescription.CreateEvent.value,
                ref=self.create_event_payload.get("ref"),
                ref_type=self.create_event_payload.get("ref_type")
            )

            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class PullRequestEvent(EventType):

    def __init__(self, event: dict):
        self.pull_request_event_payload = event

    def getEventPayload(self):
        try:

            pull_request = self.pull_request_event_payload.get("pull_request")

            payload = dict(
                event_description=GithubEventDescription.PullRequestEvent.value,
                action=self.pull_request_event_payload.get("action"),
                pull_request_number=self.pull_request_event_payload.get("number"),
                pull_request_state=pull_request.get("state"),
                pull_request_title=pull_request.get("title")
            )

            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class WatchEvent(EventType):

    def __init__(self, event: dict):
        self.watch_event_payload = event

    def getEventPayload(self):
        try:
            payload = dict(
                event_description=GithubEventDescription.WatchEvent.value,
                action=self.watch_event_payload.get("action")
            )
            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class CommitCommentEvent(EventType):

    def __int__(self, event: dict):
        self.commit_comment_payload = event

    def getEventPayload(self):
        try:
            payload = dict(
                event_description=GithubEventDescription.WatchEvent.value,
                action=self.watch_event_payload.get("action")
            )
            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class DeleteEvent(EventType):

    def __init__(self, event: dict):
        self.delete_event_payload = event

    def getEventPayload(self):
        try:
            payload = dict(
                event_description=GithubEventDescription.DeleteEvent.value,
                ref=self.delete_event_payload.get("ref"),
                ref_type=self.delete_event_payload.get("ref_type")
            )
            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class ForkEvent(EventType):

    def __init__(self, event: dict):
        self.fork_event_payload = event

    def getEventPayload(self):
        try:

            forked_repository = self.fork_event_payload.get("forkee")

            payload = dict(
                event_description=GithubEventDescription.ForkEvent.value,
                forked_repository_name=forked_repository.get("name"),
                forked_repository_full_name=forked_repository.get("full_name")
            )
            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class GollumEvent(EventType):

    def __init__(self, event: dict):
        self.gollum_event_payload = event

    def getEventPayload(self):
        try:
            payload = dict(
                event_description=GithubEventDescription.GollumEvent.value,
                ref=self.gollum_event_payload.get("ref"),
                ref_type=self.gollum_event_payload.get("ref_type")
            )
            return payload
        except KeyError as key_error:
            raise key_error
        except Exception as error:
            raise error


class IssueCommentEvent(EventType):

    def __init__(self, event: dict):
        self.issue_comment_event_payload = event

    def getEventPayload(self):
        return {}


class IssuesEvent(EventType):

    def __init__(self, event: dict):
        self.issues_event_payload = event

    def getEventPayload(self):
        return {}


class MemberEvent(EventType):

    def __init__(self, event: dict):
        self.member_event_payload = event

    def getEventPayload(self):
        return {}


class PublicEvent(EventType):

    def __init__(self, event: dict):
        self.public_event_payload = event

    def getEventPayload(self):
        return {}


class PullRequestReviewEvent(EventType):

    def __init__(self, event: dict):
        self.pull_request_event_payload = event

    def getEventPayload(self):
        return {}


class PullRequestReviewCommentEvent(EventType):

    def __init__(self, event: dict):
        self.pull_request_review_comment_event_payload = event

    def getEventPayload(self):
        return {}


class ReleaseEvent(EventType):

    def __init__(self, event: dict):
        self.release_event_payload = event

    def getEventPayload(self):
        return {}


class SponsorshipEvent(EventType):

    def __init__(self, event: dict):
        self.sponsorship_event_payload = event

    def getEventPayload(self):
        return {}
