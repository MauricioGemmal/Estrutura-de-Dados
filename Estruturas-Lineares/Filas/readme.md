```markdown
# Filas (Queues)

## Conceito

Uma fila é uma estrutura de dados linear baseada no princípio FIFO (First In, First Out), onde o primeiro elemento inserido é também o primeiro a ser removido. Um exemplo prático é uma fila de banco: a primeira pessoa a entrar é a primeira a ser atendida.

## Características

- **Princípio FIFO**: Primeiro a entrar, primeiro a sair.
- **Acesso Restrito**: Inserção no final (traseira) e remoção do início (frente).
- **Operações Fundamentais**: `enqueue` (inserção) e `dequeue` (remoção).
- **Formas de Implementação**: Utilizando arrays ou listas encadeadas.

## Operações Essenciais

### Enqueue (Inserir)
- Adiciona um elemento ao final da fila.
- Em arrays, isso envolve incrementar o índice da traseira.
- Em listas encadeadas, é criado um novo nó apontado pelo último nó atual.

### Dequeue (Remover)
- Retira o elemento do início da fila.
- Em arrays, o índice da frente é incrementado.
- Em listas encadeadas, a referência da frente é movida para o próximo nó.

### Front/Peek (Espiar o Primeiro Elemento)
- Obtém o primeiro elemento sem removê-lo.
- Útil para visualizar a próxima remoção.

### isEmpty (Verificar se Está Vazia)
- Retorna `true` se a fila não contiver elementos.

### isFull (Verificar se Está Cheia)
- Aplicável a arrays de tamanho fixo, onde não há espaço para novos elementos.

### Size (Obter Tamanho)
- Retorna a quantidade de elementos presentes na fila.

## Complexidade de Tempo

| Operação   | Complexidade |
|------------|--------------|
| Enqueue    | O(1)         |
| Dequeue    | O(1)         |
| Front/Peek | O(1)         |
| isEmpty    | O(1)         |
| isFull     | O(1)         |
| Size       | O(1)         |

## Implementações

### Com Array
- **Vantagens**: Simples e acesso rápido.
- **Desvantagens**: Tamanho fixo, desperdício de espaço.
- **Otimização**: Uso de fila circular para reutilização eficiente do espaço.

### Com Lista Encadeada
- **Vantagens**: Crescimento dinâmico.
- **Desvantagens**: Maior uso de memória para referências.
- **Eficiência**: Manter ponteiros para frente e traseira melhora o desempenho.

### Fila Circular
- **Vantagens**: Melhor aproveitamento de espaço.
- **Desvantagens**: Lógica mais complexa.
- **Implementação**: Uso de aritmética modular para circularidade.

## Aplicações

- **Escalonamento de Processos**: Sistemas operacionais utilizam filas para gerenciar tarefas.
- **Filas de Impressão**: Organização de documentos para impressão.
- **Buffers de Transferência de Dados**: Controle do fluxo de informações.
- **Algoritmos de Busca em Largura (BFS)**: Exploração sistemática de grafos.
- **Gestão de Atendimento ao Cliente**: Controle de chamadas e suporte.
- **Cache de Dados**: Implementação de estratégias como LRU (Least Recently Used).
- **Simulação de Eventos Discretos**: Modelagem computacional baseada em eventos.
- **Sistemas de Mensageria**: Comunicação em filas como Kafka e RabbitMQ.

## Exemplo: Sistema de Atendimento

Em um sistema de suporte ao cliente:

1. Os clientes entram na fila conforme sua chegada.
2. O próximo atendimento é sempre para o cliente que esperou mais tempo.
3. Novos clientes são adicionados ao final da fila.

## Variações de Filas

### Fila de Prioridade
- Elementos possuem prioridades diferentes.
- O elemento de maior prioridade sai primeiro, independentemente da ordem de inserção.
- Frequentemente implementada com heaps.

### Deque (Fila de Duas Pontas)
- Permite inserções e remoções tanto no início quanto no final.
- Combina características de pilhas e filas.

### Fila Circular
- Utiliza um array onde o final retorna ao início.
- Evita deslocamentos após remoções.

### Fila Bloqueante
- Utilizada em computação concorrente.
- As operações podem ser bloqueadas caso a fila esteja cheia ou vazia.

## Limitações das Filas

- **Acesso Restrito**: Elementos do meio não podem ser acessados diretamente.
- **Busca Ineficiente**: Pode exigir a remoção de vários elementos.
- **Tamanho Fixo em Arrays**: Pode levar a estouro de memória ou desperdício de espaço.

---

Por Mauricio Gabriel e Paulo André - UDF Ciência da Computação
```

