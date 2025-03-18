# Estruturas de Dados

Repositório criado para a disciplina de Estruturas de Dados I do curso de Ciência da Computação da UDF.

## Autores
- **Maurício Gabriel Gemmal Fonseca**
- **Paulo André Gemmal Fonseca**

## Descrição
Este repositório contém exemplos práticos de diferentes estruturas de dados, incluindo listas encadeadas, listas ordenadas e implementações de estruturas lineares como pilhas e filas.

## Problema Prático Escolhido

### Sistema de Gerenciamento de Tarefas com Prioridades usando Filas

**Problema:** Em um hospital movimentado, os pacientes precisam ser atendidos com base na gravidade de sua condição, e não na ordem de chegada. Pacientes críticos devem ser atendidos primeiro, enquanto aqueles com condições menos urgentes podem aguardar mais tempo. No entanto, dentro do mesmo nível de gravidade, os pacientes devem ser atendidos na ordem em que chegaram.

**Solução:** Implementamos um sistema de triagem hospitalar usando uma fila de prioridade. Cada paciente recebe um nome, idade, descrição do problema de saúde e um nível de gravidade (exemplo: Crítico, Grave, Moderado, Leve). Os pacientes são armazenados em filas separadas de acordo com seu nível de gravidade. Quando um médico solicita o próximo paciente para atendimento, o sistema retorna o primeiro paciente da fila com maior prioridade. 

A implementação completa deste problema pode ser encontrada no arquivo [tarefa_prioridade.py](tarefa_prioridade.py) deste repositório.

## Estrutura do Repositório

- **[Introdução](Introdução/)**: Conceitos básicos de estruturas de dados e sua importância
- **[Definição-Importância](Definição-Importância/)**: Impacto das estruturas de dados no desempenho de programas
- **[Conceitos-Fundamentais](Conceitos-Fundamentais/)**: Variáveis, tipos de dados e alocação de memória
- **[Estruturas-Lineares](Estruturas-Lineares/)**: Exemplos de listas, filas e pilhas

## Disciplina
Estruturas de Dados I - UDF
Professora: Kadidja Valeria Reginaldo de Oliveira
