# Simulador Baseado em Agentes para Interações Estratégicas entre Países

Este repositório contém o código-fonte de um simulador computacional baseado em agentes,
desenvolvido em Python, voltado à modelagem simplificada de interações estratégicas entre países.

Cada país é representado como um agente autônomo com atributos internos (influência, militar,
estabilidade, economia e HP) e relações contextuais (tensão e afinidade). As ações possíveis são:

- Atacar
- Negociar
- Dialogar
- Passar o turno

As probabilidades de sucesso são calculadas por uma função logística, com uso de aleatoriedade
para representar incertezas naturais do sistema.

------------------------------------------------------------

## Requisitos

- Python 3.8 ou superior

- Não usa bibliotecas externas (apenas random e math)

------------------------------------------------------------

## Como executar

Clone este repositório:

git clone https://github.com/GabrieliOlvz/RPG.git

cd RPG

Execute o simulador:

python rpg.py

Siga as instruções exibidas no terminal para escolher seu país e realizar ações a cada turno.

------------------------------------------------------------

## Países incluídos

Brasil, Estados Unidos, China, Alemanha, Índia, Japão, Reino Unido, França, Itália, Canadá,
Coreia do Sul, Rússia, México, Espanha e Austrália.

------------------------------------------------------------

## Encerramento da simulação

A simulação termina quando:

- O jogador é eliminado;
- Resta apenas um país vivo;
- Ou o limite máximo de turnos é atingido.

https://youtu.be/2gVGLmdznLA
link do vídeop com explicação do código.
