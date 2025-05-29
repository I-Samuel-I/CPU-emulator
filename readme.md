## Simulador de CPU Simplificada em Python

Visão Geral
Este projeto simula uma CPU básica com registradores, memória e um contador de programa (PC). Ele demonstra o ciclo fundamental de uma CPU: buscar instrução, decodificar e executar.

Instruções Suportadas

LOAD Rx, valor ou LOAD Rx, [endereço]: carrega um valor imediato ou o conteúdo da memória no registrador Rx.

STORE [endereço], Rx: armazena o valor do registrador Rx no endereço de memória especificado.

ADD Rx, Ry: soma os valores dos registradores Rx e Ry, e armazena o resultado em Rx.

HLT: termina a execução do programa.

Formato do Arquivo de Programa
Cada linha contém uma instrução. Comentários podem ser adicionados usando o caractere #, tudo após ele será ignorado.
Exemplo:
LOAD R0, 5
LOAD R1, 12
ADD R0, R1
STORE [30], R0
LOAD R2, [30]
HLT

Como Executar

Crie um arquivo texto (.txt) contendo seu programa com as instruções acima.

No script Python, ajuste o nome do arquivo para o arquivo criado.

Execute o script Python. A CPU simulará a execução e mostrará o estado dos registradores e da memória.

O que é exibido
Após cada instrução, o simulador mostra o conteúdo dos registradores R0, R1, R2 e do PC, além de posições relevantes da memória.

