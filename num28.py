import random
from secrets import SystemRandom


def pick_28():
    list_1st = list(SystemRandom().sample(range(1, 39), 18))
    remain_list_1st = [i for i in list(range(1, 39))
                       if i not in list_1st]

    counts = {i: 0 for i in range(1, 39)}

    result_1 = []
    for _ in range(3):
        numbers = []
        while len(numbers) < 6:
            SystemRandom().shuffle(list_1st)
            num = list_1st.pop(0)
            numbers.append(num)
            counts[num] += 1
        result_1.append(numbers)

    result_2 = []
    for _ in range(4):
        numbers = []
        while len(numbers) < 6:
            if not remain_list_1st:
                remain_list_1st = list(range(1, 39))
            SystemRandom().shuffle(remain_list_1st)
            num = remain_list_1st.pop(0)

            if num in numbers:
                continue
            else:
                numbers.append(num)
                counts[num] += 1
        result_2.append(numbers)

    return result_1, result_2, counts


if __name__ == "__main__":
    a, b, count = pick_28()
    print(a)
    print(b)
    print(count)
