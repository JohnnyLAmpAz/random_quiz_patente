#!/usr/bin/env python3


# LORENZO BRIVIO - random italian drive license quiz opener

import sys
import webbrowser as wb
import random

sito = 'https://www.patentati.it/quiz-patente-b/esame-%d.html'

if not len(sys.argv) == 2 or not sys.argv[1] == '-y':
    input('Click enter to open a random quiz: ')

n = random.randint(1, 657) # generate a random quiz number
print('Scheda ministeriale n.%d' % n)
wb.open_new_tab(sito % n) # open it in the browser
