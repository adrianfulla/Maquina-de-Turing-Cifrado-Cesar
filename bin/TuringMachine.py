class TuringMachine:
    def __init__(self, tapes, states, input_alphabet, tape_alphabet, initial_state, accept_states,transition_function):
        self.tape1 = list(tapes[0])
        self.tape2 = list(tapes[1])
        self.tape3 = list(tapes[2])
        self.heads = [0,0,0]
        self.state = initial_state
        self.transition_function = transition_function
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.accept_states = accept_states
        
        self.n = ["1","2","3","4","5","6","7","8","9",] 
        self.alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def step(self):
        symbol1 = self.tape1[self.heads[0]]
        symbol2 = self.tape2[self.heads[1]]
        symbol3 = self.tape3[self.heads[2]]
        if symbol1 in self.n:
            symbol1 = 'n'
        elif symbol1 in self.alp:
            if symbol1 == symbol2:
                symbol1, symbol2 = 'X', 'X'
            else:
                symbol1, symbol2 = 'X', 'Y'
        
        inputS = (symbol1, symbol2, symbol3)
        
        print(f"input: {inputS}")
        
        transition = []
        
        if inputS in self.transition_function[self.state]:
            transition = self.transition_function[self.state][inputS]
            print(f"transicion: {transition}")
        

        if transition:
            new_state, new_symbols, moves = transition
            
            if new_symbols[0] == 'X' or new_symbols[0] == 'n':
                new_symbols[0] = self.tape1[self.heads[0]]
            if new_symbols[1] == 'X' or new_symbols[1] == 'Y':
                new_symbols[1] = self.tape2[self.heads[1]]
            if new_symbols[2] == 'Z':
                new_symbols[2] = self.tape3[self.heads[2]]
                

            self.tape1[self.heads[0]] = new_symbols[0]
            self.tape2[self.heads[1]] = new_symbols[1]
            self.tape3[self.heads[2]] = new_symbols[2]

            for i in range(len(self.heads)):
                if moves[i] == 'R':
                    self.heads[i] += 1
                elif moves[i] == 'L':
                    self.heads[i] -= 1

            if self.heads[0] == len(self.tape1):
                self.tape1.append('_')
            if self.heads[1] == len(self.tape2):
                self.tape2.append('_')
            if self.heads[2] == len(self.tape3):
                self.tape3.append('_')

            self.state = new_state
            return True
        else:
            print("La máquina se detuvo.")
            return False

    def run(self):
        while True:
            print(f"Estado: {self.state}")
            print(f"Cinta 1: {''.join(self.tape1)}")
            print(f"Cinta 2: {''.join(self.tape2)}")
            print(f"Cinta 3: {''.join(self.tape3)}")
            print()

            if not self.step():
                break