# 929 Unique Email Addresses
'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
'''
'''
def numUniqueEmails(emails):
    # seperate local name and domain name using split('@')
    local_name_unfiltered = []
    domain_name = []
    local_name_filtered = []
    for email in emails:
        local_name_unfiltered.append(email.split('@')[0])
        domain_name.append(email.split('@')[1])
    for local_name in local_name_unfiltered:
        temp = ''
        for char in local_name:
            if char == '+':
                break
            if char != '.':
                temp += char
        local_name_filtered.append(temp)
    unique_email = set()
    for local, domain in zip(local_name_filtered, domain_name):
        unique_email.add((local, domain))
    return len(unique_email)
'''
def numUniqueEmails(emails):        # more concise code and use split() and replace()
    unique_email = set()
    for email in emails:
        local_name = email.split('@')[0].split('+')[0].replace('.', '')
        domain_name = email.split('@')[1]
        unique_email.add(local_name + '@' + domain_name)
    return len(unique_email)
emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com",
          "b@leetcode.com",
          "c@leetcode.com"]
print(numUniqueEmails(emails))