# Pilhas (Stacks)

## Introdução

Uma pilha é uma estrutura de dados linear baseada no princípio LIFO (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido. Um exemplo prático disso é uma pilha de pratos: o prato mais recentemente colocado no topo será o primeiro a ser retirado.

## Características

- **Princípio LIFO**: Último a entrar, primeiro a sair.
- **Acesso Restrito**: Inserção e remoção acontecem apenas no topo.
- **Operações Fundamentais**: `push` (inserir) e `pop` (remover).
- **Implementações**: Utilizando arrays ou listas encadeadas.

## Operações Fundamentais

### Push (Inserir)
- Adiciona um elemento ao topo da pilha.
- Em arrays, isso envolve incrementar o índice do topo.
- Em listas encadeadas, um novo nó é criado e apontado para o nó atual do topo.

### Pop (Remover)
- Retira o elemento do topo da pilha.
- Em arrays, o índice do topo é decrementado.
- Em listas encadeadas, o ponteiro do topo é movido para o próximo nó.

### Peek (Consultar o Topo)
- Retorna o elemento no topo sem removê-lo.
- Útil para verificar o próximo elemento a ser desempilhado.

### isEmpty (Verificar se Está Vazia)
- Retorna `true` se a pilha não contiver elementos.

### isFull (Verificar se Está Cheia)
- Aplicável apenas para implementações baseadas em arrays de tamanho fixo.

### Size (Obter o Tamanho)
- Retorna a quantidade de elementos presentes na pilha.

## Complexidade de Tempo

| Operação | Complexidade |
|----------|--------------|
| Push     | O(1)         |
| Pop      | O(1)         |
| Peek     | O(1)         |
| isEmpty  | O(1)         |
| isFull   | O(1)         |
| Size     | O(1)         |

## Métodos de Implementação

### Com Array
- **Vantagens**: Simplicidade e acesso rápido ao topo.
- **Desvantagens**: Tamanho fixo pode levar a estouro ou desperdício de espaço.
- **Otimização**: Monitorar um índice do topo para controle eficiente.

### Com Lista Encadeada
- **Vantagens**: Crescimento dinâmico sem limite fixo.
- **Desvantagens**: Consumo extra de memória devido aos ponteiros.
- **Eficiência**: Inserção e remoção ocorrem apenas no topo, otimizando o desempenho.

## Aplicações Práticas

- **Avaliação de Expressões**: Conversão de notação infixa para pós-fixa e cálculo de expressões pós-fixas.
- **Gerenciamento de Memória**: Utilização em call stacks de funções.
- **Histórico de Navegação**: Controle de páginas "Voltar" e "Avançar" em navegadores web.
- **Algoritmos de Backtracking**: Implementação da busca em profundidade (DFS) em grafos.
- **Verificação de Parênteses Balanceados**: Análise de expressões matemáticas e código-fonte.
- **Conversão de Bases Numéricas**: Mudança entre diferentes sistemas numéricos.
- **Implementação de Algoritmos**: Como o QuickSort, que usa pilhas para gerenciamento de chamadas recursivas.

## Caso de Uso: Histórico de Navegador

1. Quando o usuário acessa uma nova página, seu URL é armazenado na pilha.
2. Ao clicar em "Voltar", a pilha desempilha a página atual e retorna à anterior.
3. O botão "Avançar" usa outra pilha para restaurar as páginas previamente desempilhadas.

## Limitações

- **Acesso Restrito**: Não é possível acessar elementos intermediários diretamente.
- **Busca Ineficiente**: Exige desempilhamento até o elemento desejado.
- **Tamanho Fixo em Arrays**: Pode causar desperdício de memória ou estouro de pilha.

## Variações

### Pilha Dupla
- Utiliza um único array para gerenciar duas pilhas.

### Pilha com Mínimo/Máximo
- Armazena informações auxiliares para consulta rápida do menor/maior elemento.

### Pilha Circular
- Implementação que reaproveita espaço, permitindo um comportamento cíclico.

---

Por Mauricio Gabriel e Paulo André - UDF Ciência da Computação
