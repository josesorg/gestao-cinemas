## 3. Requisitos Não Funcionais (RNF) e Restrições Técnicas

* **RNF01 - Padrão Arquitetural:** O sistema deve ser estruturado
  obrigatoriamente utilizando a arquitetura em camadas MVC (Model, View,
  Controller), adicionando os padrões Service e Repository.

* **RNF02 - Persistência de Dados:** O sistema deve utilizar o banco de
  dados relacional **SQLite** de forma local, garantindo a gravação em disco
  sem a necessidade de servidores externos.

* **RNF03 - Tratamento de Erros e Usabilidade:** O sistema não deve exibir
  falhas de execução ou stack traces para o usuário. Em caso de violação de
  regra de negócio, o sistema deve exibir mensagens de erro claras.

* **RNF04 - Desempenho de Relatórios:** O sistema deve ser capaz de realizar
  os cálculos e exibições das totalizações de público de forma eficiente,
  retornando o resultado em até 2 segundos.

* **RNF05 - Portabilidade:** O sistema deve ser executável em múltiplos
  sistemas operacionais (Windows, Linux, macOS), necessitando apenas da
  linguagem base instalada e de suas dependências locais.
