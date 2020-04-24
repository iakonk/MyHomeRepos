class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = {}
        for dom in cpdomains:
            v_cnt, dom = dom.split()
            subdoms = dom.split('.')
            for i in range(0, len(subdoms)):
                key = '.'.join(subdoms[i:])
                result.setdefault(key, 0)
                result[key] += int(v_cnt)
        return ['{} {}'.format(cnt, dom) for dom, cnt in result.items()]


print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
