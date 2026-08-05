# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST funcional com FastAPI, aplicando conceitos de rotas, métodos HTTP, modelos de dados com Pydantic e tratamento de erros.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Service

#### Descrição
Configure uma aplicação FastAPI e implemente endpoints iniciais para validar que o serviço está funcionando.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI` em um arquivo Python
- Implementar `GET /` retornando uma mensagem simples de boas-vindas
- Implementar `GET /health` retornando um status de saúde da API (por exemplo: `{ "status": "ok" }`)


### 🛠️ Build CRUD Endpoints for Items

#### Descrição
Implemente endpoints para criar, listar, buscar, atualizar e remover itens usando uma estrutura em memória.

#### Requisitos
O programa completo deve:

- Definir modelos Pydantic para entrada e saída dos itens
- Implementar os endpoints: `POST /items`, `GET /items`, `GET /items/{item_id}`, `PUT /items/{item_id}`, `DELETE /items/{item_id}`
- Retornar `404` quando um item não for encontrado
- Garantir que cada item tenha um identificador único


### 🛠️ Add Validation and Better API Responses

#### Descrição
Aprimore a API com validações, filtros por query params e respostas HTTP apropriadas.

#### Requisitos
O programa completo deve:

- Validar campos obrigatórios (exemplo: `name` não vazio e `price` maior que zero)
- Permitir filtro por nome usando query param em `GET /items` (exemplo: `?name=book`)
- Retornar códigos HTTP corretos para sucesso, criação e remoção (como `200`, `201` e `204`)
