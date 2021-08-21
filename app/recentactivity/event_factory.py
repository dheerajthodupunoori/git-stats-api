from .enums import GithubEventTypes
from .event_payload import PushEvent, CreateEvent, PullRequestEvent, WatchEvent, CommitCommentEvent , DeleteEvent,\
    ForkEvent, GollumEvent, IssueCommentEvent, IssuesEvent, MemberEvent, PublicEvent, PullRequestReviewEvent, \
    PullRequestReviewCommentEvent, ReleaseEvent, SponsorshipEvent
from .recent_activity_custom_exceptions import InvalidGithubEventType


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
        elif self.event_type == GithubEventTypes.CommitCommentEvent.value:
            return CommitCommentEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.DeleteEvent.value:
            return DeleteEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.ForkEvent.value:
            return ForkEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.GollumEvent.value:
            return GollumEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.IssueCommentEvent.value:
            return IssueCommentEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.IssuesEvent.value:
            return IssuesEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.MemberEvent.value:
            return MemberEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.PublicEvent.value:
            return PublicEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.PullRequestReviewEvent.value:
            return PullRequestReviewEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.PullRequestReviewCommentEvent.value:
            return PullRequestReviewCommentEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.ReleaseEvent.value:
            return ReleaseEvent(self.event_payload)
        elif self.event_type == GithubEventTypes.SponsorshipEvent.value:
            return SponsorshipEvent(self.event_payload)
        else:
            raise InvalidGithubEventType(self.event_type)

        print("created event instance")
