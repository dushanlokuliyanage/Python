import re

txt = "The rain is hain and dain"

print( re.findall("ai", txt))

import camelcase
c = camelcase.CamelCase()
txt = "hello man"
print(c.hump(txt))