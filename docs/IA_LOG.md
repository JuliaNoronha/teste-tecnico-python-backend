# Projeto acelerado com o auxílio do Gemini, no modo aprendizado guiado:

    A IA simulou um Pair Programming, teve uma função de instrutora, me ensinando conceitos que ainda não dominava, como o FastApi.

    Solicitei a divisão do trabalho em fases, desde a preparação do ambiente até a lógica "inteligente" do diagnóstico.
- [x] Configuração do Ambiente: Criar o ambiente virtual e instalar as dependências.
- [x] Definição do Modelo de Dados: Decidir como as informações serão estruturadas(Campos obrigatórios + extras).
- [x] Escolha do framework e Persistência
- [ ] Implementação do Endpoint POST: Criar a rota para receber e validar os daods de foco.
- [ ] Implementação do Endpoint GET: Criar a lógica de cálculo (média e soma) e o motor de feedback.
- [ ] Tratamento de erros: Garantir que a API não aceite ```nivel_foco``` inválido. 
- [ ] Documentação (README): Instruções de como rodar e testar.

    
    Framework escolhido: FastApi, pois é moderno, rápido e já gera documentação automática(Swagger). Havia outras duas opções, Flask também seria uma boa escolha
    e o Django, por ser mais completo, poderia deixar "pesado" para o desafio. 

    Utilizei o SQLite, para não ter perda de dados.