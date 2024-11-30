#!/usr/bin/env python

import os
import sys
import getpass
import garth

if getattr(sys, 'frozen', False):
    # If we're running as a py installer bundle
    SCRIPT_DIR = os.path.dirname(sys.executable)
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

domain = input("Garmin domain [garmin.com]: ") or 'garmin.com'
username = input("Username (e-mail): ")
if not sys.stdin.isatty():  # This terminal cannot support input without displaying text
    print(f'*WARNING* The current shell ({os.name}) cannot support hidden text entry.')
    print(f'Your password entry WILL BE VISIBLE.')
    print(f'If you are running a bash shell under windows, try executing this program via winpty:')
    print(f'>winpty python {sys.argv[0]}')
    password = input("Password (will be shown): ")
else:
    password = getpass.getpass("Password: ")

garth.configure(domain=domain)
try:
    garth.login(username, password)
    garth.save('%s/garth' % SCRIPT_DIR)
except Exception as e:
    print(e)
