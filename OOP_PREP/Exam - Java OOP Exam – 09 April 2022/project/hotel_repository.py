from project.helper.helper import Helper


class HelperRepository:

    def __init__(self):
        self.helpers = []

    def add(self, helper: Helper):
        self.helpers.append(helper)

    def remove(self, helper: Helper):
        if helper in self.helpers:
            self.helpers.remove(helper)
            return True

    def find_by_name(self, searched_name: str):
        for helper in self.helpers:
            if helper.name == searched_name:
                return helper
        return None

    def get_models(self):
        # Returns a collection of helpers(unmodifiable).
        return self.helpers

    # The helpers that you should select are the ones with energy above 50 units
    def get_possible_helpers(self):
        return [helper for helper in self.helpers if helper.energy > 50]

