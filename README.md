Coletar Informações de Redes Sociais e gravar no banco NoSQL
Aluno: Briner Nunes, 20/12/2016
Conclusão e Aplicação
Busquei as informações das postagens do momento no Twitter. Coletei dados de um dia inteiro, buscando pela hashtage (#) utilizada nos post. O Twitter gera informação a cada segundo do mundo inteiro, e você ter a capacidade de coletar essas informações e armazena-las gerando algumas analises em cima disso é bem empolgante. Além do conhecimento que agrega quando você mergulha nesse mundo de banco de dados NoSQL. Utilizei o banco de dados MongoDB, e executei a rotina de coleta na linguagem Python. Todo ambiente foi no Linux Ubuntu 16.04 LTS.

Metodologia
O método utilizado foi a captação dos post’s do twitter utilizando um algoritmo em Python, no qual o mesmo enxergava a rede do Twitter através de uma biblioteca chamada Tweepy. Nela já existe os métodos de checagem e busca desses dados na rede do Twitter (def on_data).
O algoritmo gera um arquivo Json no qual temporariamente armazena para a importação para o banco de dados mongodb posteriormente. A conexão com o mongo de dados mongodb é feita através da biblioteca Pymongo utilizando a classe MongoClient. Nesse local você adiciona as portas do banco de dados, o banco e o nome da coleção para importação dos dados coletados.
Antes de tudo isso é preciso criar alguns tokens de acesso no Twitter conforme print abaixo:
 
Resultados
Deixei o algoritmo coletando o dia todo, modificando o filtro de busca por palavra a cada hora. O total de documentos criado no mongo foi de 59045. Utilizei as seguintes palavras na busca:
•	Brasil
•	Lula
•	Temer
•	Natal
•	Tempo
•	Futebol
•	Minas Gerais
•	Jogos
•	Férias
•	Comercio
•	Dados
•	Pessoas
Conclusões
O trabalho nos mostra as possibilidades que existe hoje de coletas de dados e abre uma grande porta para você, de forma simples, aplicar isso é uma gestão de empresa, gerando relatórios de redes sociais. É possível, através desses relatórios, mostrar, por exemplo, se a sua empresa está sendo bem falada na internet, se estão falando dela e quais são os públicos que estão postando sobre sua empresa. O mundo dos bancos de dados NoSQL pra mim ainda é novo, mais com esse pouco tempo que convivi com essa realidade, conclui que de várias formas você pode contribuir, de forma positiva e precisa, através de informações que até pouco tempo atrás eram ignoradas.
