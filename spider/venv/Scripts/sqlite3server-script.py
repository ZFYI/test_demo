#!C:\Users\15752\Desktop\spider\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlite3server==0.1.3','console_scripts','sqlite3server'
__requires__ = 'sqlite3server==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sqlite3server==0.1.3', 'console_scripts', 'sqlite3server')()
    )
