# Sistema de Gestão para Rede de Cinemas 🎬🍿

Um sistema de informação desenvolvido para centralizar e organizar os dados de uma rede de cinemas. Este projeto foi criado como atividade prática para a disciplina de Engenharia de Software, com foco na aplicação de conceitos de modelagem (UML) e arquitetura de software.

## 🎯 Objetivo do Projeto

O sistema resolve desafios comuns na gestão de cinemas, como o controle de filmes em cartaz, organização de sessões (respeitando intervalos e duração) e o registro diário de público. O foco principal é demonstrar a coerência entre a modelagem de requisitos e a implementação em código.

## 🛠️ Tecnologias e Arquitetura

* **Linguagem:** Será utlizado pelo vscode, PlantUML
* **Banco de Dados:** SQLite
* **Arquitetura:** MVC (Model, View, Controller) + Camada de Service + Padrão Repository
* **Modelagem:** Diagramas de Casos de Uso, Classes, Atividade e Sequência.

## ⚙️ Funcionalidades Principais

* Cadastro de cinemas (endereço e capacidade máxima).
* Cadastro de filmes (título, duração, elenco, diretor e gênero).
* Agendamento de sessões com validação de horários e intervalos.
* Registro de público diário.
* Geração de totais de público por sessão, filme e cinema.

  ### 🏗️ Arquitetura do Sistema

O fluxo de dados da aplicação segue uma separação estrita de responsabilidades, garantindo que a interface não acesse o banco de dados diretamente:

1. Diagrama de Arquitetura
   
<img width="759" height="398" alt="image" src="https://github.com/user-attachments/assets/fd410424-e639-4a7f-8c17-2a819e18501c" />

2. Diagrama de Modelo de Dados

   <img width="562" height="372" alt="image" src="https://github.com/user-attachments/assets/a40a59dc-4937-4e0e-a4dd-8001d493078d" />



## 📂 Estrutura do Projeto

Abaixo está a organização simplificada dos diretórios baseada na arquitetura escolhida:

```text
/
├── controllers/    # Controladores que recebem os dados das Views
├── models/         # Classes de domínio (Cinema, Filme, Sessao)
├── repositories/   # Persistência de dados (Conexão e queries SQLite)
├── services/       # Regras de negócio e validações
├── views/          # Interface com o usuário (Telas ou CLI)
└── main            # Arquivo principal para iniciar a aplicação
