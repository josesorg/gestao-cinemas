## 3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais descrevem os atributos de qualidade do sistema,
focando na experiência do usuário e no funcionamento adequado da aplicação.

* **RNF01 - Usabilidade:** O sistema deve ser intuitivo e fácil de usar.
  Em caso de ações inválidas (como tentar agendar uma sessão com conflito), 
  o sistema deve apresentar mensagens de erro claras e amigáveis, sem 
  exibir códigos complexos para o usuário.

* **RNF02 - Desempenho:** O sistema deve processar os registros de público
  e gerar as consultas e relatórios de totalização de forma rápida, 
  evitando longas esperas para o funcionário do cinema.

* **RNF03 - Confiabilidade:** Os dados cadastrados (cinemas, filmes,
  sessões e público) devem ficar salvos de forma segura no sistema,
  garantindo que nenhuma informação seja perdida quando o aplicativo for fechado.

* **RNF04 - Manutenibilidade:** O sistema deve ser desenvolvido e estruturado
  de forma organizada, permitindo que outros desenvolvedores consigam entender,
  corrigir ou adicionar novas funcionalidades no futuro com facilidade.

* **RNF05 - Portabilidade:** O sistema deve ser capaz de funcionar
  corretamente em diferentes computadores da rede de cinemas, independentemente
  do sistema operacional utilizado nas máquinas (Windows, macOS ou Linux).
