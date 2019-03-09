Created on Thu Mar  7 17:29:57 2019

@author: francescobenfenati
"""
import sys
rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }

def generate_state():
    return "................0................"

def evolve(stato):                                  #riceve una stringa
    stato_diviso = list(stato)
    new_state= ['.']                                #aggiungo un . all'inizio dello stato
    for i in range(31):
        string_to_translate = ''.join(stato_diviso[i:i+3])   
        translated_string = rule30[string_to_translate]
        new_state.append(translated_string)
    new_state.append('.')                           #aggiungo un . alla fine dello stato
       
    return new_state                                #restituisce la lista new_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]                    #state_seq è una lista con dentro come primo membro la
                                                    #stringa dello stato iniziale  
    
    for i in range(nsteps):                         #per il numero di stati che voglio disegnare
        
        old_state = [states_seq[-1]]                #old_state è una lista con un unico membro
                                                    #che è l'ultimo membro di states_eq
       
        stato_listato = list(states_seq[i])         #scindo l'unico membro-stringa "..0.." in una lista con 
                                                    #i singoli '.' o '0'
        
        for j in range(33):
        
            if stato_listato[j] == '.':
                sys.stdout.write(' ')
            else:
                sys.stdout.write(u'\u2588')
        sys.stdout.write('\n')
        
        old_string_state = ''.join(old_state[0:1])  #rende stringa l'unico membro-stringa di old_state
        
        new_state = evolve(old_string_state)        #new_state è una lista con singoli membri . e 0
       
        new_string_state = ''.join(new_state[0:33]) #lista composta da 33 '.' e '0' che unisco in una stringa
        
        states_seq.append(new_string_state)
    
    return states_seq

########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1


simulation(16)
