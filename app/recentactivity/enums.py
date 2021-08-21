import enum


class GithubEventTypes(enum.Enum):
    CommitCommentEvent = "CommitCommentEvent"
    CreateEvent = "CreateEvent"
    DeleteEvent = "DeleteEvent"
    ForkEvent = "ForkEvent"
    GollumEvent = "GollumEvent"
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


class GithubEventDescription(enum.Enum):

    CommitCommentEvent = "A commit comment is created."
    CreateEvent = "A Git branch or tag is created."
    DeleteEvent = "A Git branch or tag is deleted."
    ForkEvent = "A user forks a repository."
    GollumEvent = "GollumEvent"
    IssueCommentEvent = "IssueCommentEvent"
    IssuesEvent = "IssuesEvent"
    MemberEvent = "MemberEvent"
    PublicEvent = "PublicEvent"
    PullRequestEvent = "Activity related to pull requests."
    PullRequestReviewEvent = "PullRequestReviewEvent"
    PullRequestReviewCommentEvent = "PullRequestReviewCommentEvent"
    PushEvent = "One or more commits are pushed to a repository branch or tag."
    ReleaseEvent = "ReleaseEvent"
    SponsorshipEvent = "SponsorshipEvent"
    WatchEvent = "When someone stars a repository."
