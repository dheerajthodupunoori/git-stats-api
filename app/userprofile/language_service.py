from typing import Dict


class Language:

    def __init__(self, username):
        self.username = username
        self.languages = Dict[str, float]

    def computeLanguagesUsedInPercentages(self):
        pass
