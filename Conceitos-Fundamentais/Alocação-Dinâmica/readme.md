# Alocacao Dinamica de Memoria

## O que e?

A alocacao dinamica de memoria e um processo no qual um programa requisita memoria ao sistema operacional durante sua execucao, conforme necessario. Diferente da alocacao estatica, onde o espaco de memoria e definido durante a compilacao, a alocacao dinamica permite que o programa obtenha e libere memoria de forma flexivel ao longo de sua execucao.

## Principais Caracteristicas

- **Tempo de Alocacao**: Acontece durante a execucao do programa.
- **Tamanho**: Adaptavel, podendo aumentar ou diminuir conforme as necessidades.
- **Tempo de Vida**: Definido pelo programador; a memoria permanece alocada ate ser liberada manualmente ou ate o encerramento do programa.
- **Localizacao**: Utiliza a regiao da memoria chamada *heap* (monte).
- **Flexibilidade**: Permite a criacao de estruturas dinamicas que podem se ajustar as demandas do programa.

## Mecanismos de Alocacao Dinamica em Diferentes Linguagens

A alocacao dinamica pode ser realizada por diferentes mecanismos, dependendo da linguagem de programacao utilizada:

- **C/C++**: Funcoes `malloc()`, `calloc()`, `realloc()` e os operadores `new` e `delete`.
- **Java**: Utiliza o operador `new`, com gerenciamento automatico de memoria via *garbage collector*.
- **Python**: Alocacao automatica e gerenciamento interno pelo interpretador.
- **JavaScript**: O motor da linguagem gerencia a alocacao e desalocacao automaticamente.

## Vantagens da Alocacao Dinamica

- **Uso eficiente de memoria**: Permite alocar apenas o necessario, evitando desperdicio.
- **Flexibilidade**: Facilita a manipulacao de dados de tamanho variavel.
- **Adaptacao ao crescimento dos dados**: Estruturas de dados podem expandir ou reduzir dinamicamente.
- **Implementacao de estruturas complexas**: Essencial para listas encadeadas, arvores, grafos e outras estruturas dinamicas.

## Desvantagens e Desafios

- **Sobrecarga de processamento**: O gerenciamento de alocacao e desalocacao consome recursos.
- **Fragmentacao de memoria**: Pode reduzir a eficiencia do uso da memoria.
- **Risco de vazamentos de memoria**: Em linguagens que exigem liberacao manual, falhas nesse processo podem acumular memoria inutilizada.
- **Complexidade adicional**: O programador precisa gerenciar corretamente a memoria para evitar erros.

## Quando Utilizar a Alocacao Dinamica?

- **Tamanho de dados desconhecido em tempo de compilacao**.
- **Estruturas de dados que podem crescer ou reduzir durante a execucao**.
- **Otimizacao de recursos em sistemas com memoria limitada**.
- **Dados com tempo de vida variavel ao longo do programa**.

## Exemplos de Estruturas de Dados Dinamicas

1. **Listas encadeadas**: Nos alocados conforme necessario.
2. **Arvores**: Nos adicionados a medida que a estrutura cresce.
3. **Grafos**: Alocacao dinamica de vertices e arestas.
4. **Vetores dinamicos** (*std::vector* em C++ e *ArrayList* em Java).
5. **Tabelas hash**: Buckets ajustados dinamicamente.

## Gerenciamento de Memoria

- **Em linguagens com alocacao manual**: O programador deve liberar a memoria explicitamente para evitar *memory leaks*.
- **Em linguagens com *garbage collection***: O sistema identifica e libera automaticamente a memoria nao utilizada, reduzindo o risco de vazamentos, mas com impacto no desempenho.

---

📌 **Autores**: Mauricio Gabriel e Paulo Andre – UDF Ciencia da Computacao.
