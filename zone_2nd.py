import random


def pick_2nd(num, scope):
    '''選擇第二區數字，參數表每個數字重複多少次'''
    zone_2nd = [i for i in range(1, scope)
                for _ in range(num)]
    # random.shuffle(zone_2nd)

    return zone_2nd


def pick28_2nd():
    list_2nd = list(random.sample(range(1, 9), 4))
    remain_list_2nd = [i for i in list(range(1, 9))
                       if i not in list_2nd]

    list_2nd = [i for i in list_2nd for _ in range(1)]
    print(list_2nd)

    remain_list_2nd = [i for i in remain_list_2nd
                       for _ in range(1)]
    print(remain_list_2nd)

    return list_2nd, remain_list_2nd


if __name__ == "__main__":
    list_2nd = pick_2nd(2, 9)
    # print(list_2nd)
    pick28_2nd()
    # print(list_2nd_test)
