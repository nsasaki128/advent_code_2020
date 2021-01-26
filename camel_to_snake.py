import re

import sys
import fileinput
def main():
    for line in fileinput.input():
        print(re.sub("([A-Z])",lambda x:"_" + x.group(1).lower(), line).replace("_false", "False").replace("_true", "True").replace("_none", "None"), end="")


if __name__ == '__main__':
    main()

