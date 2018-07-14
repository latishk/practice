# length = int(input())
# array = list(map(int, input().split()))
# mid = length // 2
#
#
# def median(array):
#     length = len(array)
#     if length:
#         array = sorted(array)
#         return int((array[int((length - 1) / 2)] + array[int((length) / 2)]) / 2)
#
#
# def quartile():
#     if length % 2 == 0:
#         Q3 = median(array[mid:])
#     else:
#         Q3 = median(array[mid + 1:])
#
#     return median(array[:mid]), median(array), Q3
#
# print(median(array[:mid]))
# print(median(array))
# print(Q3)
#
#
# length = int(input())
# elements = list(map(int, input().split()))
# frequency = list(map(int, input().split()))
#
# dataset = []


# def median(array):
#     length = len(array)
#     if length:
#         array = sorted(array)
#         return ((array[int((length - 1) / 2)] + array[int((length) / 2)]) / 2)
#
#
# def get_mid(data):
#     return len(data) // 2
#
#
# def quartile(array, mid):
#     if length % 2 == 0:
#         Q3 = median(array[mid:])
#     else:
#         Q3 = median(array[mid + 1:])
#
#     return median(array[:mid]), median(array), Q3
#
#
# for e, f in zip(elements, frequency):
#     for _ in range(f):
#         dataset.append(e)
#
# dataset.sort()
# Q1, Q2, Q3 = quartile(dataset, get_mid(dataset))
# print(Q1, Q2, Q3)
# print(Q3 - Q1)


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if self.isOpenParentheses(c):
                stack.append(c)
            elif self.isParentheses(c):
                if len(stack):
                    if self.isMatch(stack[-1], c):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                continue
        if not len(stack):
            return True
        return False

    def isMatch(self, top, input):
        if (top == '{' and input == '}') or (top == '(' and input == ')') or (top == '[' and input == ']'):
            return True
        return False

    def isParentheses(self, input):
        if input in "{}[]()":
            return True
        return False

    def isOpenParentheses(self, input):
        if input in "{[(":
            return True
        return False


def share_stablized(current_share, new_share):
    for i in range(len(current_share)):
        if round(new_share[i], 5) != round(current_share[i], 5):
            return False
        return True


def get_new_share(market_share_list, switch_probablity):
    new_market_share = [0 for _ in range(len(market_share_list))]

    for index, share in enumerate(market_share_list):
        share_gained = 0
        share_retained = 0
        for index_2, probability in enumerate(market_share_list):
            if index == index_2:
                share_retained = market_share_list[index] * switch_probablity[index][index_2]
            else:
                share_gained += market_share_list[index_2] * switch_probablity[index_2][index]

        new_market_share[index] = share_gained + share_retained
    return new_market_share


def get_market_share(current_share, switch_probablity):
    market_share_list = [0.4, 0.6]

    switch_probablity = [[0.8, 0.2],
                         [0.1, 0.9]]

    new_market_share = get_new_share(market_share_list, switch_probablity)
    while not share_stablized(market_share_list, new_market_share):
        market_share_list = [x for x in new_market_share]
        new_market_share = get_new_share(market_share_list, switch_probablity)
    return [round(x, 4) for x in new_market_share]


print(get_market_share([0.4, 0.6], [[0.8, 0.2], [0.1, 0.9]]))
