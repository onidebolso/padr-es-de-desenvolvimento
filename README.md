# Padrões de Desenvolvimento - Strategy

Projeto acadêmico de Engenharia de Software II para demonstrar o padrão de projeto Strategy.

Este repositório mostra duas abordagens para o mesmo problema: calcular o total de uma compra com desconto.

## Objetivo

Explicar, de forma didática, como a solução fica:

1. sem padrão, usando `if/elif` para decidir o desconto;
2. com Strategy, separando cada regra de desconto em uma classe própria.

## Cenário escolhido

O sistema simula um checkout simples com três perfis de cliente:

- cliente comum: sem desconto;
- cliente recorrente: 10% de desconto;
- cliente premium: 20% de desconto.

Esse cenário é bom para Strategy porque as regras podem mudar com facilidade. Quando a lógica cresce, a versão sem padrão tende a ficar cheia de condicionais. Com Strategy, cada regra fica isolada e o contexto apenas delega o cálculo.

## Estrutura do projeto

- [main.py](main.py): executa as duas demonstrações;
- [strategy_demo/sem_strategy.py](strategy_demo/sem_strategy.py): solução sem padrão;
- [strategy_demo/strategy.py](strategy_demo/strategy.py): solução com Strategy;
- [strategy_demo/models.py](strategy_demo/models.py): modelos compartilhados.

## Como executar

Use Python 3.10 ou superior.

```bash
python main.py
```

## O que o código demonstra

### Sem Strategy

A função de checkout contém as regras diretamente. Isso funciona, mas mistura decisão de negócio com processamento.

### Com Strategy

Cada regra de desconto implementa a mesma interface. O checkout recebe a estratégia e calcula o valor sem precisar saber qual regra está sendo usada.

## Pontos fortes

- reduz condicionais espalhadas pela aplicação;
- facilita incluir novos tipos de desconto;
- melhora organização e legibilidade;
- permite trocar a regra em tempo de execução.

## Pontos fracos

- cria mais classes e arquivos;
- pode parecer exagero para problemas muito simples;
- exige um pouco mais de abstração inicial.

## Conclusão

Strategy é útil quando existem várias formas de executar uma mesma operação e essas variações podem mudar ao longo do tempo. Neste projeto, o padrão deixa o cálculo de desconto mais modular, extensível e fácil de apresentar em comparação com a solução baseada em condicionais.

## Roteiro sugerido para a apresentação

1. Mostrar o problema e o cenário escolhido.
2. Apresentar a solução sem padrão.
3. Mostrar as limitações da solução sem padrão.
4. Explicar o Strategy.
5. Demonstrar a solução com Strategy.
6. Fechar com pontos fortes, fracos e conclusão.