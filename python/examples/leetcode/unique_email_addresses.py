# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

import re


def find_unique_emails(emails):
    seen = set()
    for one_email in emails:
        recp, domain = None, None

        restricted_chars = re.match('(.*?)\+.*(@.*)', one_email)
        if restricted_chars:
            recp, domain = restricted_chars.groups()
        else:
            match = re.match('(.*)(@.*)', one_email)
            if match:
                recp, domain = match.groups()

        if recp and domain:
            seen.add(recp.replace('.', '')+domain)
    return len(seen)


assert find_unique_emails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert find_unique_emails(["fg.r.u.uzj+o.pw@kziczvh.com",
                          "r.cyo.g+d.h+b.ja@tgsg.z.com",
                          "fg.r.u.uzj+o.f.d@kziczvh.com",
                          "r.cyo.g+ng.r.iq@tgsg.z.com",
                          "fg.r.u.uzj+lp.k@kziczvh.com",
                          "r.cyo.g+n.h.e+n.g@tgsg.z.com",
                          "fg.r.u.uzj+k+p.j@kziczvh.com",
                          "fg.r.u.uzj+w.y+b@kziczvh.com",
                          "r.cyo.g+x+d.c+f.t@tgsg.z.com",
                          "r.cyo.g+x+t.y.l.i@tgsg.z.com",
                          "r.cyo.g+brxxi@tgsg.z.com",
                          "r.cyo.g+z+dr.k.u@tgsg.z.com",
                          "r.cyo.g+d+l.c.n+g@tgsg.z.com",
                          "fg.r.u.uzj+vq.o@kziczvh.com",
                          "fg.r.u.uzj+uzq@kziczvh.com",
                          "fg.r.u.uzj+mvz@kziczvh.com",
                          "fg.r.u.uzj+taj@kziczvh.com",
                          "fg.r.u.uzj+fek@kziczvh.com"]) == 2

assert find_unique_emails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]) == 3

assert find_unique_emails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]) == 1