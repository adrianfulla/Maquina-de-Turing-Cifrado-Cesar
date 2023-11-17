class TuringMachine:
    def __init__(self, tapes, initial_state, transition_function):
        self.tape1 = tapes[0]
        self.tape2 = tapes[1]
        self.tape3 = tapes[2]
        self.head1 = 0      
        self.head2 = 0      
        self.head3 = 0      
        self.state = initial_state
        self.transition_function = transition_function

    def step(self):
        current_symbol1 = self.tape1[self.head1]
        current_symbol2 = self.tape2[self.head2]
        current_symbol3 = self.tape3[self.head3]

        transition = self.transition_function.get((self.state, current_symbol1, current_symbol2, current_symbol3))

        if transition:
            new_state, new_symbol1, move1, new_symbol2, move2, new_symbol3, move3 = transition

            self.tape1[self.head1] = new_symbol1
            self.tape2[self.head2] = new_symbol2
            self.tape3[self.head3] = new_symbol3

            self.head1 += move1
            self.head2 += move2
            self.head3 += move3

            if self.head1 == len(self.tape1):
                self.tape1.append('B')
            if self.head2 == len(self.tape2):
                self.tape2.append('B')
            if self.head3 == len(self.tape3):
                self.tape3.append('B')

            self.state = new_state
        else:
            print("La máquina se detuvo.")
            return

    def run(self):
        while True:
            print(f"Estado: {self.state}")
            print(f"Cinta 1: {''.join(self.tape1)}")
            print(f"Cinta 2: {''.join(self.tape2)}")
            print(f"Cinta 3: {''.join(self.tape3)}")
            print()

            self.step()