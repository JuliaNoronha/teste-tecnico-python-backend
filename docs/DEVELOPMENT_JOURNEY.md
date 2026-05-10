# Desafios e soluções

## Desafios enfrentados:

### - Erro de atributo no SQLAlchemy:
#### Durante a criação do modelo, ocorreu um erro indicando que a tabela não possuía o atributo ```__tablename__```. Ao analisar o código, percebi que havia utilizado ```:``` em vez de ```=``` na atribuição. A correção reforçou a atenção necessária à sintaxe específica do SQLAlchemy.

###   - Conflito com o módulo Datetime: 
#### Tive uma dificuldade inicial com a importação do ```datetime```, resultando em um ```AttributeError```. Com o auxílio da IA, entendi a diferença entre importar o módulo e a classe específica, optando por ```from datetime import datetime``` para tornar o código mais limpo e funcional.

## Aprendizado com IA:
#### A IA foi fundamental não apenas na correção, mas para explicar a causa raiz dos erros. Isso transformou um momento de travamento em uma oportunidade de aprendizado sobre uma estrutura interna das bibliotecas Python.