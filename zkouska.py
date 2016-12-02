# -*- coding: utf-8 -*-
import random


file_s = open('vetyS.txt', 'r')
file_t = open('vetyT.txt', 'r')

lines_s = file_s.readlines()
lines_t = file_t.readlines()

def simulate():
    index_s = random.randint(0, len(lines_s) - 1)
    index_t = random.randint(0, len(lines_t) - 1)

    print('#########################################')
    print('Vaše věty jsou: ')
    print(lines_s[index_s])
    print(lines_t[index_t])

def run():
    decision = raw_input('Pro zkoušku z MA3 stiskněte enter.')
    if decision == '':
        simulate()
    elif decision == 'vse':
        print("vse")

def main():
    rep = True
    run()
    while rep:
        repeat = raw_input('Vybrali jste si špatně? Zkuste to znovu, zmáčkněte enter. Pro ukončení napiště konec: ')
        if repeat == '':
            simulate()
        elif repeat == 'konec':
            rep = False

main()

#for event in pygame.event.get():
#    if event.type == pygame.KEYDOWN:
#        if event.key == pygame.K_KP_ENTER:
#            simulate()