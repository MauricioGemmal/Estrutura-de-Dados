# Estruturas de Dados: Definição e Importância

## Estruturas Lineares vs. Não Lineares

### Estruturas Lineares
Nas estruturas de dados lineares, os elementos são organizados de forma sequencial, onde cada elemento (exceto o primeiro e o último) possui um predecessor e um sucessor.

#### Exemplos:
- **Listas**: Coleção ordenada de elementos homogêneos.
- **Pilhas**: Estrutura LIFO (*Last In, First Out*), onde o último elemento adicionado é o primeiro a ser removido.
- **Filas**: Estrutura FIFO (*First In, First Out*), onde o primeiro elemento adicionado é o primeiro a ser removido.
- **Arrays**: Coleção indexada de elementos do mesmo tipo.
- **Listas Ligadas**: Estrutura composta por nós interligados, onde cada nó contém um valor e uma referência para o próximo.

### Estruturas Não Lineares
Nessas estruturas, os elementos são organizados de maneira não sequencial, permitindo conexões múltiplas entre elementos.

#### Exemplos:
- **Árvores**: Estruturas hierárquicas formadas por nós, sendo o primeiro o nó raiz.
  - *Árvores Binárias*: Cada nó pode ter até dois filhos.
  - *Árvores AVL*: Variante balanceada das árvores binárias de busca.
  - *Árvores B*: Estruturas balanceadas amplamente usadas em bancos de dados.

- **Grafos**: Conjunto de vértices (nós) conectados por arestas.
  - *Grafos Direcionados*: As arestas possuem uma direção definida.
  - *Grafos Não Direcionados*: As arestas não possuem direção fixa.

- **Tabelas Hash**: Estrutura que associa chaves a valores utilizando funções hash.

## Impacto das Estruturas de Dados no Desempenho
A escolha da estrutura correta influencia diretamente a eficiência de um programa.

### 1. Complexidade Temporal
A eficiência das operações é expressa usando a notação Big O, representando o tempo de execução relativo ao tamanho da entrada.

| Estrutura de Dados         | Acesso | Busca  | Inserção | Remoção |
|---------------------------|--------|--------|---------|---------|
| **Array**                 | O(1)   | O(n)   | O(n)    | O(n)    |
| **Lista Ligada**          | O(n)   | O(n)   | O(1)    | O(1)    |
| **Pilha**                 | O(n)   | O(n)   | O(1)    | O(1)    |
| **Fila**                  | O(n)   | O(n)   | O(1)    | O(1)    |
| **Tabela Hash**           | N/A    | O(1)*  | O(1)*   | O(1)*   |
| **Árvore Binária**        | O(n)   | O(n)   | O(n)    | O(n)    |
| **Árvore Binária de Busca** | O(n)   | O(n)   | O(n)    | O(n)    |
| **Árvore AVL**            | O(log n) | O(log n) | O(log n) | O(log n) |

*Nota: No pior caso, a tabela hash pode ter complexidade O(n) devido a colisões.*

### 2. Complexidade Espacial
A alocação de memória também deve ser considerada:
- **Arrays** são eficientes, mas podem desperdiçar espaço se houver posições não utilizadas.
- **Listas Ligadas** possuem sobrecarga devido às referências adicionais.
- **Tabelas Hash** consomem mais memória para minimizar colisões.

### 3. Facilidade de Implementação
Estruturas simples, como arrays, são mais fáceis de implementar, enquanto árvores AVL exigem maior complexidade algorítmica.

### 4. Adaptabilidade
- **Listas Ligadas** são vantajosas quando há inserções e remoções frequentes.
- **Árvores Balanceadas** mantêm eficiência mesmo com alterações constantes nos dados.

### 5. Casos de Uso
Cada estrutura se adequa a diferentes cenários:
- **Pilhas** são úteis para controle de chamadas de função e análise de expressões matemáticas.
- **Filas de Prioridade** otimizam escalonamento de tarefas.
- **Tabelas Hash** são ideais para buscas rápidas, como em dicionários e conjuntos.

A escolha correta da estrutura de dados pode determinar se um programa será executado em milissegundos ou em horas.

---

Por **Mauricio Gabriel e Paulo André** - *UDF Ciência da Computação*
