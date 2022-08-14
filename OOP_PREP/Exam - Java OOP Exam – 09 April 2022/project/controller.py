from project.helper.happy import Happy
from project.helper.sleepy import Sleepy
from project.hotel_repository import HelperRepository
from project.instrument.instrument import Instrument
from project.present.present import Present
from project.present_repository import PresentRepository


class ControllerImpl:

    def __init__(self):
        self.helper_repository = HelperRepository()
        self.present_repository = PresentRepository()

    def add_helper(self, helper_type: str, helper_name: str):
        if helper_type not in ["Happy", "Sleepy"]:
            return "Helper type doesn't exist!"

        if helper_type == "Happy":
            helper = Happy(helper_name)
            self.helper_repository.add(helper)
        else:
            helper = Sleepy(helper_name)
            self.helper_repository.add(helper)

        return f"Successfully added {helper_type} named {helper_name}!"

    def add_instrument_to_helper(self, helper_name, power: int):
        helper = self.helper_repository.find_by_name(helper_name)
        if not helper:
            raise Exception("The helper you want to add an instrument to doesn't exist!")

        instrument = Instrument(power)
        helper.add_instrument(instrument)
        return f"Successfully added instrument with power {instrument.power} to helper {helper.name}!"

    def add_present(self, present_name: str, energy_required: int):
        present = Present(present_name, energy_required)

        # adds it to the corresponding repository.
        self.present_repository.add(present)
        return f"Successfully added Present: {present.name}!"

    def craft_presents(self, present_name: str):
        result = ""
        presents_done = 0

        # The helpers that you should select are the ones with energy above 50 units
        possible_helpers = self.helper_repository.get_possible_helpers()
        if not possible_helpers:
            raise Exception("There is no helper ready to start crafting!")

        # whether the present is done and how many instruments have been broken in the process
        for helper in possible_helpers:
            helper_energy = helper.energy

            present = Present(present_name, helper_energy)
            presents_done += 1

            helper.work()

            #return f"Present {presentName} is {done/not done}. {countBrokenInstruments} instrument/s have been broken while working on it!"

    def report(self):
        pass
        # result = f"{countCraftedPresents} presents are done!"
        # result = "Helpers info:"
        # result = f"Name: {helperName1}"
        # result = f"Energy: {helperEnergy1}"
        # result = f"Instruments: {countInstruments} not broken left"
        #
        # return result


