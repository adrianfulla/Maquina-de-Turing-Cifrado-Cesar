from time import sleep
import os
class TuringMachine:
    def __init__(self, tapes, states, input_alphabet, tape_alphabet, initial_state, accept_states,transition_function):
        self.tapes = [list(tapes[0]), list(tapes[1]), list(tapes[2])]
        self.heads = [0,0,0]
        self.state = initial_state
        self.transition_function = transition_function
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.accept_states = accept_states
        self.recursion = 0
        self.steps = 0
        
        self.n = ["1","2","3","4","5","6","7","8","9",] 
        self.alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def step(self):
        symbol1 = self.tapes[0][self.heads[0]]
        symbol2 = self.tapes[1][self.heads[1]]
        symbol3 = self.tapes[2][self.heads[2]]
        if symbol1 in self.n:
            symbol1 = 'n'
            if symbol2 in self.alp:
                symbol2 = 'y'
            if symbol3 in self.alp:
                symbol3 = 'z'
        elif symbol1 in self.alp:
            if symbol1 == symbol2:
                symbol1, symbol2 = 'x', 'x'
            else:
                symbol1 = 'x'
                if symbol2 in self.alp:
                 symbol2 = 'y'
            if symbol3 in self.alp:
                symbol3 = 'z'
        else:
            if symbol2 in self.alp:
                 symbol2 = 'y'
            if symbol3 in self.alp:
                symbol3 = 'z'
        
        inputS = (symbol1, symbol2, symbol3)
        
       # print(f"input: {inputS}, heads:{self.heads}")
        
        transition = []
        
        if inputS in self.transition_function[self.state]:
            transition = list(self.transition_function[self.state][inputS])
        #    print(f"transicion: {transition}")
        

        if transition:
            new_state, new_symbols, moves = transition
            
            if new_symbols[0] == 'n-1':
                self.tapes[0][self.heads[0]] = str(int(self.tapes[0][self.heads[0]])-1)
            elif new_symbols[0] == 'z':
                self.tapes[0][self.heads[0]] = self.tapes[2][self.heads[2]]
            elif new_symbols[0] == '9':
                self.tapes[0][self.heads[0]] = '9'
            elif new_symbols[0] == '_':
                self.tapes[0][self.heads[0]] = '_'
            if new_symbols[1] == 'x' or new_symbols[1] == 'y':
                self.tapes[1][self.heads[1]] = self.tapes[1][self.heads[1]]
            if new_symbols[2] == 'z':
                self.tapes[2][self.heads[2]] = self.tapes[2][self.heads[2]]
                
            for i in range(len(self.heads)):
                if moves[i] == 'R':
                    self.heads[i] += 1
                elif moves[i] == 'L':
                    self.heads[i] -= 1

            if self.heads[0] == len(self.tapes[0]):
                self.tapes[0].append('_')
                self.recursion += 1
            if self.heads[1] == len(self.tapes[1]):
                self.tapes[1].append('_')
            if self.heads[2] == len(self.tapes[2]):
                self.tapes[2].append('_')

            self.state = new_state
            
            if self.recursion >= 10:
                print("Recursion maxima lograda")
                return False
            
            self.steps += 1
            
            return True
        else:
            print("La máquina se detuvo.")
            return False

    def run(self):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        while True:
            self.printStatus()

            if not self.step():
                if self.state in self.accept_states:
                    print(f"La cadena SI fue aceptada en {self.steps}")
                else:
                    print(f"La cadena NO fue aceptada {self.steps}")
                return self.tapes[0]
            
            sleep(0.05)
            
            
    def printStatus(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        cintas =["","",""]
        for i in range(len(self.tapes)):
            for j in range(self.heads[i]):
                cintas[i] += (self.tapes[i][j])
            cintas[i] +=(f"[{self.tapes[i][self.heads[i]]}]")
            for j in range(self.heads[i]+1, len(self.tapes[i])):
                cintas[i] += (self.tapes[i][j])
                
        exp = (f"Estado: {self.state}\nCinta 1: {cintas[0]}\nCinta 2: {cintas[1]}\nCinta 3: {cintas[2]}\n")

        print(exp)
        
        
        