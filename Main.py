from bin.TuringMachine import TuringMachine 
from bin.JsonOperator import JsonOperator
import sys
            
     
def cypher(n, expression):
    jsonOp = JsonOperator()
    data = jsonOp.readJson("bin/turingmachinecypher.json")
    
    expression = expression.upper().replace(" ", "_")

    tapes = (
        f"__{str(n)}{expression}__",
        "*ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    )
    
    transitions = {}
    
    for state in data['transitions']:
        transitions[state] = {}
        for simbols in data['transitions'][state]:
            transitions[state][tuple(simbols.replace("(", "").replace(")", "").replace("'", "").split(","))] = data['transitions'][state][simbols]
    
    
    MT = TuringMachine((tapes[0], tapes[1],tapes[1]), data['states'], 
                       data['input_alphabet'], data['tape_alphabet'],
                       data['initial_state'], data['accept_states'],
                       transitions)
    
    result = MT.run()
    result = ''.join(result).replace(" ", "_")
    pres = result.replace("_", " ")
    print(f"Expresion resultante: {pres}")
    return result
    
def decypher(n, expression):
    jsonOp = JsonOperator()
    data = jsonOp.readJson("bin/turingmachinedecypher.json")

    expression = expression.upper().strip("_")

    tapes = (
        f"__{str(n)}{expression}__",
        "*ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    )
    
    transitions = {}
    
    for state in data['transitions']:
        transitions[state] = {}
        for simbols in data['transitions'][state]:
            transitions[state][tuple(simbols.replace("(", "").replace(")", "").replace("'", "").split(","))] = data['transitions'][state][simbols]
    
    MT = TuringMachine((tapes[0], tapes[1],tapes[1]), data['states'], 
                       data['input_alphabet'], data['tape_alphabet'],
                       data['initial_state'], data['accept_states'],
                       transitions)
    
    result = MT.run()
    result = ''.join(result).strip("_")
    pres = result.replace("_", " ")
    print(f"Expresion resultante: {pres}")
    return result
    
if __name__ == '__main__':
    # n = 25
    # expression = "The quick brown fox jumps over the lazy dog"
     
    # res = cypher(n=n, expression=expression)
    # deres = decypher(n=n, expression=res)
    while True:
        print("--Maquina de Turing Cifrado y Descifrado Cesar--")
        print('''
--MENU--
1. Cifrar
2. Descifrar
3. Salir
''')
        option = input("Que desea realizar? \n")
        
        if option in ["1", "2"]:
            n = input("Ingrese el numero por el cual desea desplazar: \n")
            n = int(n) % 26
            if option == "1":
                exp = input("Ingrese la expresion a cifrar: \n")
                cypher(n, exp)
            if option == "2":
                exp = input("Ingrese la expresion a descifrar: \n")
                decypher(n, exp)
        elif option == "3":
            print("Adios")
            sys.exit()