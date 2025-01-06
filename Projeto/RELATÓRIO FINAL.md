# Relatório da Interface Gráfica
## Unidade Curricular: Algoritmos e Técnicas de programação
#
### Docentes: José Carlos Ramalho, Luís Filipe Cunha
### Discentes: Diana Antunes Neves A107189, Dinis Azevedo Pereira A107276, Maria de Fátima da Silva Pereira A107160. 2ºAno de Licenciatura em Engenharia Biomédica
#
#### Índice
1. [Introdução](#introdução)
2. [Análise e Requisitos](#análise-e-requisitos)
    2.1. [Interface da Linha de Comando](#interface-da-linha-de-comando)  
    2.2. [Interface Gráfica](#interface-gráfica)  
3. [Estrutura de Dados](#estrutura-de-dados)
4. [Conceção do Algoritmo](#conceção-do-algoritmo)  
    4.1. [Bibliotecas](#bibliotecas)  
        4.1.1. [import PySimpleGUI as sg](#import-pysimplegui-as-sg)  
        4.1.2. [import matplotlib.pyplot as plt](#import-matplotlibpyplot-as-plt)  
        4.1.3. [from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg](#from-matplotlibbackendsbackend_tkagg-import-figurecanvastkagg)  
        4.1.4. [import json](#import-json)  
        4.1.5. [import os](#import-os)  
        4.1.6. [import os.path](#import-ospath)  
        4.1.7. [from datetime import datetime](#from-datetime-import-datetime)  
    4.2. [Funções](#funções)  
        4.2.1. [Ficheiro](#ficheiro)  
        4.2.2. [Menu](#menu)  
        4.2.3. [Exportação Parcial de Dados](#exportação-parcial-de-dados)  
        4.2.4. [Criar uma Publicação](#criar-uma-publicação)  
        4.2.5. [Atualizar uma Publicação](#atualizar-uma-publicação)  
        4.2.6. [Consultar uma Publicação](#consultar-uma-publicação)  
        4.2.7. [Apagar uma Publicação](#apagar-uma-publicação)  
        4.2.8. [Relatório de Estatísticas](#relatório-de-estatísticas)  
        4.2.9. [Análise de Publicações por Autor](#análise-de-publicações-por-autor)  
        4.2.10. [Análise de Publicações por Palavras-Chave](#análise-de-publicações-por-palavras-chave)  
        4.2.11. [Importar Novos Dados](#importar-novos-dados)  
        4.2.12. [Exportar Dados](#exportar-dados)  
        4.2.13. [Ajuda](#ajuda)  
        4.2.14. [Sair](#sair)  
4. [Linha de Comando](#linha_de_comando)
5. [Problemas de Concretização](#problemas-de-concretização)  
6. [Conclusão](#conclusão)

#### Introdução
Este projeto foi desenvolvido no âmbito da Unidade Curricular **Algoritmos e Técnicas de Programação** e tem como base a criação de uma aplicação com uma interface gráfica e uma linha de comando, que permita ao utilizador aceder a uma série de artigos publicados, registados num ficheiro, facilitando a sua visualização e a possível manipulação dos dados dos artigos. Para isso, foram desenvolvidas diversas ferramentas de pesquisa que utilizam filtros relevantes, como a data de publicação dos artigos, palavras-chave e informações sobre os autores. Além disso, a aplicação permite adicionar ou eliminar artigos, e disponibiliza um relatório de estatísticas que mostra gráficos sobre as informações presentes no ficheiro.

Este relatório apresenta o progresso deste projeto, dividindo-se em 6 partes principais:
    1. Uma breve explicação sobre a estrutura dos dados utilizados;
    2. A análise dos requisitos da aplicação;
    3. Uma descrição detalhada do *design* do algoritmo, com ênfase nas bibliotecas utilizadas e nas funções que desempenham papéis fundamentais no código geral;
    4. A Linha de Comando;
    5. Os erros que encontramos e como foram solucionados;
    6. Por fim, as realizações alcançadas graças a este projeto.

#### Análise e requisitos
A intenção do nosso trabalho foi desenvolver um sistema em Python que permitisse criar, atualizar e analisar publicações científicas.
Após analisarmos a proposta dos requisitos do projeto, começámos por desenvolver as funções que executariam cada requisito do sistema.
No entanto, uma das exigências do trabalho é o desenvolvimento de duas interfaces: Interface Gráfica e Interface da Linha de Comando. Assim sendo, ao abrir o programa, o utilizador tem a possibilidade de escolher a que pretende executar.
![alt text](https://i.postimg.cc/Prrm0bQj/Captura-de-ecr-2025-01-05-150802.png)
**Figura 1:** Escolha da Interface

##### Interface da Linha de Comando
A linha de comando remete-se à utilização de uma "interface" dentro de terminal do VSCode, com código escrito em Python. Esta, por sua vez, apresenta uma estrutura bastante semelhante à da interface gráfica, contudo, apresenta um *def menu()* seguido de *print()*, que, ao receber um input de 0 a 9, irá entregar ao utilizador a funcionalidade desejada.
As principais diferenças entre este modo e a interface gráfica são: a falta de *pop ups*, havendo apenas *print()* de informações.
A nosso ver, trata-se de uma Interface menos intuitiva do que a Interface Gráfica, uma vez que só é possível fazer um input de cada vez e há menos funcionalidades disponíveis, como por exemplo a possibilidade de fechar uma janela a qualquer momento.

##### Interface Gráfica
Executando a Interface Gráfica, a primeira janela a aparecer é **Carregamento de Dados**, que permite importar os dados de um ficheiro para o programa. 
![alt text](https://i.postimg.cc/DzYr3b0j/Captura-de-ecr-2025-01-04-191414.png)
**Figura 2:** Carregamento de Dados

Para cada requisito, desenvolvemos uma função que cumprisse o solicitado.
Por último, desenvolvemos uma interface gráfica que permite ao utilizador aceder ao sistema e às suas funcionalidades, um **Menu** que dá ao utilizador a opção de selecionar a função que pretende executar
![alt text](https://i.postimg.cc/FsRLTrhF/Captura-de-ecr-2025-01-05-151417.png)
**Figura 3:** Menu

Criámos as funções **Criar e Atualizar uma Publicação**, que permitem adicionar uma nova publicação e atualizar as informações de uma publicação existente no ficheiro de dados do sistema.

Para funções como **Atualizar uma publicação**, **Apagar uma publicação** foi necessário criar uma função intermediária que defina a publicação específica que o utilizador pretende manipular. Após receber um filtro, o programa irá definir por extenso os artigos que encontrou, dando ao utilizador a possibilidade de escolher um.
O código utilizado para definir esta função intermediária foi adaptado do código que utilizamos para definir a função **Consultar Publicação**.
![alt text](https://i.postimg.cc/CLf6PSPp/Captura-de-ecr-2025-01-04-192343.png)
**Figura 4:** Procurar publicações

No final da execução da pesquisa **Consulta de publicações**, o utilizador terá a opção de exportar os dados resultantes da pesquisa.
![alt text](https://i.postimg.cc/tCMDHfct/Captura-de-ecr-2025-01-04-193855.png)
**Figura 5:** Exportação parcial de dados

O código utilizado para definir esta função intermediária foi adaptado do código que utilizamos para definir a função **Exportar Dados**.

Dentro da função **Relatório de Estatísticas**, o utilizador pode escolher uma das seguintas opções. Se selecionar as opções **Gráfico de publicações de um autor por ano** ou **Gráfico de publicações por cada mês de um ano** o programa irá pedir ao utilizador para introduzir os dados necessários à execução dos gráficos. Caso contrário, os gráficos serão apresentados diretamente.
![alt text](https://i.postimg.cc/VLCmqyXd/Captura-de-ecr-2025-01-04-193103.png)
**Figura 6:** Escolha do relatório

Através da função **Importar novos dados**, o utilizador poderá novos artigos presentes num ficheiro .JSON à variável interna do programa.

Sempre que o utilizador fechar o programa, surgirá uma janela que lhe dará a opção de **Exportar dados**, função tal que pode chamar a qualquer momento, selecionando-a no menu. Desta forma, os dados manipulados estarão sempre salvaguardados.
![alt text](https://i.postimg.cc/vmN61FW3/Captura-de-ecr-2025-01-04-194321.png)
**Figura 7:** Exportar dados

#### Estrutura de dados
Para viabilizar o desenvolvimento do algoritmo, foi imprescindível definir uma estrutura de dados adequada ao projeto. Essa etapa é crucial para estabelecer uma linha de raciocínio clara que orienta a criação das funções que compõem o código.
Assim, a base de dados escolhida foi uma lista, onde cada elemento corresponde a uma publicação. Cada publicação nessa lista é representada por um dicionário, que contém as seguintes chaves: resumo, palavras-chave, autores, doi, pdf, data de publicação, título e url.
Os campos resumo, palavras-chave, doi, pdf, data de publicação, título e url armazenam valores do tipo string; e o campo autores consiste numa lista, onde cada elemento corresponde a um autor. Cada autor da lista é representado por um dicionário que contém as seguintes chaves: nome, afiliação e orcid.

![alt text](https://i.postimg.cc/5tZmck3R/Captura-de-ecr-2024-12-31-174905.png)
**Figura 8:** Estrutura de dados

#### Conceção do Algoritmo
##### Bibliotecas
* ***import PySimpleGUI as sg***
É uma biblioteca que permite a criação de interfaces gráficas (GUIs) em Python. Permite a criação rápida de janelas e elementos interativos como botões, campos de entrada, caixas de seleção e tabelas. Através desta biblioteca fomos capazes de criar uma interface para o programa, tornando-o mais acessível e eliminando a necessidade de usar a linha de comando.

* ***import matplotlib.pyplot as plt***
É uma biblioteca utilizada para a criação de gráficos e visualização de dados em Python. Fornece suporte a diferente tipos de gráficos e a sua personalização completa, incluindo eixos, cores, títulos e legendas. Integra-se com outras bibliotecas e ferramentas de GUI, como o PySimpleGUI. Através desta biblioteca conseguimos desenvolver a função “Relatório de estatísticas”, tornando o programa capaz de criar gráficos personalizados com base nas escolhas do utilizador.

* ***from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg***
É um submódulo do **módulo Matplotlib** utilizado para integrar gráficos gerados por ele diretamente nas janelas do PySimpleGUI, que usa Tkinter como backend. Sua principal utilidade é permitir a exibição de gráficos estatísticos ou analíticos de forma visual e interativa dentro da interface gráfica do programa.

* ***import json***
Trata-se de um módulo da biblioteca padrão do Python que é utilizado para manipular dados no formato de JSON (JavaScript Object Notation). Através deste módulo o programa é capaz de ler arquivos JSON e convertê-los para estruturas de dados do Python e também de escrever dados do Python em arquivos JSON para armazenamento ou exportação. A utilização deste módulo foi fundamental para o funcionamento do programa desenvolvido uma vez que tem por base a manipulação de dados que estão num ficheiro em formato JSON.

* ***import os***
Trata-se de um módulo da biblioteca padrão do Python que fornece funções para interagir com o sistema operacional. É utilizado para operações gerais no sistema de arquivos e permite uma maior flexibilidade e compatibilidade com diferentes sistemas operacionais.

* ***import os.path***
É um submódulo do **módulo os** que oferece ferramentas específicas para a manipulação de caminhos de arquivos e diretórios de forma compatível com diferentes sistemas operacionais. Verifica a existência de arquivos ou diretórios (os.path.isfile). Desta forma garantimos que o programa consegue localizar e verificar a existência de ficheiros que contêm dados (neste caso, ficheiros JSON), o que ajuda a evitar erros relacionados com caminhos incorretos de ficheiros.

Embora o **módulo os.path** seja extremamente útil para operações relacionadas a caminhos (os.path.join e os.path.isfile), precisamos do **módulo os** para manipular o sistema de arquivos (como criar, excluir ou listar arquivos e diretórios) ou realizar outras operações no sistema operacional. Embora no código não haja funções que necessitem diretamente de operações gerais, como listar diretórios ou alterar permissões, o **módulo os** é importado como uma dependência natural para trabalhar em conjunto com **módulo os.path**.

* ***from datetime import datetime**
Trata-se de um módulo da biblioteca padrão do Python usado para manipulação de datas e horários. Permite registrar ou manipular informações de tempo, como datas de criação, modificação ou publicação de artigos. O módulo datetime é essencial no programa para lidar com qualquer funcionalidade que envolva datas e horários.

##### Funções
###### **Ficheiro** 
Esta função é a porta para o nosso trabalho, visto que é esta que irá encontrar o *databank* que será utilizado em todas as funções.

* *def criar_layout_ficheiro()*
Gera a interface que permite ao utilizador escolher o nome do ficheiro .json a ser carregado.

* *def ficheiro()*
Aqui, o código irá procurar dentro da pasta selecionada pelo utilizador), um ficheiro com o nome escolhido e assim que o encontre, torna a variável databank a lista de dados com todos os valores do ficheiro, através de:

* *def carregar_json(fnome)*
Onde acontece a importação dos dados, estando pronta para caso aconteçam erros, principalmente através do código onde abre um arquivo fnome no modo de leitura (“r”).
Já o encoding=”uft-8” permite processar caracteres especiais (acentos, símbolos, etc.).

###### **Menu**
Para acedermos ao menu principal, primeiro, precisamos de percorrer algumas funções:

* *def criar_layout_menu()*
Que cria o layout usado dentro do menu, ou seja, todos os botões e texto são gerados graças a esta função.

* *def menu()*
Onde estão todos os botões que irão executar todo o código deste projeto tendo como base um ciclo while True, que liga o input do utilizador às diferentes funções. Desta forma, ao carregarmos em um botão, event vai se igualar ao nome do botão, que gera as infotmações dentro do while True. 

###### **Exportação parcial de dados** 
Após pesquisar informação, será questionado ao utilizador se ele quer exportar apenas esses dados para um novo ficheiro, isso é possivel graças a:

* *def exportacao_parcial(res)*
Que chama a função de exportar(dados).

###### **Criar uma publicação**
Esta é a função que permite ao utilizador criar, de total livre vontade, a publicação com as características que desejar para adicionar ao databank.

* *def criar_layout_artigo()*
Onde criamos uma interface intuitiva e com pequenas dicas, para tornar o processo de criação mais simples, usando funções como sg.Multiline e sg.Input de tamanhos específicos capazes de receber a informação para ser utilizada para criar dados.

* *def criar()*
Que ao ser chamada, mostra toda a estrutura da função anterior e é responsável por aumentar janelas [window.extend_layout()] e juntar tudo o que foi introduzido pelo autor nos seus respectivos lugares.

###### **Atualizar uma publicação**
Possibilita alteração do código em partes específicas através das suas várias funções:

* *def layout_listar_publicacoes(resultados)*
Onde está presente não só a interface mas também o processo de acoplamento das novas informações e das que não foram alteradas para remodelar a lista ao layout.

* *def atualizar_publish_date(artigo_atualizar)*
   *def atualizar_abstract(artigo_atualizar)*
   *def atualizar_keywords(artigo_atualizar)*
   *def atualizar_authors(artigo_atualizar)*
São funções auxiliares que ajudam a função principal a receber os dados.

* *def atualizar(databank)*
Onde o código principal acontece, capaz de reconhecer erros e de copiar e modificar o databank linha por linha.

###### **Consultar uma publicação** 
Aqui, podemos consultar uma publicação através da escolha do utilizador.

* *def extenso_gui(public)*
Em primeiro lugar, definimos uma função que ao receber dados os expõem de forma intuitiva para o autor.Desta forma, aquilo que o utilizador procurar procurar pode ser melhor visualizado.

* *def procurar(databank)*
É a função que permite ao autor escolher como quer procurar os dados, chama a função extenso_gui() , para mostrar todas as publicações que se enquadram nos parâmetros escolhidos pelo autor. Esta função é capaz de criar novas interfaces para guiar a procura do utilizador e mostrar os dados escolhidos.

###### **Apagar uma publicação**
* *def apagar(databank)*
Este código procura dentro do databank dados com a estrutura selecionada pelo utilizador para os eliminar por completo, usando um ciclo de for public in databank: para copiar todos os dados que não serão eliminados.

###### **Relatório de estatísticas**
Este botão leva o usuário a uma nova interface, onde poderá ver todo o tipo de estatísticas do databank que desejar.

* *def draw_figure(canvas_elem, figure)*
Permite renderizar um gráfico matplotlib em um elemento gráfico de uma janela feita com PySimpleGUI e integrar de forma transparente o matplotlib com a interface gráfica do PySimpleGUI usando o backend Tkinter.

* *def apagar(databank)def criar_layout_estat1()*
   *def criar_layout_estat2()*
São duas funções responsáveis por receber a informação que será utilizada para alguns gráficos, sendo estas duas puxadas mais tarde para uma bom funcionamento de todos os gráficos.

* *def criar_layout_estat3()*
Este é o layout que irá mostrar várias opções de gráficos para o utilizador visualizar ao carregar nos botões.

* *def estat()*
Por sua vez, esta função irá receber o input e irá chamar as próximas funções dando lhes os dados necessários para funcionar.
Em todas as seguintes funções vão ser criados gráficos, sendo por isso necessário criar legendas e valores para ser possivel a criação desses gráficos.

* *def disKWperANO(biglist)*
No caso da distribuição das top palavras-chave por ano, utilizamos estes códigos: x = list(top_keywords.keys()) y = list(top_keywords.values()), para definir o eixo dos x e dos y ; fig, ax = plt.subplots(figsize=(10, 6)) ax.bar(x, y, color='green'), tamanho e cor das colunas;  ax.set_title("Distribuição de Frequências das Top 20 Palavras-Chaves") ax.set_xlabel("Palavras-Chaves") ax.set_ylabel("Frequência"), legendas; ax.set_xticks(range(len(x))), duração/alcance (neste caso, as palavras-chave); ax.set_xticklabels(x, rotation=45, ha="right", fontsize=9), legendas; ax.set_yticks(range(10, max(y) + 10, max(1, max(y)//5))), marcadores do eixo y; plt.tight_layout(), que ajusta o gráfico. Assim, será possivel abrir um código com draw_figure().
Nota: Nas seguintes 5 funções usa-se um código muito semelhante.

Para além disso também é importante, neste caso, contar as palavras chave, usando o código for word in keywords:
for word in keywords:
        subwd = word.split("/") 
   for wd in subwd: 
        if wd in lekeywords: 
            lekeywords[wd] += 1 
        else: 
            lekeywords[wd] = 1

* *def disPUBarthorPerYear(biglist, authorname)*
Gera um gráfico de publicações de um autor por ano.

* *def yearlyDistrub(biglist)*
Cria o gráfico de publicações no ano escolhido.

* *def dis20KeyWord(biglist)*
Cria um gráfico da distribuição de frequências das top 20 palavras-chave.

* *def pubDISmesPano(biglist, year)*
Gera o gráfico de publicações por cada mês de um ano.

* *def dis20pubporArthor(biglist)*
Cria um gráfico de publicações por autor.

###### **Análise de publicações por autor**
Como o nome já diz, esta função permite a visualização de publicações de um autor específico.

* *def layout_autores(authors)*
Onde temos um layout que mostra os autores ordenados decrescentemente por número de publicações e deixa o utilizador escolher um que será utilizado como base na função:

* *def layout_publicacoes(listofPubs, autor)*
Que mostra as publicações da lista criada por:

* *def analiseauthor(databank)*
Uma função que encontra todas as publicações de um dado autor e permite à função anterior demonstrar apenas os dados corretos.

###### **Análise de publicações por palavras-chave**
Tal como a última função, esta função permite a visualização de publicações, mas, desta vez,por palavras-chave específicas.
Esta função funciona de forma bastante semelhante à anterior, apenas usando estas funções específicas para procurar os artigos com as palavras-chaves dentro do databank.

* *def layout_keywords(keywords)*
   *def layout_publicacoes1(listofpub, keyword)*
   *def analisekeyword(databank)*

###### **Importar novos dados**
Onde, podemos alterar o databank para utilizarmos novos dados.

* *def criar_layout_importar()*
Que contém uma interface simples e facil de utilizar.

* *def importar(databank)*
Uma função basicamente igual à inicial , [ficheiro()] capaz de ir buscar novos dados para o databank, completando (no caso de não acabar com .json) o nome do ficheiro escolhido.

###### **Exportar dados**
Capaz de exportar os dados para um ficheiro do agrado do utilizador.

* *def criar_layout_exportar()*
Onde, assim como até agora, está a interface da exportação de dados.

* *def exportar(databank)*
A função principal, onde os dados dentro de () irão ser copiados para um ficheiro externo json.

###### **Ajuda**
É a função responsável por entregar um pequeno resumo dentro do próprio código para o utilizador.

* *def ajuda()*
Que, ao contrário de várias funções principais, é apenas uma interface que explica cada botão dentro do menu e o que ele faz.

###### **Sair**
Tal como em todos os sites, é necessário conseguir sair da janela. Para isso, nós usamos: 

* if event in (sg.WIN_CLOSED, “Sair”).
Onde é verificado se o evento captado é igual a sg.WIN_CLOSED (janela fechada) ou a“Sair”(botão pressionado).

#### Problemas de Concretização
Ao longo deste projeto, enfrentámos vários contratempos, que nos obrigaram a procurar soluções diferentes e inovadoras.
Uma das nossas dificuldades foi a adaptação das funções para a interface gráfica, em particular o painel de controlo para os gráficos. Devido à sua formatação, tivemos de utilizar uma nova biblioteca, o que nos levou a reaprender como formatar corretamente os gráficos para que o relatório estatístico fosse esteticamente viável.
Outra dificuldade foi a adaptação do código do editor Jupyter Notebbok para um ficheiro Python, nomeadamente a função *def carregar_json(fnome)*, que sofreu uma grande reestruturação.
Em suma, os problemas que encontramos ao longo do desenvolvimento deste programa, seja qual fosse a sua dimensão, foram ultrapassados com base no intercâmbio de conhecimentos que adquirimos ao longo das aulas e na pesquisa de novas soluções.

#### Conclusão
O objetivo deste projeto era desenvolver uma aplicação que permita criar, atualizar e analisar publicações científicas, pesquisa das mesmas usando filtros relevantes (data de publicação, palavras-chave, autores, título, afiliação), gerar relatórios detalhados para a análise de métricas das publicações e dos seus autores. 
Consideramos que conseguimos cumprir todos os requisitos propostos.Esforçámo-nos bastante para que a nossa interface fosse de uso fácil e intuitivo, e acreditamos que atingimos esse objetivo.
Tudo o que adquirimos neste semestre foi determinante para a manipulação de dados e a criação de uma interface gráfica e de linha de comando, que levaram ao desenvolvimento bem-sucedido deste programa. 
Depois de uma análise cuidadosa, concluimos que este projeto foi importante para a consolidação de todos os conceitos aprendidos, para a compreensão da sua utilidade e de cada ferramenta que utilizamos e ainda para o aprimoramento da nossa capacidade de pesquisa e de resolução de problemas.