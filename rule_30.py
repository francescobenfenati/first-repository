#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:29:57 2019

@author: francescobenfenati
"""
#%% generating
import sys
import random
RULES = {30: {"000": '.',"00.": '.',"0.0": '.',"...": '.',
              "0..": '0',".00": '0',".0.": '0',"..0": '0'},
        
        
         90: {"000": ".", "00.": "0", "0.0": ".", "0..": "0",
            ".00": "0", ".0.": ".", "..0": "0", "...": "."},
                
         110: {"000": '.', "00.": '0', "0.0": '0', "0..": '.',
              ".00": '0', ".0.": '0', "..0": '0', "...": '.'},
                        
         184: {"000": "0", "00.": ".", "0.0": "0", "0..": "0",
              ".00": "0", ".0.": ".", "..0": ".", "...": "."}
         }


def generate_state(number_of_cells):                    #genera uno stato con n celle di cui tutti '.' tranne uno '0' al centro
    
    intermediate_position = int((number_of_cells-1)/2)  #posizione "intermedia" dove mettere lo '0'
    state = []
    
    for i in range(intermediate_position):
        state.append('.')

    state.append('0')

    for j in range(intermediate_position+1,number_of_cells):
        state.append('.')
    
    return state


def evolve(stato,nrule,border_rule):                                      #riceve ora una lista
    
    length = len(stato)
    new_state = ['.']                                   #aggiungo un . all'inizio dello stato
    if border_rule == 1:
        for i in range(length-2):
            string_to_translate = ''.join(stato[i:i+3])
            translated_cell = RULES[nrule][string_to_translate]   #eseguo la traduzione dei tripletti
            new_state.append(translated_cell)
        new_state.append('.')                               #aggiungo un . alla fine dello stato
    elif border_rule == 2:
        for i in range(length):
            if i<length-2:
                string_to_translate = ''.join(stato[i:i+3])
                translated_cell = RULES[nrule][string_to_translate]
                new_state.append(translated_cell)
            elif i == length -2:
                string_to_translate = stato[i]+stato[-1]+stato[0]
                translated_cell = RULES[nrule][string_to_translate]
                new_state.append(translated_cell)
            elif i == length-1:
                string_to_translate = stato[-1]+stato[0]+stato[1]
                new_state[0] = translated_cell
    elif border_rule == 3:
        for i in range(length):
            if i == 0:
                string_to_translate = stato[i+1]+stato[i]+stato[i+1]
                translated_cell = RULES[nrule][string_to_translate]
                new_state[0] = translated_cell
                continue
            elif i == length-1:
                string_to_translate = stato[i-1]+stato[i]+stato[i-1]
                translated_cell = RULES[nrule][string_to_translate]
                new_state.append(translated_cell)
            else:
                string_to_translate = stato[i-1]+stato[i]+stato[i+1]
                translated_cell = RULES[nrule][string_to_translate]
                new_state.append(translated_cell)

    return new_state                                    #restituisce la lista new_state

#%% simulation function
def simulation(ncells,nrule,border_rule,number_states):
    initial_state = generate_state(ncells)
    states_seq = [initial_state]                        #state_seq è una lista con dentro come primo membro lo stato iniziale
    if number_states == "d":
        number_states = int(((ncells-1)/2)+1)
    else:
        number_states = int(number_states)
    for i in range(number_states):
        old_state = states_seq[-1]                      #old_state è la lista-stato presente in ultima posizione di states_seq
    
        for j in range(ncells):
        
            if old_state[j] == '.':                     #disegno le celle
                sys.stdout.write('  ')
            else:
                sys.stdout.write(u'\u2588')
                sys.stdout.write(u'\u2588')
        sys.stdout.write('\n')
        
        new_state = evolve(old_state,nrule,border_rule)                   #new_state è la lista-stato con singoli membri . e 0
        states_seq.append(new_state)
    return states_seq

########################################################
#%% testing
def test_generation_valid_state():                      #verifico se il seed generato ha solo . e 0
    n = random.randint(1,20)                            #come posso verificare per un qualsiasi input?
    state = generate_state(n)
    assert set(state) == {'.', '0'}


def test_generation_single_alive():                     #verifico se il seed ha uno e uno solo '0'
    n = random.randint(1,20)
    state = generate_state(n)
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1

def test_evolve_valid_state():                          #verifico che, se lo stato di input ha solo . e 0, anche l'output sarà tale
    n = random.randint(1,20)
    nb = [1,2,3]
    rule = [30,90,110,184]
    for i in nb:
        for r in rule:
            state = evolve(generate_state(n),r,i)
            assert set(state) == {'.','0'}


def test_generate_length():                             #verifico che la lunghezza dello stato generato sia quella voluta
    n = random.randint(1,20)
    x = generate_state(n)
    l = len(x)
    assert l == n

def test_levolved_equal_lgenerated():                   #verifico che len(generato) = len(evoluto)
    n = random.randint(1,20)
    nb = [1,2,3]
    rule = [30,90,110,184]
    status = generate_state(n)
    for i in nb:
        for r in rule:
            x = evolve(status,r,i)
            assert len(x) == len(status)


#%% main
y=1
a=0
while y==1:
    while a==0:
        nr = input('Quale regola vuoi applicare? scegli fra [30,90,110,184]: ')
        try:
            nrule = int(nr)
            if nrule <0:
                print("Numero non valido")
                continue
            lista = [30,90,110,184]
            for i in range(4):
                if nrule == lista[i]:
                    a=1
                    break
                elif i == 3:
                    print('Non esiste questa regola o comunque non la conosco')
    
        except ValueError:
            print('Invalid input')
    r = input("Come vuoi i bordi, costanti [1], circolari [2] o riflettenti[3]?: ")
    border = int(r)

    nb = input('Quante celle vuoi per ogni stato?: ')
    
    try:
        number = int(nb)
        if number <0:
            print("Numero non valido")
    except ValueError:
        print("Invalid input")

    else:
        numero = input("quante iterazioni vuoi?('d' per default): ")
        simulation(number,nrule,border,numero)
        x = input('Vuoi generarne un altro? Digita \'1\' se sì, altrimenti \'0\': ')
        y = int(x)
        a=0

