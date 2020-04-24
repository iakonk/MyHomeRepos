"""
cat ips.txt | python find_missing_ips.py - '192.0.2.16/29'

cat ips.txt
192.0.2.16
192.0.2.23
"""
import sys
import argparse
import netaddr


class IPRangeParser(object):
    def __init__(self, net_mask):
        self.network = netaddr.IPNetwork(net_mask)
        self.prev_ip = None

    def _print_range(self, start_ip=None, end_ip=None):
        """prints inclusive range"""
        for ip in netaddr.iter_iprange(start_ip, end_ip):
            print(ip)

    def print_missing(self, input):
        for ind, line in enumerate(input):
            file_ip = netaddr.IPAddress(line)
            range_ip = self.network[ind]
            if int(file_ip) > int(range_ip):
                if self.prev_ip:
                    self._print_range(start_ip=int(self.prev_ip) + 1, end_ip=int(file_ip) - 1)
                else:
                    self._print_range(start_ip=self.network[0], end_ip=int(file_ip) - 1)
            self.prev_ip = file_ip


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('net_mask', type=str, )
    args = parser.parse_args()

    ip_parser = IPRangeParser(args.net_mask)
    ip_parser.print_missing(args.input)
