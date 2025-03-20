# Listas

## Definição

Uma lista é uma estrutura de dados linear que armazena uma coleção ordenada de elementos. Cada elemento possui uma posição específica, determinada pelo seu índice. O tipo de elementos suportados depende da implementação e da linguagem de programação utilizada.

## Tipos de Listas

### 1. Lista Sequencial (Array)
- **Implementação**: Elementos armazenados de forma contígua na memória.
- **Acesso**: Direto por índice (O(1)).
- **Característica**: Tamanho geralmente fixo ou redimensionado conforme necessário.

### 2. Lista Ligada (Linked List)
- **Implementação**: Elementos armazenados em posições dispersas na memória, conectados por referências (ponteiros).
- **Tipos**:
  - **Lista Simplesmente Ligada**: Cada nó aponta apenas para o próximo.
  - **Lista Duplamente Ligada**: Cada nó contém referências para o próximo e o anterior.
  - **Lista Circular**: O último nó aponta para o primeiro.
- **Acesso**: Sequencial, iniciando pela cabeça da lista (O(n)).
- **Característica**: Tamanho dinâmico, facilitando inserção e remoção de elementos.

## Operações Básicas

### 1. Inserção
- **No início**: Adiciona um elemento na primeira posição.
- **No final**: Adiciona um elemento na última posição.
- **Em posição arbitrária**: Insere um elemento em um índice específico.

### 2. Remoção
- **Do início**: Remove o primeiro elemento.
- **Do final**: Remove o último elemento.
- **De posição arbitrária**: Remove um elemento em um índice específico.

### 3. Acesso
- **Por índice**: Obtém o elemento em uma posição específica.
- **Sequencial**: Percorre a lista do início ao fim.

### 4. Busca
- **Por valor**: Localiza a posição de um elemento específico.
- **Por condição**: Filtra elementos que atendem a uma condição específica.

### 5. Atualização
- **Por índice**: Modifica o valor de um elemento em determinada posição.

## Complexidade de Tempo

### Lista Sequencial (Array)
| Operação | Complexidade |
|----------|--------------|
| Acesso | O(1) |
| Inserção no início | O(n) |
| Inserção no final | O(1)* |
| Inserção em posição arbitrária | O(n) |
| Remoção do início | O(n) |
| Remoção do final | O(1) |
| Remoção de posição arbitrária | O(n) |
| Busca | O(n) |

*Se houver espaço disponível. Caso contrário, O(n) devido ao realocamento.

### Lista Ligada
| Operação | Lista Simples | Lista Duplamente Ligada |
|----------|----------------|------------------------|
| Acesso | O(n) | O(n) |
| Inserção no início | O(1) | O(1) |
| Inserção no final | O(n)* | O(1)* |
| Inserção em posição arbitrária | O(n) | O(n) |
| Remoção do início | O(1) | O(1) |
| Remoção do final | O(n) | O(1) |
| Remoção de posição arbitrária | O(n) | O(n) |
| Busca | O(n) | O(n) |

*Se a referência para o final da lista for mantida, a inserção no final pode ser O(1).

## Vantagens e Desvantagens

### Listas Sequenciais (Arrays)
**Vantagens**:
- Acesso direto aos elementos por índice.
- Melhor aproveitamento da memória cache devido à localidade espacial.
- Implementação simples.

**Desvantagens**:
- Tamanho fixo ou necessidade de realocação.
- Inserção e remoção custosas devido ao deslocamento de elementos.
- Possível desperdício de memória.

### Listas Ligadas
**Vantagens**:
- Tamanho dinâmico.
- Inserções e remoções eficientes no início e no final (para listas duplamente ligadas).
- Melhor aproveitamento de memória sem desperdício de espaços contíguos.

**Desvantagens**:
- Acesso sequencial aos elementos.
- Maior consumo de memória devido às referências adicionais.
- Menor eficiência no uso da memória cache.

## Aplicações Comuns

1. **Implementação de Estruturas**: Pilhas, filas, deques, etc.
2. **Manipulação de Dados Dinâmicos**: Quando o tamanho dos dados pode mudar frequentemente.
3. **Algoritmos de Ordenação e Busca**.
4. **Gerenciamento de Memória**: Controle de blocos livres e alocados.
5. **Histórico de Navegação**: Em navegadores da web.
6. **Listas de Reprodução**: Em aplicativos de mídia.

---

Por Mauricio Gabriel e Paulo André - UDF Ciência da Computação
