from .enums import GithubEventTypes
from abc import ABC, abstractmethod


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
        return {}


class CreateEvent(EventType):

    def __init__(self, event: dict):
        self.create_event_payload = event

    def getEventPayload(self):
        return {}


class PullRequestEvent(EventType):

    def __init__(self, event: dict):
        self.pull_request_event_payload = event

    def getEventPayload(self):
        return {}

class WatchEvent(EventType):

    def __init__(self, event: dict):
        self.watch_event_payload = event

    def getEventPayload(self):
        return {}


class EventTypeFactory:

    def __init__(self, event_type: str, event: dict):
        self.event_type = event_type
        self.event_payload = event

    def createEventInstance(self):

        print("creating event instance for {event_type}".format(event_type=self.event_type))

        if self.event_type == GithubEventTypes.PushEvent.value:
            return PushEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.CreateEvent.value:
            return CreateEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.PullRequestEvent.value:
            return PullRequestEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.WatchEvent.value:
            return WatchEvent(self.event_payload)

        print("created event instance")

