import re

str = "Arizona: 479, 501, 870. California: 209, 213, 650."
match = re.findall("\d", str)
print(match)

str = "The ghost that says boo haunts the loo."
match = re.findall(".oo", str)
print(match)
