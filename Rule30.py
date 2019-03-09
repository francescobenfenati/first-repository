"""
Created on Thu Mar  7 17:29:57 2019

@author: francescobenfenati
"""

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
    return ".....0......"

def evolve(stato): #riceve una stringa
    stato_diviso = list(stato)
    new_state= ['.']    
    for i in range(10):
        string_to_translate = ''.join(stato_diviso[i:i+3])   
        translated_string = rule30[string_to_translate]
        new_state.append(translated_string)
    new_state.append('.')
       
    return new_state #restituisce una lista

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    
    for i in range(nsteps):
        print(states_seq[i])
        old_state = [states_seq[-1]]
        #print(states_seq)
        #print(old_state)
        old_string_state = ''.join(old_state[0:12])
        #print(old_string_state)
        new_state = evolve(old_string_state)
        #print(new_state)
        
        new_string_state = ''.join(new_state[0:12])
        
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


#nuovo_stato = evolve(stato)
#stato_stringato = ''.join(nuovo_stato[0:10])
#print(stato_stringato)


simulation(10)

#first commit
