from project.present.present import Present


class PresentRepository:

    def __init__(self):
        self.presents = []

    def add(self, present: Present):
        self.presents.append(present)

    def remove(self, present: Present):
        if present in self.presents:
            self.presents.remove(present)
            return True

    def find_by_name(self, searched_name: str):
        for present in self.presents:
            if present.name == searched_name:
                return present
        return None

    def get_models(self):
        pass