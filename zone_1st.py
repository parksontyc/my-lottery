import random
from secrets import SystemRandom


def pick_1st(groups):
    list_1st = list(range(1, 39))

    counts = {i: 0 for i in range(1, 39)}

    # 取出8組, result就是用來放8組數字
    result = []
    for i in range(groups):
        # 取出6個數字, numbers放六個數字
        numbers = []
        while len(numbers) < 6:
            if not list_1st:
                list_1st = list(range(1, 39))
            SystemRandom().shuffle(list_1st)
            num = list_1st.pop(0)

            # 檢查數字是否重複, 並計數
            if num in numbers:
                continue
            else:
                numbers.append(num)
                counts[num] += 1

        result.append(numbers)

    return result, counts


if __name__ == "__main__":
    group_1st, count_1st = pick_1st(7)
    print(group_1st)
    print(count_1st)
