import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

f = figlet_format('missile!', font='starwars')
print f

cprint(f, 'yellow', 'on_red', attrs=['bold'])