# Módulo SXE
### Planteamento:
- Kanban para as empresas: 
  - Unha taboa kanban a cal permite crear as columnas que se deseen.
  - Para cada tarefa que se engade a estas taboas engadimos a fecha de solicitude.
  - Para cada tarefa calculárase fai cantos días se solicitou o proxecto (móstrase na vista tree)
  - Todos as columnas do kanban poden ser creadas dende a súa propia vista ou dende o kanban tendo unha descrición predeterminada
  - As columnas do kanban serán mostradas pese a non ter valores para poder cambiar o estado das tarefas só arrastrandoas as columnas correspondentes
  - As tarefas teñen campos requeridos, e non poderán ser creadas con datas posteriores a de uso da aplicación.
  - En caso de crear a base de datos con (Demo data), crearánse valores, os cales traerán tres estados para as tarefas e 4 tarefas.
  - En caso de engadir un novo estado para as tarefas (na súa vista propia) os regresar a taboa kanban aparecerá.
  - O caso contrario sucederá en caso de eliminala, ou cambiarán en caso de editalas.
  - Non se poderá borrar un estado/columna en caso de que algunha tarefa se encontre nela.