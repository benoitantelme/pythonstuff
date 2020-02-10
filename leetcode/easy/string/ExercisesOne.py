from typing import List


def defangIPaddr(address: str) -> str:
    res = ""
    for char in address:
        if char == '.':
            res += "[.]"
        else:
            res += char

    return res


print(defangIPaddr("1.1.1.1"))


def balancedStringSplit(s: str) -> int:
    res = 0
    r = 0
    l = 0

    for char in s:
        if char == 'R':
            r += 1
        else:
            l += 1
        if l == r and l != 0:
            res += 1
            l = 0
            r = 0

    return res


print(balancedStringSplit("RLRRLLRLRL"))


def freqAlphabets(s: str) -> str:
    res = ""
    i = 0
    while i < len(s):
        if i < len(s) - 2 and s[i + 2] == '#':
            res += chr(96 + int(s[i:i + 2]))
            i += 3
        else:
            res += chr(96 + int(s[i]))
            i += 1
    return res


print(freqAlphabets("110#11#12"))


def numUniqueEmails(emails: List[str]) -> int:
    addresses = set()
    for email in emails:
        split = email.split('@')
        local_name = split[0]

        if '+' in local_name:
            local_name = local_name.split('+')[0]

        if '.' in local_name:
            local_name = ''.join(local_name.split('.'))

        addresses.add(local_name + '@' + split[1])

    return len(addresses)


print(numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))


def findLUSlength(a: str, b: str) -> int:
    if a == b:
        return -1
    la = len(a)
    lb = len(b)
    if la == lb:
        return la
    elif la > lb:
        return la
    else:
        return lb


print(findLUSlength("aba", "cdc"))

