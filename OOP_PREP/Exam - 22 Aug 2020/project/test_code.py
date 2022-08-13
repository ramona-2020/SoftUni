from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()


def test_one():

    child1 = Child(5)
    child2 = Child(3, 2)

    #hlone_old = AloneOld("Philipp", 150) # ok
    #alone_young = AloneYoung("Philipp", 150) # ok
    #old_couple = OldCouple("Philipp", 150, 40) # ok
    young_couple_with_children = YoungCoupleWithChildren("Philipp", 150, 40, child1)

    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()