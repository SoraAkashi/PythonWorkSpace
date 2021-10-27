import re
m = re.search(r'(?<=-)\w+', 'spam-egg')
m.group(0)
'egg'