


# a, X, 9, < -- ordinary characters just match themselves exactly.
# . (a period) - - matches any single character except newline '\n'
# \w - - matches a "word" character: a letter or digit or underbar[a-zA-Z0-9_].
# \W - - matches any non-word character.
# \b - - matches word boundary ( in between a word character and a non word character)
# \s - - matches a single whitespace character - - space, newline, return, tab
# \S - - matches any non-whitespace character.
# \t, \n, \r - - tab, newline, return
# \d - - matches any numeric digit[0-9]
# \D matches any non-numeric character.
# ^ -- matches the beginning of the string, or specify omition of certain characters
# $ -- matches the end of the string
# \ -- escapes special character.
# (x | y | z) matches exactly one of x, y or z.
# (x) in general is a remembered group. We can get the value of what matched by using the groups() method of the object returned by re.search.
# x? matches an optional x character (in other words, it matches an x zero or one times).
# x * matches x zero or more times.
# x + matches x one or more times.
# x{m, n} matches an x character at least m times, but not more than n times.
# ?: matches an expression but do not capture it. Non capturing group.
# ?= matches a suffix but exclude it from capture. Positive lookahead.
# a(?=b) will match the "a" in "ab", but not the "a" in "ac"
# In other words, a(?=b) matches the "a" which is followed by the string 'b', without consuming what follows the a.
# ?! matches if suffix is absent. Negative look ahead.
# a(?!b) will match the "a" in "ac", but not the "a" in "ab"
# ?<= positive look behind
# [] matches for groupings of consecutive characters
# ?<! negative look behind

# Homework Exercise
# Print each persons name and twitter handle etc., using groups, should look like:
#  [
#     ([first name] [last name],
#      email, 
#      phone,
#      title,
#      Twitter handle)
# ]

import re

file = open('./names.txt', encoding='utf-8')

# read the text of the file and store it as Python data
data = file.read()

# always close the data stream
file.close()

info = re.findall(r'''
([\w+ \w+]*,\s[-\w+ ]+)
\s+
([-\d\w]*@[-.\w\d]+)
\s+
(\(?\d{3}\)?\s?-?\d{3}-\d{4})?
\s+
([\w+ ]*\w+,\s[\w+ ]+)?
\s+
(@\w+)?

''', data, re.X)
print(info)
