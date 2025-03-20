# Alocação Estática de Memória

## Definição

A alocação estática de memória refere-se à reserva de espaço para variáveis e estruturas de dados durante a compilação, antes da execução do programa. O tamanho e a duração dessas variáveis são determinados no momento da compilação e permanecem constantes ao longo da execução.

## Características

- **Tempo de Alocação**: Definido em tempo de compilação.
- **Tamanho**: Fixo e imutável durante a execução.
- **Tempo de Vida**: Depende do escopo da variável:
  - Variáveis globais: Existem durante toda a execução.
  - Variáveis locais: Persistem enquanto o bloco onde foram declaradas estiver ativo.
- **Localização**: Normalmente armazenadas na pilha ou na seção de dados do programa.
- **Flexibilidade**: Baixa, pois o tamanho não pode ser alterado dinamicamente.

## Tipos de Variáveis com Alocação Estática

- **Variáveis Globais**: Definidas fora de funções, mantêm-se ativas durante toda a execução.
- **Variáveis Locais Estáticas**: Declaradas com `static` dentro de funções, preservam seu valor entre chamadas.
- **Arrays de Tamanho Fixo**: Definidos com um tamanho constante em tempo de compilação.
- **Estruturas de Dados Estáticas**: Structs e classes cujos campos possuem tamanhos fixos.

## Vantagens

1. **Desempenho**: Acesso rápido, pois os endereços de memória são conhecidos em tempo de compilação.
2. **Segurança**: Reduz riscos de vazamentos de memória.
3. **Previsibilidade**: Favorece sistemas embarcados e aplicações críticas.
4. **Eficiência**: Evita a sobrecarga de alocação/desalocação dinâmica.

## Desvantagens

1. **Inflexibilidade**: Não permite redimensionamento em tempo de execução.
2. **Uso Ineficiente da Memória**: Pode alocar mais espaço do que o necessário.
3. **Limitações**: Não é ideal para casos onde o tamanho dos dados é desconhecido antecipadamente.

## Aplicações Ideais

1. **Dados com Tamanho Fixo**: Quando não há necessidade de redimensionamento.
2. **Sistemas Embarcados**: Onde a previsibilidade de recursos é essencial.
3. **Aplicações de Tempo Real**: Que exigem respostas consistentes.
4. **Pequenas Estruturas**: Quando a alocação dinâmica não traz benefícios significativos.

## Exemplo Prático

Em um sistema de processamento de transações bancárias:
- Um array estático pode armazenar as 100 transações mais recentes, caso apenas esse limite de dados seja necessário.
- Registros de clientes podem ser estruturados com campos fixos (nome, endereço, etc.), utilizando memória alocada estaticamente.

---
**Autores:** Mauricio Gabriel e Paulo André - UDF Ciência da Computação
