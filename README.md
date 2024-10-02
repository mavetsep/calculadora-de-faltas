# Calculadora de Faltas

o projeto é uma calculadora de faltas que ajuda você a descobrir quantas aulas pode faltar e ainda ser aprovado. ele usa a carga horária do curso para fazer os cálculos.

## Como Funciona

a calculadora determina quantas aulas você pode faltar da seguinte maneira:

1. **Total de Aulas**: Primeiro, ela calcula quantas aulas existem no seu curso. (considera que cada aula tem 45 minutos) 
   - ex: se seu curso tem 60 horas, isso significa que você terá um total de 80 aulas.

2. **Frequência Mínima**: Para passar, você precisa frequentar pelo menos 75% das aulas. 
   - ex: se você tem 80 aulas no total, precisará frequentar 60 aulas para ser aprovado.

3. **Faltas Permitidas**: agora, a calculadora descobre quantas faltas você pode ter. isso é feito subtraindo o número de aulas que você precisa frequentar do total de aulas.
   - ex: se você tem 80 aulas e precisa frequentar 60, você pode faltar até 20 aulas sem ser reprovado.

então se o seu curso tem 60 horas, você pode faltar até 20 aulas e ainda ser aprovado.

## Pré-requisitos

para rodar, você precisa ter o python instalado no seu computador, e as seguintes bibliotecas devem ser instaladas:

```bash
pip install tkinter pygame pillow
