from project.helper.helper import Helper
from project.present.present import Present


class ShopImpl:

    def craft(self, present: Present, helper: Helper):
        helper_instruments = [inst for inst in helper.instruments()]

        # if the helper has energy and an instrument that isn't broken
        with helper.can_work() and helper_instruments:
            for inst in helper_instruments:
                if inst.is_broken():
                    continue

                inst.use()
                helper.work()





