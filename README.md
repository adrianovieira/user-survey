# User Survey

> Desafio Data Science

## Objetivo

Esta aplicação tem como alvo mostrar a **evolução temporal da taxa de conversão**.

Tem como desafio principal a otimização de consulta aos dados,
garantindo um tempo de resposta rápido e eficiente para a aplicação,
mesmo com o grande volume de informações.

### Tecnologias permitidas

- **Backend**: Node.js, Golang.
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
