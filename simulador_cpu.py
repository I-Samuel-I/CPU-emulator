memoria = [0] * 64
R = {'R0': 0, 'R1': 0, 'R2': 0}
PC = 0

def carregar_programa(caminho):
    with open(caminho) as f:
        return [linha.split('#')[0].strip() for linha in f if linha.strip() and not linha.strip().startswith('#')]

def executar(programa):
    global PC
    while PC < len(programa):
        instr = programa[PC].replace(',', '').split()
        if instr[0] == 'HLT': break
        elif instr[0] == 'LOAD':
            R[instr[1]] = int(instr[2]) if instr[2][0] != '[' else memoria[int(instr[2][1:-1])]
        elif instr[0] == 'STORE':
            memoria[int(instr[1][1:-1])] = R[instr[2]]
        elif instr[0] == 'ADD':
            R[instr[1]] += R[instr[2]]
        PC += 1

    print(f"R0={R['R0']} R1={R['R1']} R2={R['R2']} PC={PC}")
    print(f"Mem[30]={memoria[30]}")

programa = carregar_programa('test.txt')
executar(programa)