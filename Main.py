from bin.TuringMachine import TuringMachine 
from bin.JsonOperator import JsonOperator
            
     
def main():
    jsonOp = JsonOperator()
    data = jsonOp.readJson("bin/turingmachine.json")

    tapes = (
        "__1THE_QUICK_BROWN_FOX_JUMPS_OVER_THE_LAZY_DOG__",
        "*ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    )
    
    transitions = {}
    
    for state in data['transitions']:
        transitions[state] = {}
        for simbols in data['transitions'][state]:
            transitions[state][tuple(simbols.replace("(", "").replace(")", "").replace("'", "").split(","))] = data['transitions'][state][simbols]
    
    print(data['input_alphabet'])
    
    MT = TuringMachine((tapes[0], tapes[1],tapes[1]), data['states'], 
                       data['input_alphabet'], data['tape_alphabet'],
                       data['initial_state'], data['accept_states'],
                       transitions)
    
    MT.run()
    
if __name__ == '__main__':
    main()