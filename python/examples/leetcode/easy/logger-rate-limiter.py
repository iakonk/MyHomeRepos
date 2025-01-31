class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.uniq_recs = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.uniq_recs:
            self.uniq_recs[message] = timestamp + 10
            return True
        elif timestamp >= self.uniq_recs[message]:
            self.uniq_recs[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
obj = Logger()
for param in [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]:
    if param:
        print(obj.shouldPrintMessage(*param))
