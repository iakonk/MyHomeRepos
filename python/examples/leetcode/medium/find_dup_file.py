class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        import re

        aggr = {}
        for item in paths:
            fpath, rest = item.split(" ", 1)
            rx = re.compile('([\w\d.]+)(\([\w\d.;:!,]+\))')
            for fname, fcnt in rx.findall(rest):
                aggr.setdefault(fcnt, [])
                aggr[fcnt].append('%s/%s' % (fpath, fname))
        return [v for _, v in aggr.items() if len(v) > 1 ]

print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))