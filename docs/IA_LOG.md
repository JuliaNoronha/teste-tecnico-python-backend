# Projeto acelerado com o auxílio do Gemini, no modo aprendizado guiado:

    A IA simulou um Pair Programming, teve uma função de instrutora, me ensinando conceitos que ainda não dominava, como o FastApi.

    Solicitei a divisão do trabalho em fases, desde a preparação do ambiente até a lógica "inteligente" do diagnóstico.
- [x] Configuração do Ambiente: Criar o ambiente virtual e instalar as dependências.
- [x] Definição do Modelo de Dados: Decidir como as informações serão estruturadas(Campos obrigatórios + extras).
- [x] Escolha do framework e Persistência
- [x] Implementação do Endpoint POST: Criar a rota para receber e validar os daods de foco.
- [x] Implementação do Endpoint GET: Criar a lógica de cálculo (média e soma) e o motor de feedback.
- [x] Tratamento de erros: Garantir que a API não aceite ```nivel_foco``` inválido. 
- [x] Documentação (README): Instruções de como rodar e testar.

    
Framework escolhido: FastApi, pois é moderno, rápido e já gera documentação automática(Swagger). Havia outras duas opções, Flask também seria uma boa escolha
    e o Django, por ser mais completo, poderia deixar "pesado" para o desafio. 

Utilizei o SQLite, para não ter perda de dados.

# 🤖 AI Usage Log

## Registro de Uso de Inteligência Artificial

| Etapa | Descrição do auxílio da IA | Minha escolha                                                                                                      |
|---|---|--------------------------------------------------------------------------------------------------------------------|
| Arquitetura | Sugestão de divisão de arquivos (`models`, `schemas`, `database`, `routers`). | Estrutura adotada para manter o projeto organizado e alinhado com padrões utilizados em APIs REST profissionais.   |
| Modelagem | Geração inicial da entidade SQLAlchemy e definição dos campos principais. | Ajustei manualmente imports, tipagens e nome da tabela para manter consistência no projeto.                        |
| Validação | Sugestão do uso de `Field` do Pydantic para validar o range de `nivel_foco` entre 1 e 5. | Mantive a validação automática e complementei com mensagens de erro mais amigáveis nos endpoints.                  |
| Banco de Dados | Auxílio na configuração do SQLite e criação da dependência `get_db`. | Revisei manualmente o ciclo de abertura e fechamento das sessões para evitar vazamento de conexão.                 |
| Endpoints | Estrutura inicial dos endpoints `POST /registro-foco` e `GET /diagnostico-produtividade`. | Adaptei os retornos JSON e padronizei os status HTTP da aplicação.                                                 |
| Diagnóstico Inteligente | Sugestões de mensagens automáticas baseadas na média de foco do usuário. | Refinei as mensagens para deixá-las mais naturais e úteis para o usuário final.                                    |
| Tratamento de Erros | Sugestão de handlers globais para exceções HTTP e validações. | Ajustei os retornos para seguir um padrão consistente de respostas da API.                                         |
| README | Estrutura inicial da documentação do projeto. | Reescrevi a documentação como um guia de instalação com os passos para o ```uvicorn``` e o ```requirements.txt```. |

## Considerações Finais

A Inteligência Artificial foi utilizada como ferramenta de apoio para acelerar tarefas repetitivas, pesquisa de boas práticas e estruturação inicial do projeto.

Todas as decisões arquiteturais, validações finais, adaptações de código e regras de negócio foram revisadas e ajustadas manualmente durante o desenvolvimento.

