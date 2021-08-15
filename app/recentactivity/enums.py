import enum


class GithubEventTypes(enum.Enum):
    CommitCommentEvent = "CommitCommentEvent"
    CreateEvent = "CreateEvent"
    DeleteEvent = "DeleteEvent"
    ForkEvent = "ForkEvent"
    GollumnEvent = "GollumEvent"
    IssueCommentEvent = "IssueCommentEvent"
    IssuesEvent = "IssuesEvent"
    MemberEvent = "MemberEvent"
    PublicEvent = "PublicEvent"
    PullRequestEvent = "PullRequestEvent"
    PullRequestReviewEvent = "PullRequestReviewEvent"
    PullRequestReviewCommentEvent = "PullRequestReviewCommentEvent"
    PushEvent = "PushEvent"
    ReleaseEvent = "ReleaseEvent"
    SponsorshipEvent = "SponsorshipEvent"
    WatchEvent = "WatchEvent"
