# Simulador de CPU Simplificada em Python

> Status: Em desenvolvimento

- Python 🐍

---

## Visão Geral

Este projeto simula uma CPU simplificada com:

- Registradores: `R0`, `R1`, `R2`
- Memória de 64 posições
- Contador de Programa (`PC`)

O simulador executa instruções básicas para manipular registradores e memória, demonstrando o ciclo fetch-decode-execute de uma CPU.

---

## Instruções Suportadas

- `LOAD Rx, valor`  
  Carrega um valor imediato no registrador `Rx`.  
  Exemplo: `LOAD R0, 5`

- `LOAD Rx, [endereço]`  
  Carrega o conteúdo da memória no endereço indicado para o registrador `Rx`.  
  Exemplo: `LOAD R1, [10]`

- `STORE [endereço], Rx`  
  Armazena o conteúdo do registrador `Rx` na memória no endereço indicado.  
  Exemplo: `STORE [30], R0`

- `ADD Rx, Ry`  
  Soma o conteúdo dos registradores `Rx` e `Ry` e armazena o resultado em `Rx`.  
  Exemplo: `ADD R0, R1`

- `HLT`  
  Finaliza a execução do programa.

---

## Formato do Arquivo de Programa

Cada linha do arquivo contém uma instrução válida. Comentários podem ser adicionados após o caractere `#`.  

Exemplo de programa válido (`test.txt`):

```txt
LOAD R0, 5          # Carrega 5 em R0
LOAD R1, 12         # Carrega 12 em R1
ADD R0, R1          # Soma R0 e R1, resultado em R0
STORE [30], R0      # Armazena R0 na memória endereço 30
LOAD R2, [30]       # Carrega da memória endereço 30 em R2
HLT                 # Finaliza o programa
