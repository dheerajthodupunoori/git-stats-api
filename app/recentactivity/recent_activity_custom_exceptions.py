class InvalidGithubEventType(Exception):

    def __init__(self, event_type, message="Invalid event type"):
        self.event_type = event_type
        self.error_message = message
        super().__init__(self.error_message)

    def __str__(self):
        return f'{self.event_type} is invalid Github event type'
