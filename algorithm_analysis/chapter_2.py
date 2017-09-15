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
        one_group_len = int(round(float(len(balls_list))/float(groups_amount)))
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
        print 'First odd group: %s' %  odd_group

        groups = self._group_balls(odd_group, 2)
        print 'Second odd group: %s' % groups
        odd_ball = self._find_odd_group(groups)
        return odd_ball

balls = [7, 7, 7, 7, 7, 6, 7, 7]
odd_ball = IdentifyOddBall(balls)
print odd_ball.find_odd_ball()