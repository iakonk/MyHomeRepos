class IdentifyFalseBag(object):
    """
    You are given 10 bags of gold coins. Nine bags contain coins that each weigh 10
    grams. One bag contains all false coins that weigh one gram less. You must identify
    this bag in just one weighing. You have a digital balance that reports the weight of
    what is placed on it.
    """

    def __init__(self, bags, expected_coin_weight):
        """ """
        self.bags = bags
        self.expected_coin_weight = expected_coin_weight
        self.taken_coins_amount = 0

    def _weight_bags(self, bags):
        """ [[10], [9, 9], [10, 10, 10]] """
        total_weight = 0
        for bag in bags:
            total_weight += sum(bag)
            self.taken_coins_amount += len(bag)
        return total_weight

    def _take_coins(self):
        """ """
        bags_ = []
        for n, bag in enumerate(self.bags):
            bags_.append(bag[: n + 1])
        return bags_

    def identify_false_bag(self):
        """ """
        bags_ = self._take_coins()
        total_weight = self._weight_bags(bags_)
        false_bag_num = self.expected_coin_weight * self.taken_coins_amount - total_weight
        return false_bag_num


bags = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        ]
false_bag = IdentifyFalseBag(bags, 10)
assert false_bag.identify_false_bag() == 2


class IdentifyOddBall(object):
    """
    You have eight balls all of the same size. Seven of them weigh the same, and one
    of them weighs slightly more. How can you find the ball that is heavier by using a
    balance and only two weighing?

    Solution works with len(list) == 8, otherwise more than 2 weighing are required
    """

    def __init__(self, balls):
        self.balls = balls

    def _weigh_group(self, one_group):
        """ """
        return sum(one_group)

    def _find_odd_group(self, balls_groups):
        """ """
        while balls_groups:
            curr_group = balls_groups.pop(0)
            try:
                next_group = balls_groups.pop(0)
            except IndexError:
                return curr_group

            curr_group_weigh = self._weigh_group(curr_group)
            next_group_weigh = self._weigh_group(next_group)
            if curr_group_weigh == next_group_weigh:
                continue
            if curr_group_weigh > next_group_weigh:
                return next_group
            else:
                return curr_group

    def _group_balls(self, balls_list, groups_amount):
        """ return: [[7, 7, 7], [7, 7, 7], [6, 7]] """
        result = []

        one_group = []
        one_group_len = int(round(float(len(balls_list)) / float(groups_amount)))
        while balls_list:
            one_ball = balls_list.pop(0)
            one_group.append(one_ball)
            if len(one_group) == one_group_len and len(result) < groups_amount:
                result.append(one_group)
                one_group = []
                groups_amount -= 1
            else:
                continue
        if one_group:
            result.append(one_group)
        return result

    def find_odd_ball(self):
        """ """
        groups = self._group_balls(self.balls, 3)
        odd_group = self._find_odd_group(groups)
        print 'Odd group: %s' % odd_group

        groups = self._group_balls(odd_group, 2)
        odd_ball = self._find_odd_group(groups)
        print 'Odd ball %s' % odd_ball
        return odd_ball


balls = [7, 7, 7, 7, 7, 6, 7, 7]
odd_ball = IdentifyOddBall(balls)
assert odd_ball.find_odd_ball() == [6]


def selection_sort(list_):
    """
     Time complexity"
     Best: O(n^2),  Average: O(n^2), Worst: O(n^2)
    """
    for curr_elem_index in range(len(list_)):
        min_elem_index = curr_elem_index

        for next_elem_index in range(curr_elem_index + 1, len(list_)):
            if list_[next_elem_index] < list_[min_elem_index]:
                min_elem_index = next_elem_index

        min_elem = list_[min_elem_index]
        list_[min_elem_index] = list_[curr_elem_index]
        list_[curr_elem_index] = min_elem


lst = [18, 5, 3, 19, 6, 0, 7, 4, 2, 5]
selection_sort(lst)
print lst


def insertion_sort(list_):
    """
    Time complexity:
    Worst: O(n^2)
    """
    for curr_index in range(1, len(list_)):
        curr_val = list_[curr_index]
        curr_position = curr_index

        while curr_position > 0 and list_[curr_position - 1] > curr_val:
            list_[curr_position] = list_[curr_position - 1]
            curr_position -= 1
        list_[curr_position] = curr_val

lst = [18, 5, 3, 19, 6, 0, 7, 4, 2, 5]
insertion_sort(lst)
print lst

