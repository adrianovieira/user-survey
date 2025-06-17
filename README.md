# User Survey

> Desafio Data Science

[![pipeline status](https://gitlab.com/adrianovieira/isurvey-backend/badges/main/pipeline.svg)](https://gitlab.com/adrianovieira/isurvey-backend/-/pipelines)
[![coverage iSurveys Status v1.0](https://gitlab.com/adrianovieira/isurvey-backend/badges/surveys-1.2/coverage.svg?job=job::integration::tests::v1.0&key_text=iSurveys+Status+v1.0&key_width=130)](https://gitlab.com/adrianovieira/isurvey-backend/-/commits/main)
[![coverage iSurveys Status v1.2](https://gitlab.com/adrianovieira/isurvey-backend/badges/surveys-1.2/coverage.svg?job=job::integration::tests::v1.2&key_text=iSurveys+Status+v1.2&key_width=130)](https://gitlab.com/adrianovieira/isurvey-backend/-/commits/main)

## Objetivo

Esta aplicação tem como alvo mostrar a **evolução temporal da taxa de conversão**.

Tem como desafio principal a otimização de consulta aos dados,
garantindo um tempo de resposta rápido e eficiente para a aplicação,
mesmo com o grande volume de informações.

### Tecnologias permitidas

- **Backend**: Node.js, Python, Golang e :woman_technologist: :man_technologist:
- **Frontend**: React.
- **Banco de Dados**: PostgreSQL.
- **Conteinerização**: Docker.

## Documentação

Detalhamento do processo de desenvolvimento, incluindo as escolhas feitas em termos de
arquitetura, otimização de performance e trade-offs.

### Artefatos

Documentação de Arquitetura, Desenho da Solução e especificação OpenAPI-3 podem ser
acessados aqui no diretório [**_docs_**](./docs) deste repositório.

- Arquitetura da Solução ([`ArquiteturaSolucao.adoc`](./docs/ArquiteturaSolucao.adoc))
- Desenho da Solução ([`DesenhoSolucao.adoc`](./docs/DesenhoSolucao.adoc))
- OpenAPI-3 ([`openapi.json`](./docs/user_survery/openapi.json))

## Requisitos

- **API**: Rota que retorna a evolução no tempo da taxa de conversão.
- **Contêinerização**: A aplicação será conteinerizada sob Docker.

### Requisitos Adicionais

- **Front-end**: Implementar dashboard dos dados retornados.
- **Testes Automatizados**: Criar testes automatizados para garantir a qualidade e confiabilidade do código.
- **Filtros Adicionais**: Permitir que o usuário aplique filtros adicionais no dashboard.

## Operação

:woman_lifting_weights: :man_lifting_weights:

### Local :woman_surfing: :man_surfing:

Você pode executar esta aplicação localmente! :smiling_face_with_halo: :raising_hands:

:see_no_evil_monkey: :hear_no_evil_monkey: :speak_no_evil_monkey:

Execute estes passos abaixo: :ninja: :man_teacher: :penguin:

1.  Use o `docker-compose.yml` deste projeto para inicializar o _backend_ e o banco de dados.  
    O banco vai ser inicializado com uns poucos dados de exemplo. :raising_hands:

    ```shell
    docker compose up -d
    ```

    Acesse a API no endereço http://api.isurvey.localhost (magia :man_technologist: proxy reverso)  
    usando os endpoints descritos na documentação [_OpenAPI_](./docs/user_survery/openapi.json).

2.  Para usar a aplicação web e acesse usando http://web.isurvey.localhost (magia :man_technologist: proxy reverso).  
    Será baixada a mais recente release da imagem.

    - inicializar o serviço

      ```shell
      docker compose up -d web
      ```

    :woman_technologist: :man_technologist: :heart_hands:
    aí na sua máquina.

3.  Remover o serviço

    ```shell
    docker compose down web  # para remover o web
    docker compose down -v   # remove os demais serviços
    ```

:woman_dancing: :man_dancing: :hundred_points: :person_biking: :person_mountain_biking: :doughnut: :custard: :beer_mug: :cut_of_meat: :wine_glass: :cheese_wedge: :pizza: :hot_beverage: :cheese_wedge:
