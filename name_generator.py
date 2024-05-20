# name_generator.py
#
# By TJ Hertz, 2024
#
# Given a list of adjectives, nouns and verbs, this script generates random names for your 
# song/band/project/label/whatever.
# 
# Simply feed it a newline-separated list of adjectives, nouns and verbs when prompted, and
# let it do the rest.
#

import random

mode = input('\nChoose mode: "1" (ADJECTIVE NOUN), "2" (NOUN NOUN), "3" (ADJECTIVE VERB), "4" (RANDOM MIX) (default)\n')
if mode == '':
    mode = '4'

if mode not in ['1','2','3','4']:
    raise RuntimeError("Unknown input mode")

mode = int(mode)

if mode != 2:
    print("\nEnter adjectives one at a time or leave input blank to continue:\n")
    adjectives = []
    while 1:
        val = input()
        if val == "":
            break
        else:
            adjectives += [val]

print("\nEnter nouns one at a time or leave input blank to continue:\n")
nouns = []
while 1:
    val = input()
    if val == "":
        break
    else:
        nouns += [val]

if mode == 3 or mode == 4:
    print("\nEnter verbs one at a time or leave input blank to continue:\n")
    verbs = []
    while 1:
        val = input()
        if val == "":
            break
        else:
            verbs += [val]

shortlist = []
while True:
    if mode != 4:
        type = mode    
    else:
        type = random.choice([1,2,3])
    
    if type == 1:
        candidate = f'{random.choice(adjectives)} {random.choice(nouns)}'
    elif type == 2:
        candidate = f'{random.choice(nouns)} {random.choice(nouns)}'
    elif type ==3:
        candidate = f'{random.choice(adjectives)} {random.choice(verbs)}'
    
    print ('\n\n' + candidate + '\n')
    next_step = input('Add to shortlist? (enter "y" to add to shortlist, "custom" to add a custom entry, leave blank to skip to the next idea, "done" to view results)\n')
    if next_step == 'y':
        shortlist += [candidate]
        print ('Added to shortlist!\n')
    elif next_step == 'n' or '':
        continue
    elif next_step == 'done':
        break
    elif next_step == 'custom':
        shortlist += [input('Enter custom name to add to shortlist:\n')]
    else:
        print ('\nUnknown input! \n')

print ("\n\nShortlist:")
for item in shortlist:
    print(item)
