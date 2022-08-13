from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def remove_room(self, room: Room):
        self.rooms.remove(room)

    @property
    def all_people_in_the_hotel(self):
        all_people_in_the_hotel = 0
        for room in self.rooms:
            all_people_in_the_hotel += room.members_count
        return all_people_in_the_hotel

    @staticmethod
    def monthly_expenses_with_room_cost(room: Room):
        total_consumption = 0
        total_consumption += room.expenses + room.ROOM_COST
        return total_consumption

    def monthly_expenses_for_appliances(*args):
        # args are Appliances list
        total_expense = 0
        for arg in args[1]:
            total_expense += arg.get_monthly_expense()

        return total_expense

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.ROOM_COST

        return f"Monthly consumtions: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            family_budget = room.budget
            room_monthly_cost = Everland.monthly_expenses_with_room_cost(room)
            if family_budget >= room_monthly_cost:
                budget_left = family_budget - room_monthly_cost
                result += f"{room.family_name} paid {room_monthly_cost:.2f}$ and have {budget_left:.2f}$ left.\n"
                family_budget -= room_monthly_cost
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.remove_room(room)

        return result.strip()

    def status(self):
        # Return information about the hotel
        result = f"Total population: {self.all_people_in_the_hotel}\n"
        for room in self.rooms:
            result += f"{str(room)}\n"
            appliances_monthly_cost = self.monthly_expenses_for_appliances(room.appliances)
            if room.children:
                for i in range(len(room.children)):
                    child = room.children[i]
                    child_monthly_cost = child.get_monthly_expense()
                    result += f"--- Child {i+1} monthly cost: {child_monthly_cost:.2f}$\n"

            result += f"--- Appliances monthly cost: {appliances_monthly_cost:.2f}$\n"

        return result.strip()

