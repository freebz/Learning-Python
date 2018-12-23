# 패턴 매칭

import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
match.group(1)
# 'Python '


match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
match.groups()
# ('usr', 'home', 'lumberjack')

re.split('[/:]', '/usr/home/lumberjack')
# ['', 'usr', 'home', 'lumberjack']
