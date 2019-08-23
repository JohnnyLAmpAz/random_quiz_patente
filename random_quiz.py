#!/usr/bin/env python3


# LORENZO BRIVIO - random "italian drive license B" quiz opener

import sys
import os.path
import webbrowser as wb
import random

# if '-y' option is passed then skip the prompt and start directly
if not len(sys.argv) == 2 or not sys.argv[1] == '-y':
    input('Click enter to open a random quiz: ')

path = os.path.join(os.path.dirname(__file__),".done.txt")

# if file doesn't exists then create one
if not os.path.exists(path):
    open(path, 'w').close()

# open the file with already done quizes
#   "r+": Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
fo = open(path, 'r+')

# read quiz numbers
done = fo.read().split()

# generate a random quiz number
while True:
    n = random.randint(1, 657)
    if not str(n) in done:
        break

# add n at the end of done file
fo.seek(0, 2)
fo.write('%d\n' % n)
fo.close()

# open the quiz
print('Scheda ministeriale n.%d' % n)
sito = 'https://www.patentati.it/quiz-patente-b/esame-%d.html'
wb.open_new_tab(sito % n)  # open it in the browser
