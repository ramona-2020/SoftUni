from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> True or False:
        for i in range(len(self.decorations)):
            decoration = self.decorations[i]
            self.decorations.pop(i)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        # Returns the first decoration of the given type if there is. Otherwise, returns a message "None".
        for decoration in self.decorations:
            if decoration.decoration_type == decoration_type:
                return decoration

        return "None"
