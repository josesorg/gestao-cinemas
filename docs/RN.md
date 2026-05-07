## 2. Regras de Negócio (RN)

* **RN01 - Limite de Capacidade:** A quantidade de público registrada em
  uma sessão não pode, sob nenhuma hipótese, ultrapassar a capacidade máxima
  estipulada para a unidade de cinema onde a sessão ocorre.

* **RN02 - Prevenção de Conflitos de Horário:** Um mesmo cinema não pode
  possuir duas sessões diferentes alocadas para acontecerem simultaneamente.

* **RN03 - Intervalo Obrigatório:** O sistema deve garantir um intervalo
  mínimo obrigatório (ex: 30 minutos) entre o horário de término de um filme
  e o início da próxima sessão no mesmo cinema, destinado à limpeza.

* **RN04 - Cálculo Automático de Término:** O horário de término de uma
  sessão não deve ser inserido manualmente. O sistema deve calculá-lo
  automaticamente somando a duração do filme ao horário de início da sessão.

* **RN05 - Validação Temporal:** O sistema não deve permitir o agendamento
  de novas sessões utilizando datas e horários retroativos (no passado).
