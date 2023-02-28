import random
from zone_1st import pick_1st
from zone_2nd import pick_2nd, pick28_2nd
from show import show_number
from prize import winner_number
from num28 import pick_28


if __name__ == '__main__':
    choice = input(
        "please enter (1)picker_8 (2)picker_28 (3)picker_56 (4)picker_104: ")

    if choice == "1":
        group_1st, _ = pick_1st(8)
        group_2nd = pick_2nd(1, 9)
        random.shuffle(group_2nd)

        result = []
        for i, num in enumerate(group_2nd):
            result.append(group_1st[i]+[num])

    elif choice == "2":
        part_1, part_2 = pick28_2nd()

        result = []
        for num in part_1:
            result1, result2, _ = pick_28()
            for sublist in result1:
                result.append(sublist + [num])

        for num in part_2:
            result1, result2, _ = pick_28()
            for sublist in result2:
                result.append(sublist + [num])

    elif choice == "3":
        group_2nd = pick_2nd(1, 9)
        random.shuffle(group_2nd)

        result = []
        for num in group_2nd:
            group_1st, _ = pick_1st(7)
            for sublist in group_1st:
                result.append(sublist + [num])

    elif choice == "4":
        group_2nd = pick_2nd(1, 9)
        random.shuffle(group_2nd)

        result = []
        for num in group_2nd:
            group_1st, _ = pick_1st(13)
            for sublist in group_1st:
                result.append(sublist + [num])

    show_number(result)
    winner_number(result)
    print(_)
