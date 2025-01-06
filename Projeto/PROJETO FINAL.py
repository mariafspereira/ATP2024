import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os.path
import json
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

sg.theme('BrownBlue')

databank = []
databank_importado = []

def firstmenu_layout():
    layout_fm = [
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas", font=("Arial", 13, "bold"))],
        [sg.Button("Interface Gráfica",font=("Arial 14"), size=(35, 1))],
        [sg.Button("Interface de Linha de Comando", font="Arial 14", size=(35, 1))],
        [sg.Button("Sair", font="Arial 14", size=(9, 1))]
        ]
    return [[sg.Column(layout_fm, justification='center', element_justification='center')]]

def first_menu():
    window = sg.Window("Menu de Interface", firstmenu_layout(), resizable=True, finalize=True)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Sair":
            window.close()
            break
        elif event == "Interface Gráfica":
            window.close()
            inter_GUI()
            return
        elif event == "Interface de Linha de Comando":
            window.close()
            inter_CLI()
            return
        
    window.close

def inter_GUI():
# MENU PRINCIPAL
    def criar_layout_menu():
        layout = [
            [sg.Text("Selecione uma opção", font=("Arial", 13, "bold"))],
            [sg.Button("Criar uma publicação",font=("Arial 14", 14), size=(35, 1))],
            [sg.Button("Atualizar uma publicação", font="Arial 14", size=(35, 1))],
            [sg.Button("Consultar uma publicação", font="Arial 14", size=(35, 1))],
            [sg.Button("Apagar uma publicação", font="Arial 14", size=(35, 1))],
            [sg.Button("Relatório de estatísticas", font="Arial 14", size=(35, 1))],
            [sg.Button("Análise de publicações por autor", font="Arial 14", size=(35, 1))],
            [sg.Button("Análise de publicações por palavras-chave", font="Arial 14", size=(35, 1))],
            [sg.Button("Importar novos dados", font="Arial 14", size=(35, 1))],
            [sg.Button("Exportar dados", font="Arial 14", size=(35, 1))],
            [sg.Button("Ajuda", font="Arial 15", size=(9, 1)), sg.Button("Sair", font="Arial 14", size=(9, 1))]
        ]
        return [[sg.Column(layout, justification='center', element_justification='center')]]

    def menu():
        window = sg.Window("Menu", criar_layout_menu(), resizable=True, finalize=True)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                window.close()
                exportar(databank)
                break
            elif event == "Criar uma publicação":
                window.close()
                criar()
                menu()
                return
            elif event == "Atualizar uma publicação":
                window.close()
                atualizar(databank)
                menu()
                return
            elif event == "Consultar uma publicação":
                window.close()
                procurar(databank)
                menu()
                return
            elif event == "Apagar uma publicação":
                window.close()
                apagar(databank)
                menu()
                return
            elif event == "Relatório de estatísticas":
                window.close()
                estat()
                menu()
                return
            elif event == "Análise de publicações por autor":
                window.close()
                analiseauthor(databank)
                menu()
                return
            elif event == "Análise de publicações por palavras-chave":
                window.close()
                analisekeyword(databank)
                menu()
                return
            elif event == "Importar novos dados":
                window.close()
                importar(databank)
                menu()
                return
            elif event == "Exportar dados":
                window.close()
                exportar(databank)
                menu()
                return
            elif event == "Ajuda":
                window.close()
                ajuda()
                menu()
                return
        window.close()


    #CARREGAR FICHEIRO
    def carregar_json(fnome):
        try:
            with open(fnome, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            sg.popup_error(f"Arquivo {fnome} não encontrado.")
        except json.JSONDecodeError as e:
            sg.popup_error(f"Erro ao decodificar o arquivo JSON: {e}")
        except Exception as e:
            sg.popup_error(f"Erro inesperado: {e}")
        return None

    def criar_layout_ficheiro():
        return [
            [sg.Text("Insira o nome do ficheiro a carregar:", font=("Arial", 13, "bold")), sg.InputText(key="-ficheiro-", do_not_clear=True, size=(40, 1))],
            [sg.Text("Exemplo: ata_medica_papers.json", font=("Arial", 10))],
            [sg.Text("")],
            [sg.Text("Insira a localização do ficheiro a carregar:", font=("Arial", 13, "bold")), sg.InputText(key="-data-", do_not_clear=True, size=(80, 1))],
            [sg.Text("Exemplo: c:\\Users\\Nome_Utilizador\\Desktop\\Pasta", font=("Arial", 10))],
            [sg.Button("Ok", size=(4, 1), font="Arial 11"), sg.Button("Sair", size=(5, 1), font="Arial 11")]
        ]

    def ficheiro():
        global databank
        layout = criar_layout_ficheiro()
        window = sg.Window("Base de Dados", layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                break
            elif event == "Ok":
                filename = values["-ficheiro-"]
                data = values["-data-"]
                if not filename.endswith(".json"):
                    filename += ".json"
                # Ajustar o caminho do arquivo se necessário
                filename = os.path.join(data, filename)
                if os.path.isfile(filename):
                    databank = carregar_json(filename)
                    if databank is not None:
                        window.close()
                        menu()
                        return
                else:
                    sg.popup_error("Ficheiro não encontrado!", font="Arial 13 bold", title="Fracasso")
        window.close()

    #CRIAR UMA PUBLICAÇÃO
    def criar_layout_artigo():
        layout = [
            [sg.Text("Criar um novo artigo", font=("Arial", 13, "bold"))],
            [sg.Text("Caso o artigo não tenha algum parâmetro, não preencha o campo", font=("Arial", 10))],
            [sg.Text("Título:", font="Arial 11"), sg.Input(key="titulo", font="Arial 11", size=(24, 1))],
            [sg.Text("Resumo:", font="Arial 11"), sg.Multiline(key="resumo", size=(20, 3))],
            [sg.Text("Keywords:", font="Arial 11"), sg.Input(key="keywords", font="Arial 11", size=(21, 1))],
            [sg.Text("Data:", font="Arial 11"), sg.Input(key="data", font="Arial 11", size=(24, 1))],
            [sg.Text("Formato da data: aaaa-mm-dd", font=("Arial", 10))],
            [sg.Text("DOI:", font="Arial 11"), sg.Input(key="doi", font="Arial 11", size=(24, 1))],
            [sg.Text("PDF:", font="Arial 11"), sg.Input(key="pdf", font="Arial 11", size=(24, 1))],
            [sg.Text("URL:", font="Arial 11"), sg.Input(key="url", font="Arial 11", size=(24, 1))],
            [sg.Text("Autores:", font="Arial 11")],
            [sg.Text("Nome do Autor:", font="Arial 11"), sg.Input(key="autor_nome_1", font="Arial 11", size=(20, 1)),
            sg.Text("Afiliação do Autor:", font="Arial 11"), sg.Input(key="autor_afiliação_1", font="Arial 11", size=(20, 1)),
            sg.Text("ORCID do Autor:", font="Arial 11"), sg.Input(key="autor_orcid_1", font="Arial 11", size=(20, 1))],
            [sg.Button("Adicionar Autor", size=(14, 1), font="Arial 11")],
            [sg.Button("Salvar", size=(6, 1), font="Arial 11"), sg.Button("Cancelar", size=(8, 1), font="Arial 11")]
        ]
        return layout

    def criar():
        global databank
        window = sg.Window("Criar artigo", criar_layout_artigo())
        
        autores_contador = 1

        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break
            
            if event == "Adicionar Autor":
                autores_contador += 1
                window.extend_layout(window, [
                    [sg.Text(f"Nome do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_nome_{autores_contador}", font="Arial 11", size=(20, 1)),
                    sg.Text(f"Afiliação do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_afiliação_{autores_contador}", font="Arial 11", size=(20, 1)),
                    sg.Text(f"ORCID do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_orcid_{autores_contador}", font="Arial 11", size=(20, 1))]
                ])
            
            if event == "Salvar":
                authors = []
                for i in range(1, autores_contador + 1):
                    autor_nome = values.get(f"autor_nome_{i}")
                    autor_afiliação = values.get(f"autor_afiliação_{i}")
                    autor_orcid = values.get(f"autor_orcid_{i}")
                    autor = {
                        "name": autor_nome,
                        "affiliation": autor_afiliação,
                        "orcid": autor_orcid
                    }
                    autor_sem_vazios = {k: v for k, v in autor.items() if v}
                    authors.append(autor_sem_vazios)

                dicionario = {
                    "title": values["titulo"],
                    "keyword": values["keywords"],
                    "abstract":values["resumo"],
                    "authors": authors,
                    "doi": values["doi"],
                    "pdf": values["pdf"],
                    "url": values["url"],
                    "publish_date": values["data"]
                }

                dicionario_sem_vazios = {k: v for k, v in dicionario.items() if v}
                databank.append(dicionario_sem_vazios)
                
                sg.popup("Artigo salvo com sucesso!")
                break
        window.close()

    #ATUALIZAR UMA PUBLICAÇÃO
    def layout_listar_publicacoes(resultados):
            i = 1
            layout = [[sg.Text(f"Publicações encontradas", font="Arial 13 bold")]]
            for public in resultados:
                layout.append([sg.Text(f"Artigo {i}", font="Arial 13 bold")])
                if "title" in public:
                    layout.append([sg.Text("Título:", font="Arial 11 bold"), sg.Text(public["title"], font="Arial 10")])
                if "publish_date" in public:
                    layout.append([sg.Text("Data de publicação:", font="Arial 11 bold"), sg.Text(public["publish_date"], font="Arial 10")])
                if "authors" in public:
                    layout.append([sg.Text("Autores", font="Arial 11 bold")])

                    # Dados
                    nomes = "\n".join([autor.get("name", "N/A") for autor in public["authors"]])
                    afiliacoes = "\n".join([autor.get("affiliation", "N/A") for autor in public["authors"]])
                    orcids = "\n".join([autor.get("orcid", "N/A") for autor in public["authors"]])

                    # Layout das colunas
                    authors_layout = [
                        [
                            sg.Text("Nome", font="Arial 11 bold", pad=(3, 0)), 
                            sg.Text("Afiliação", font="Arial 11 bold", pad=(120, 0)), 
                            sg.Text("ORCID", font="Arial 11 bold", pad=(195, 0))
                        ],
                        [
                            sg.Multiline(
                                nomes, 
                                size=(20, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True,
                                key="ColunaNomes"
                            ),
                            sg.Multiline(
                                afiliacoes, 
                                size=(50, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True, 
                                key="ColunaAfil"
                            ),
                            sg.Multiline(
                                orcids, 
                                size=(30, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True,
                                key="ColunaOrcid"
                            ),
                        ]
                    ]
                    layout.extend(authors_layout)
                if "abstract" in public:
                    layout.append([sg.Text("Resumo:", font="Arial 11 bold")])
                    layout.append([sg.Multiline(public["abstract"], size=(80, 10), disabled=True, font="Arial 10")])
                if "keywords" in public:
                    layout.append([sg.Text("Keywords:", font="Arial 11 bold"), sg.Text(public["keywords"], font="Arial 10")])
                if "doi" in public:
                    layout.append([sg.Text("DOI:", font="Arial 11 bold"), sg.Text(public["doi"], font="Arial 10")])
                if "pdf" in public:
                    layout.append([sg.Text("PDF:", font="Arial 11 bold"), sg.Text(public["pdf"], font="Arial 10")])
                if "url" in public:
                    layout.append([sg.Text("URL:", font="Arial 11 bold"), sg.Text(public["url"], font="Arial 10")])
                i = i + 1
                layout.append([sg.Text("")])
            
            layout.append([sg.Text("Escolha o índice da publicação a atualizar", font=("Arial", 11, "bold"))])
            layout.append([sg.InputText(key="INDICE", font="Arial 11")])
            layout.append([sg.Text("Introduza um número inteiro", font=("Arial", 10))])
            layout.append([sg.Text("Escolha o parâmetro a atualizar", font=("Arial", 11, "bold"))])
            layout.append([sg.InputText(key="PARAMETRO", font="Arial 11")])
            layout.append([sg.Text("Parâmetros possíveis: publish_date, abstract, keywords, authors", font=("Arial", 10))])
                
        
            return [
                [sg.Column(
                    layout,
                    size=(900, 600),  # Define a área visível (largura x altura)
                    scrollable=True,
                    vertical_scroll_only=False
                )],
                [sg.Button("Selecionar", font=("Arial", 11), size=(9, 1)), sg.Button("Cancelar", font="Arial 11", size = (9,1))]
            ]

    def atualizar_publish_date(artigo_atualizar):
        layout = [
            [sg.Text("Insira a nova data de publicação: ", font="Arial 11 bold")],
            [sg.InputText(key="NOVO_VALOR", font="Arial 11")],
            [sg.Text("Introduza a data no formato: aaaa-mm-dd", font="Arial 10")],
            [sg.Button("Atualizar", font=("Arial", 11), size=(9,1)), sg.Button("Cancelar", font=("Arial", 11), size=(9,1))]
        ]
        window = sg.Window("Atualizar", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return
            elif event == "Atualizar":
                novo_valor = values["NOVO_VALOR"].strip()
                if novo_valor:
                    artigo_atualizar["publish_date"] = novo_valor
                    sg.popup("Data de publicação atualizada com sucesso!")
                else:
                    sg.popup("Por favor, insira um valor para a data de publicação.")
            window.close()
            return artigo_atualizar
            
    def atualizar_abstract(artigo_atualizar):
        layout = [
            [sg.Text("Insira o novo resumo: ", font="Arial 11 bold")],
            [sg.InputText(key="NOVO_VALOR", font="Arial 11")],
            [sg.Button("Atualizar", font=("Arial", 11), size=(9,1)), sg.Button("Cancelar", font=("Arial", 11), size=(9,1))]
        ]
        window = sg.Window("Atualizar", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return
            elif event == "Atualizar":
                novo_valor = values["NOVO_VALOR"].strip()
                if novo_valor:
                    artigo_atualizar["abstract"] = novo_valor
                    sg.popup("Resumo atualizada com sucesso!")
                else:
                    sg.popup("Por favor, insira um valor para o resumo.")
            window.close()
            return artigo_atualizar

    def atualizar_keywords(artigo_atualizar):
        layout = [
            [sg.Text("Insira as novas palavras-chave: ", font="Arial 11 bold")],
            [sg.InputText(key="NOVO_VALOR", font="Arial 11")],
            [sg.Text("Introduza as palavras chave no formato: Exposição Ambiental, Portugal, Poluição pelo Fumo do Tabaco/efeitos adversos", font="Arial 10")],
            [sg.Button("Atualizar", font=("Arial", 11), size=(9,1)), sg.Button("Cancelar", font=("Arial", 11), size=(9,1))]
        ]
        window = sg.Window("Atualizar", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return
            elif event == "Atualizar":
                novo_valor = values["NOVO_VALOR"].strip()
                if novo_valor:
                    artigo_atualizar["keywords"] = novo_valor
                    sg.popup("Palavras-chave atualizadas com sucesso!")
                else:
                    sg.popup("Por favor, insira um valor para o resumo.")
            window.close()
            return artigo_atualizar
            
    def atualizar_authors(artigo_atualizar):
        layout = [[sg.Text("Insira os dados do(s) autor(es) ", font="Arial 11 bold")],
                [sg.Text("Nome do Autor:", font="Arial 11"), sg.InputText(key="autor_nome_1", font="Arial 11", size=(20, 1)),
                    sg.Text("Afiliação do Autor:", font="Arial 11"), sg.InputText(key="autor_afiliação_1", font="Arial 11", size=(20, 1)),
                    sg.Text("ORCID do Autor:", font="Arial 11"), sg.InputText(key="autor_orcid_1", font="Arial 11", size=(20, 1))],
                [sg.Button("Adicionar Autor", size=(14, 1), font="Arial 11")],
                [sg.Button("Atualizar", size=(9, 1), font="Arial 11"), sg.Button("Cancelar", size=(9, 1), font="Arial 11")]
        ]
                
        window = sg.Window("Atualizar", layout)
        autores_contador = 1
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                return None
            
            if event == "Adicionar Autor":
                autores_contador += 1
                window.extend_layout(window, [
                    [sg.Text(f"Nome do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_nome_{autores_contador}", font="Arial 11", size=(20, 1)),
                    sg.Text(f"Afiliação do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_afiliação_{autores_contador}", font="Arial 11", size=(20, 1)),
                    sg.Text(f"ORCID do Autor {autores_contador}:", font="Arial 11"), sg.Input(key=f"autor_orcid_{autores_contador}", font="Arial 11", size=(20, 1))]
                ])

            elif event == "Atualizar":
                authors = []
                for i in range(1, autores_contador + 1):
                    autor_nome = values.get(f"autor_nome_{i}")
                    autor_afiliação = values.get(f"autor_afiliação_{i}")
                    autor_orcid = values.get(f"autor_orcid_{i}")
                    autor = {
                        "name": autor_nome,
                        "affiliation": autor_afiliação,
                        "orcid": autor_orcid
                    }
                    autor_sem_vazios = {k: v for k, v in autor.items() if v}
                    authors.append(autor_sem_vazios)
                artigo_atualizar["authors"] = authors
                sg.popup("Autores atualizados com sucesso!")
        
                window.close()
                return artigo_atualizar

    def atualizar(databank):
        # Janela inicial para escolher o filtro
        layout_inicial = [
            [sg.Text("Escolha o filtro que pretende utilizar para procurar a publicação", font=("Arial", 13, "bold"))],
            [sg.Radio("Título", "FILTRO", font=("Arial", 11), key="TITULO", default=True)],
            [sg.Radio("Autores", "FILTRO", font=("Arial", 11), key="AUTORES")],
            [sg.Radio("Afiliação", "FILTRO", font=("Arial", 11), key="AFILIACAO")],
            [sg.Radio("Data de publicação", "FILTRO", font=("Arial", 11), key="DATA")],
            [sg.Radio("Palavras-chave", "FILTRO", font=("Arial", 11), key="PALAVRAS_CHAVE")],
            [sg.Button("Continuar", font=("Arial", 11), size=(9,1)), sg.Button("Cancelar", font=("Arial", 11), size=(9,1))]
        ]

        window = sg.Window("Procurar publicações", layout_inicial)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Continuar":
                if values["TITULO"]:
                    chave = "title"
                elif values["AUTORES"]:
                    chave = "authors"
                elif values["AFILIACAO"]:
                    chave = "affiliation"
                elif values["DATA"]:
                    chave = "publish_date"
                elif values["PALAVRAS_CHAVE"]:
                    chave = "keywords"
                else:
                    sg.popup("Por favor, selecione um filtro!")
                    continue

                window.close()
                break

        layout_filtro = [
            [sg.Text(f"Insira o valor para o filtro '{chave}'", font=("Arial", 13, "bold"))],
            [sg.InputText(key="FILTRO_INPUT", font="Arial 11")],
            [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
        ]
        window_filtro = sg.Window(f"Procurar por {chave.capitalize()}", layout_filtro)

        while True:
            event, values = window_filtro.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window_filtro.close()
                return None

            if event == "Procurar":
                filtro_valor = values["FILTRO_INPUT"].strip().lower()
                if not filtro_valor:
                    sg.popup("Por favor, insira um valor para o filtro!")
                    continue
                window_filtro.close()
                break

        resultados = []

        for public in databank:
            if chave == "title" and filtro_valor in public.get("title", "").lower():
                resultados.append(public)
            elif chave == "authors":
                autores = [autor.get("name", "").lower() for autor in public.get("authors", [])]
                if any(filtro_valor in autor for autor in autores):
                    resultados.append(public)
            elif chave == "affiliation":
                for autor in public.get("authors", []):
                    if filtro_valor in autor.get("affiliation", "").lower():
                        resultados.append(public)
            elif chave == "publish_date" and filtro_valor == public.get("publish_date", "").lower():
                resultados.append(public)

            elif chave == "keywords" and isinstance(public.get("keywords", ""), str):
                kwds = public.get("keywords", "")
                if kwds:  
                    keywds = [kw.strip().lower() for kw in public["keywords"].split(",")]
                    for w in keywds:
                        keywords=[word for word in w.split("/")]
                if filtro_valor in keywords:
                    resultados.append(public)


        if not resultados:
            sg.popup("Nenhuma publicação encontrado com o filtro especificado.")
            return None

        window_atualizar = sg.Window("Atualizar Artigo", layout_listar_publicacoes(resultados))

        while True:
            event, values = window_atualizar.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window_atualizar.close()
                return None

            if event == "Selecionar":
                try:
                    indice = int(values["INDICE"]) - 1
                    parametro = values["PARAMETRO"].strip()

                    if not parametro:
                        sg.popup_error("Por favor, insira o parâmetro a ser atualizado.")
                        continue

                    if 0 <= indice < len(resultados):
                        artigo_atualizar = resultados[indice]
                        if parametro in artigo_atualizar:
                            if parametro == "publish_date":
                                window_atualizar.close()
                                atualizar_publish_date(artigo_atualizar)
                            elif parametro == "abstract":
                                window_atualizar.close()
                                atualizar_abstract(artigo_atualizar)
                            elif parametro == "keywords":
                                window_atualizar.close()
                                atualizar_keywords(artigo_atualizar)
                            elif parametro == "authors":
                                window_atualizar.close()
                                atualizar_authors(artigo_atualizar)
                        else:
                            sg.popup_error(f"O parâmetro '{parametro}' não existe no artigo.")
                    else:
                        sg.popup_error("Índice inválido.")
                except ValueError:
                    sg.popup_error("Por favor, insira um índice válido.")


    #CONSULTAR UMA PUBLICAÇÃO
    #Definir por extenso 
    def extenso_lista(resultados):
        i = 1
        layout = [[sg.Text(f"Publicações encontradas", font="Arial 13 bold")]]
        for public in resultados:
            layout.append([sg.Text(f"Artigo {i}", font="Arial 13 bold")])
            if "title" in public:
                layout.append([sg.Text("Título:", font="Arial 11 bold"), sg.Text(public["title"], font="Arial 10")])
            if "publish_date" in public:
                layout.append([sg.Text("Data de publicação:", font="Arial 11 bold"), sg.Text(public["publish_date"], font="Arial 10")])
            if "authors" in public:
                layout.append([sg.Text("Autores", font="Arial 11 bold")])

                # Dados
                nomes = "\n".join([autor.get("name", "N/A") for autor in public["authors"]])
                afiliacoes = "\n".join([autor.get("affiliation", "N/A") for autor in public["authors"]])
                orcids = "\n".join([autor.get("orcid", "N/A") for autor in public["authors"]])

                # Layout das colunas
                authors_layout = [
                    [
                        sg.Text("Nome", font="Arial 11 bold", pad=(3, 0)), 
                        sg.Text("Afiliação", font="Arial 11 bold", pad=(120, 0)), 
                        sg.Text("ORCID", font="Arial 11 bold", pad=(195, 0))
                    ],
                    [
                        sg.Multiline(
                            nomes, 
                            size=(20, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True,
                            key="ColunaNomes"
                        ),
                        sg.Multiline(
                            afiliacoes, 
                            size=(50, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True, 
                            key="ColunaAfil"
                        ),
                        sg.Multiline(
                            orcids, 
                            size=(30, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True,
                            key="ColunaOrcid"
                        ),
                    ]
                ]
                layout.extend(authors_layout)
            if "abstract" in public:
                layout.append([sg.Text("Resumo:", font="Arial 11 bold")])
                layout.append([sg.Multiline(public["abstract"], size=(80, 10), disabled=True, font="Arial 10")])
            if "keywords" in public:
                layout.append([sg.Text("Keywords:", font="Arial 11 bold"), sg.Text(public["keywords"], font="Arial 10")])
            if "doi" in public:
                layout.append([sg.Text("DOI:", font="Arial 11 bold"), sg.Text(public["doi"], font="Arial 10")])
            if "pdf" in public:
                layout.append([sg.Text("PDF:", font="Arial 11 bold"), sg.Text(public["pdf"], font="Arial 10")])
            if "url" in public:
                layout.append([sg.Text("URL:", font="Arial 11 bold"), sg.Text(public["url"], font="Arial 10")])
            i = i + 1
            layout.append([sg.Text("")])
        layout.append([sg.Button("Sair", size=(6, 1), font=("Arial 11"))])

        scrollable_layout = [[sg.Column(layout, scrollable=True, vertical_scroll_only=False, size=(900, 600))]]
        window = sg.Window("Publicações Encontradas", scrollable_layout, resizable=True)    

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Sair"):
                window.close()
                return

    def procurar(databank):
        layout_inicial = [
            [sg.Text("Escolha o filtro que pretende utilizar para procurar a publicação", font=("Arial", 13, "bold"))],
            [sg.Radio("Título", "FILTRO", font=("Arial", 11), key="TITULO")],
            [sg.Radio("Autores", "FILTRO", font=("Arial", 11), key="AUTORES")],
            [sg.Radio("Afiliação", "FILTRO", font=("Arial", 11), key="AFILIACAO")],
            [sg.Radio("Data de publicação", "FILTRO", font=("Arial", 11), key="DATA")],
            [sg.Radio("Palavras-chave", "FILTRO", font=("Arial", 11), key="PALAVRAS_CHAVE")],
            [sg.Button("Continuar", font=("Arial", 11), size=(9, 1)), sg.Button("Sair", font=("Arial", 11), size=(5, 1))]
        ]

        window = sg.Window("Procurar publicações", layout_inicial)
                
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Sair":
                window.close()
                return

            if event == "Continuar":
                if values["TITULO"]:
                    chave = 1
                elif values["AUTORES"]:
                    chave = 2
                elif values["AFILIACAO"]:
                    chave = 3
                elif values["DATA"]:
                    chave = 4
                elif values["PALAVRAS_CHAVE"]:
                    chave = 5
                else:
                    sg.popup("Por favor, selecione um filtro!")
                    continue
                
                window.close()
                break

        if chave == 1: 
            layout_titulo = [
                [sg.Text("Insira o título da publicação", font=("Arial 11 bold"))],
                [sg.InputText(key="TITULO_INPUT", font="Arial 11")],
                [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
            ]
            window_titulo = sg.Window("Procurar por Título", layout_titulo)
            while True:
                event, values = window_titulo.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window_titulo.close()
                    return
                if event == "Procurar":
                    titulo = values["TITULO_INPUT"]
                    res = []
                    for public in databank:
                        if "title" in public and titulo.lower() in public['title'].lower():
                            res.append(public)
                    if res:
                        window.close()
                        sg.popup(f"Foram encontradas {len(res)} publicações.")
                        extenso_lista(res)
                        exportacao_parcial(res)
                    else:
                        sg.popup(f"Não foi encontrado nenhuma publicação com o título '{titulo}'.")
                    window_titulo.close()
                    break

        elif chave == 2:
            layout_autores = [
                [sg.Text("Insira os nomes dos autores (separados por vírgulas)", font=("Arial 11 bold"))],
                [sg.InputText(key="AUTORES_INPUT", font="Arial 11")],
                [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
            ]
            window_autores = sg.Window("Procurar por Autores", layout_autores)

            while True:
                event, values = window_autores.read()

                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    sg.popup("Operação cancelada.")
                    window_autores.close()
                    return

                if event == "Procurar":
                    nome = values["AUTORES_INPUT"]

                    # Validação básica da entrada
                    if not nome.strip():
                        sg.popup("Por favor, insira pelo menos um nome de autor.")
                        continue

                    autores_nome = [autor.strip().lower() for autor in nome.split(",")]
                    res = []

                    # Verificação segura do databank
                    try:
                        for public in databank:
                            if "authors" in public:
                                names = [author["name"].strip().lower() for author in public["authors"] if "name" in author]
                                if any(autor in names for autor in autores_nome):
                                    res.append(public)
                    except Exception as e:
                        sg.popup(f"Ocorreu um erro ao procurar os autores: {e}")
                        break

                    # Exibir resultados
                    if res:
                        window.close()
                        sg.popup(f"Foram encontradas {len(res)} publicações.")
                        extenso_lista(res)
                        exportacao_parcial(res)
                    else:
                        sg.popup(f"Não foi encontrada nenhuma publicação pelos autores '{nome}'.")
                    
                    window_autores.close()
                    break


        elif chave == 3:
            layout_afiliacao = [
                [sg.Text("Insira a afiliação (separada por vírgulas)", font=("Arial 11 bold"))],
                [sg.InputText(key="AFILIACAO_INPUT", font="Arial 11")],
                [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
            ]
            window_afiliacao = sg.Window("Procurar por Afiliação", layout_afiliacao)
            while True:
                event, values = window_afiliacao.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window_afiliacao.close()
                    return
                if event == "Procurar":
                    nome = values["AFILIACAO_INPUT"]
                    res = []
                    for public in databank:
                        if "authors" in public:
                            for autor in public["authors"]:
                                if "affiliation" in autor and nome.lower() in autor["affiliation"].lower():
                                    res.append(public)
                    if res:
                        window.close()
                        sg.popup(f"Foram encontradas {len(res)} publicações.")
                        extenso_lista(res)
                        exportacao_parcial(res)
                    else:
                        sg.popup(f"Não foi encontrado nenhuma publicação pela afiliação '{nome}'.")
                    window_afiliacao.close()
                    break

        elif chave == 4:
            layout_data = [
                [sg.Text("Insira a data de publicação (aaaa-mm-dd)", font=("Arial 11 bold"))],
                [sg.InputText(key="DATA_INPUT", font="Arial 11")],
                [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
            ]
            window_data = sg.Window("Procurar por Data de publicação", layout_data)
            while True:
                event, values = window_data.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window_data.close()
                    return
                if event == "Procurar":
                    data = values["DATA_INPUT"]
                    res = []
                    for public in databank:
                        if "publish_date" in public and public["publish_date"] == data:
                            res.append(public)
                    if res:
                        window.close()
                        sg.popup(f"Foram encontradas {len(res)} publicações.")
                        extenso_lista(res)
                        exportacao_parcial(res)
                    else:
                        sg.popup(f"Não foi encontrado nenhuma publicação com a data '{data}'.")
                    window_data.close()
                    break

        elif chave == 5:
            layout_palavras = [
                [sg.Text("Insira as palavras-chave (separadas por vírgulas)", font=("Arial 11 bold"))],
                [sg.InputText(key="PALAVRAS_INPUT", font="Arial 11")],
                [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
            ]
            window_palavras = sg.Window("Procurar por Palavras-Chave", layout_palavras)
            while True:
                event, values = window_palavras.read()
                if event in (sg.WINDOW_CLOSED, "Cancelar"):
                    window_palavras.close()
                    return
                if event == "Procurar":
                    nome = values["PALAVRAS_INPUT"]
                    keywords_nome = [keyword.strip().lower() for keyword in nome.split(",")]
                    
                    res = []
                    for public in databank:
                        if "keywords" in public:
                            keywds_public = [keyword.strip().lower() for keyword in public['keywords'].split(",")]
                            for word in keywds_public:
                                keywords_public =[w for w in word.split("/")]
                            if any(keyword in keywords_public for keyword in keywords_nome):
                                res.append(public)
                    if res:
                        window.close()
                        sg.popup(f"Foram encontradas {len(res)} publicações.")
                        extenso_lista(res)
                        exportacao_parcial(res)
                    else:
                        sg.popup(f"Não foi encontrado nenhuma publicação pelas palavras-chave '{nome}'.")
                    window_palavras.close()
                    break
            
    #EXPORTAÇÃO PARCIAL DE DADOS
    def exportacao_parcial(res):
        layout = [
            [sg.Text("Deseja exportar os resultados desta pesquisa?", font=("Arial", 13, "bold"))],
            [sg.Button("Sim", size=(4, 1), font="Arial 11"), sg.Button("Não", size=(5, 1), font="Arial 11")]
        ]
        window = sg.Window("Exportação Parcial de Dados", layout)
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Não":
                window.close()
                return
            elif event == "Sim":
                exportar(res)
                window.close()
                return
        
    #APAGAR UMA PUBLICAÇÃO
    def apagar(databank):
        # Janela inicial para escolher o filtro
        layout_inicial = [
            [sg.Text("Escolha o filtro que pretende utilizar para procurar a publicação", font=("Arial 13 bold"))],
            [sg.Radio("Título", "FILTRO", font=("Arial 11"), key="TITULO", default=True)],
            [sg.Radio("Autores", "FILTRO", font=("Arial 11"), key="AUTORES")],
            [sg.Radio("Afiliação", "FILTRO", font=("Arial 11"), key="AFILIACAO")],
            [sg.Radio("Data de publicação", "FILTRO", font=("Arial 11"), key="DATA")],
            [sg.Radio("Palavras-chave", "FILTRO", font=("Arial 11"), key="PALAVRAS_CHAVE")],
            [sg.Button("Continuar", font=("Arial 11"), size=(9, 1)), sg.Button("Sair", font=("Arial 11"), size=(5, 1))]
        ]

        window = sg.Window("Procurar Artigos", layout_inicial)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Sair"):
                window.close()
                return None

            if event == "Continuar":
                if values["TITULO"]:
                    chave = "title"
                elif values["AUTORES"]:
                    chave = "authors"
                elif values["AFILIACAO"]:
                    chave = "affiliation"
                elif values["DATA"]:
                    chave = "publish_date"
                elif values["PALAVRAS_CHAVE"]:
                    chave = "keywords"
                else:
                    sg.popup("Por favor, selecione um filtro!")
                    continue

                window.close()
                break

        layout_filtro = [
            [sg.Text(f"Insira o valor para o filtro '{chave}'", font=("Arial 13 bold"))],
            [sg.InputText(key="FILTRO_INPUT", font="Arial 11")],
            [sg.Button("Procurar", font=("Arial 11"), size=(8, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))]
        ]
        window_filtro = sg.Window(f"Procurar por {chave.capitalize()}", layout_filtro)

        while True:
            event, values = window_filtro.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window_filtro.close()
                return None

            if event == "Procurar":
                filtro_valor = values["FILTRO_INPUT"].strip().lower()
                if not filtro_valor:
                    sg.popup("Por favor, insira um valor para o filtro!")
                    continue
                window_filtro.close()
                break

        resultados = []

        for public in databank:
            if chave == "title" and filtro_valor in public.get("title", "").lower():
                resultados.append(public)
            elif chave == "authors":
                autores = [autor.get("name", "").lower() for autor in public.get("authors", [])]
                if any(filtro_valor in autor for autor in autores):
                    resultados.append(public)
            elif chave == "affiliation":
                for autor in public.get("authors", []):
                    if filtro_valor in autor.get("affiliation", "").lower():
                        resultados.append(public)
            elif chave == "publish_date" and filtro_valor == public.get("publish_date", "").lower():
                resultados.append(public)
            elif chave == "keywords" and isinstance(public.get("keywords", ""), str):
                words = public.get("keywords", "")
                if words:
                    kwds = [kw.strip().lower() for kw in public["keywords"].split(",")]
                    for word in kwds:
                        keywords = [w for w in word.split("/")]
                if filtro_valor in keywords:
                    resultados.append(public)

        if not resultados:
            sg.popup("Nenhuma publicação encontrado com o filtro especificado.")
            return None

        layout_lista = [[sg.Text("Artigos encontrados:")]]
        for i, artigo in enumerate(resultados):
            layout_lista.append([sg.Text(f"{i + 1}. {artigo.get('title', 'Sem título')}")])

        layout_lista.append([sg.Text("Escolha o índice da publicação a apagar", font=("Arial 11 bold"))])
        layout_lista.append([sg.InputText(key="INDICE", font="Arial 11")])
        layout_lista.append([sg.Text("Introduza um número inteiro", font=("Arial 10"))])
        layout_lista.append([sg.Button("Apagar", font=("Arial 11"), size=(6, 1)), sg.Button("Cancelar", font=("Arial 11"), size=(8, 1))])

        window_atualizar = sg.Window("Apagar Artigo", layout_lista)

        while True:
            event, values = window_atualizar.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window_atualizar.close()
                return None

            if event == "Apagar":
                try:
                    indice = int(values["INDICE"]) - 1

                    if 0 <= indice < len(resultados):
                        databank.remove(resultados[indice])
                    else:
                        sg.popup_error("Índice inválido.")
                except ValueError:
                    sg.popup_error("Por favor, insira um índice válido.")
                finally:
                    window_atualizar.close()
                    break


    #RELATÓRIO DE ESTATÍSTICAS
    def draw_figure(canvas_elem, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas_elem.TKCanvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(fill='both', expand=True)

    def criar_layout_estat1():
        return[
            [sg.Text("Indique o ano que pretende estudar:", font="Arial 11"), sg.Input(key="Ano", font="Arial 11")],
            [sg.Button("Pesquisar", font=("Arial 11"), size=(9, 1))]
        ]

    def criar_layout_estat2():
        return[
            [sg.Text("Indique o nome do autor que pretende estudar:", font="Arial 11"), sg.Input(key="Autor", font="Arial 11")],
            [sg.Button("Pesquisar", font=("Arial 11"), size=(9, 1))]
        ]

    def criar_layout_estat3():
        layout= [
            [sg.Text("Selecione uma opção", font="Arial 13 bold")],
            [sg.Button("Gráfico de publicações por ano", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Gráfico de publicações por cada mês de um ano", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Gráfico de publicações por autor", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Gráfico de publicações de um autor por ano", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Distribuição de frequêncis das top 20 palavras-chave", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Distribuição das top palavras-chave por ano", font=("Arial 14"), size=(50, 1))],
            [sg.Button("Cancelar", font=("Arial 14"), size=(9, 1))],
        ]
        return [[sg.Column(layout, justification='center', element_justification='center')]]

    def estat():
        window = sg.Window("Escolha do relatório", criar_layout_estat3(), font=('Arial', 24))

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                break
            if event == "Gráfico de publicações por ano":
                yearlyDistrub(databank)
            if event == "Gráfico de publicações por cada mês de um ano":
                window.close()
                window = sg.Window("Estatísticas", criar_layout_estat1(), font=('Arial', 24))
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        window.close()
                        window = sg.Window("Escolha do relatório", criar_layout_estat3(), font=('Arial', 24))
                        break
                    elif event == "Pesquisar":
                        try:
                            ano = int(values["Ano"])
                            if len(str(ano)) == 4:
                                pubDISmesPano(databank, ano)
                        except ValueError:
                            sg.popup_error("Por favor, insira um ano válido!")
            if event == "Gráfico de publicações por autor":
                dis20pubporArthor(databank)
            if event == "Gráfico de publicações de um autor por ano":
                window.close()
                window = sg.Window("Estatísticas", criar_layout_estat2(), font=('Arial', 24))
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        window.close()
                        window = sg.Window("Escolha do relatório", criar_layout_estat3(), font=('Arial', 24))
                        break
                    elif event == "Pesquisar":
                        nome = values["Autor"]
                        if nome != "":
                            disPUBarthorPerYear(databank, nome)
            if event == "Distribuição de frequêncis das top 20 palavras-chave":
                dis20KeyWord(databank)
            if event == "Distribuição das top palavras-chave por ano":
                disKWperANO(databank)
        window.close()
        return

    def disKWperANO(biglist):
        kwpyear = {}

        # Processa as publicações e conta as palavras-chave por ano
        for public in biglist:
            valid = True  

            if "publish_date" not in public or "keywords" not in public:
                valid = False

            if valid:
                try:
                    # Extrai apenas a parte antes de "—" (se existir)
                    clean_date = public["publish_date"].split("—")[0].strip()
                    leyear = datetime.strptime(clean_date, "%Y-%m-%d").year
                except ValueError:
                    print(f"Invalid date format in: {public['publish_date']}")
                    valid = False

            if valid:  
                kword = public["keywords"].split(",")
                for wrd in kword:
                    for keyword in wrd.split("/"):
                        if leyear not in kwpyear:
                            kwpyear[leyear] = {}
                        kwpyear[leyear][keyword] = kwpyear[leyear].get(keyword, 0) + 1

        # Ordena as palavras-chave por ano e seleciona a mais frequente de cada ano
        freqword = []
        keywordpyear = {}
        keywordy = dict(sorted(kwpyear.items(), key=lambda pair: pair[0]))
        
        for leyear in keywordy:
            lelist = sorted(keywordy[leyear].items(), key=lambda pair: pair[1], reverse=True)
            freqword.append(lelist[0][0])
            keywordpyear[leyear] = lelist[0][1]

        # Criação do gráfico
        x = list(keywordpyear.keys())
        y = list(keywordpyear.values())

        # Plota o gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(x, y, color='indigo')
        ax.set_title("Distribuição das Top Palavras-Chave por Ano")
        ax.set_xlabel("Ano")
        ax.set_ylabel("Frequência da Palavra-chave")
        ax.set_xticks(x)
        if y:  # Verifica se a lista y não está vazia
            ax.set_yticks(range(0, max(y) + 2, max(1, max(y) // 5)))
        else:
            # Exibe uma mensagem de erro na interface
            sg.popup("Aviso", "A lista de dados (y) está vazia. Nenhum dado para exibir no gráfico.", keep_on_top=True)
            ax.set_yticks([0])  # Define um tick padrão
        plt.tight_layout()

        # Adiciona as palavras-chave no topo das barras
        for bar, word in zip(bars, freqword):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, word, ha='center', va='bottom', fontsize=10)

        # Criando uma nova janela para o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window("Gráfico de Palavras-Chave por Ano", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break

        graph_window.close()

    def dis20KeyWord(biglist):
        lekeywords = {}

        # Processa as publicações e conta a frequência das palavras-chave
        for public in biglist:
            if "keywords" in public:
                keywords = public["keywords"].split(",")

                for word in keywords:
                    subwd = word.split("/")
                    for wd in subwd:
                        if wd in lekeywords:
                            lekeywords[wd] += 1
                        else:
                            lekeywords[wd] = 1

        # Ordena as palavras-chave por frequência e pega as top 20
        sorted_keywords = sorted(lekeywords.items(), key=lambda pair: pair[1], reverse=True)
        top_keywords = dict(sorted_keywords[:20])

        # Prepara os dados para o gráfico
        x = list(top_keywords.keys())
        y = list(top_keywords.values())

        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x, y, color='green')
        ax.set_title("Distribuição de Frequências das Top 20 Palavras-Chaves")
        ax.set_xlabel("Palavras-Chaves")
        ax.set_ylabel("Frequência")
        ax.set_xticks(range(len(x)))
        ax.set_xticklabels(x, rotation=45, ha="right", fontsize=9)
        ax.set_yticks(range(10, max(y) + 10, max(1, max(y)//5)))
        plt.tight_layout()

        # Criando uma nova janela para o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window("Gráfico de Frequência das Palavras-Chaves", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break

        graph_window.close()

    def disPUBarthorPerYear(biglist, authorname):
        pubyear = {}

        # Processa as publicações e conta por ano para o autor específico
        for public in biglist:
            for autor in public["authors"]:
                if autor["name"].lower() == authorname.lower():
                    if "publish_date" in public:
                        pday = datetime.strptime(public["publish_date"], "%Y-%m-%d")
                        if pday.year in pubyear:
                            pubyear[pday.year] += 1
                        else:
                            pubyear[pday.year] = 1

        # Ordena o dicionário por ano
        pubpyear = dict(sorted(pubyear.items()))

        # Prepara os dados para o gráfico
        x = list(pubpyear.keys())
        y = list(pubpyear.values())

        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x, y, color='gold')
        ax.set_title(f"Distribuição de Publicações de {authorname} por Ano")
        ax.set_xlabel("Anos")
        ax.set_ylabel("Número de Publicações")
        ax.set_xticks(x)
        if y:  # Verifica se a lista y não está vazia
            ax.set_yticks(range(0, max(y) + 2, max(1, max(y) // 5)))
        else:
            # Exibe uma mensagem de erro na interface
            sg.popup("Aviso", "A lista de dados (y) está vazia. Nenhum dado para exibir no gráfico.", keep_on_top=True)
            ax.set_yticks([0])  # Define um tick padrão
        ax.tick_params(axis='x', labelrotation=45)
        plt.tight_layout()

        # Criando uma nova janela para o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window(f"Gráfico de Publicações de {authorname}", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break

        graph_window.close()

    def yearlyDistrub(biglist):
        dic = {}
        
        # Aqui você percorre a lista de dados e calcula a distribuição por ano
        for public in biglist:
            # Verifica se a chave "publish_date" está presente no item
            if "publish_date" in public:
                fulldate = public['publish_date']
                date = fulldate[0:4]  # Extrai o ano da data
                if date in dic:
                    dic[date] += 1
                else:
                    dic[date] = 1

        dicti = dict(sorted(dic.items()))  # Ordena o dicionário pelas chaves (anos)

        # Gera o gráfico
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(dicti.keys(), dicti.values(), color='blue')
        ax.set_title("Distribuição de Publicações por Ano")
        ax.set_xlabel("Anos")
        ax.set_ylabel("Número de Publicações")
        ax.tick_params(axis='x', labelrotation=45)
        ax.set_yticks([50, 100, 150])

        # Criando uma nova janela para exibir o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window("Gráfico de Publicações por Ano", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela de gráfico
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break
        
        graph_window.close()

    def pubDISmesPano(biglist, year):

        # Mapeamento de números de meses para nomes
        month = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 
                7: "Jul", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
        
        # Dicionário para armazenar contagem de publicações por mês
        gragh = {}
        
        # Processa cada publicação na lista
        for public in biglist:
            if "publish_date" in public:
                strdate = public["publish_date"]
                # Extrai a parte válida da data
                date_part = strdate.split("—")[0].strip()
                try:
                    # Converte a string de data em um objeto datetime
                    datefrm = datetime.strptime(date_part, "%Y-%m-%d")
                    # Filtra apenas publicações do ano especificado
                    if datefrm.year == year:
                        month_name = month[datefrm.month]
                        gragh[month_name] = gragh.get(month_name, 0) + 1
                except ValueError:
                    print(f"Invalid date format found: {strdate}.")
        
        # Ordena o dicionário por ordem dos meses
        legragh = {k: gragh.get(k, 0) for k in month.values()}

        # Prepara os dados para o gráfico
        x = list(legragh.keys())
        y = list(legragh.values())

        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(x, y, color='pink')
        ax.set_title(f"Distribuição de Publicações por mês de {year}")
        ax.set_xlabel("Meses")
        ax.set_ylabel("Número de Publicações")
        if y:  # Verifica se a lista y não está vazia
            ax.set_yticks(range(0, max(y) + 2, max(1, max(y) // 5)))
        else:
            # Exibe uma mensagem de erro na interface
            sg.popup("Aviso", "A lista de dados (y) está vazia. Nenhum dado para exibir no gráfico.", keep_on_top=True)
            ax.set_yticks([0])  # Define um tick padrão
        ax.tick_params(axis='x', labelrotation=45)

        # Criação de uma nova janela para exibir o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window(f"Gráfico de Publicações - {year}", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela de gráfico
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break

        graph_window.close()

    def dis20pubporArthor(biglist):

        # Dicionário para armazenar a contagem de publicações por autor
        leauthor = {}

        # Processa cada publicação na lista
        for public in biglist:
            for autor in public["authors"]:
                if autor["name"] in leauthor:
                    leauthor[autor["name"]] += 1
                else:
                    leauthor[autor["name"]] = 1

        # Ordena os autores pelo número de publicações (descendente) e pega os 20 primeiros
        almostd = sorted(leauthor.items(), key=lambda pair: pair[1], reverse=True)
        theauthor = dict(almostd[:20])

        # Prepara os dados para o gráfico
        x = list(theauthor.keys())
        y = list(theauthor.values())

        # Criação do gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x, y, color='grey')
        ax.set_title("Distribuição de Publicações por Autor")
        ax.set_xlabel("Autor")
        ax.set_ylabel("Número de Publicações")
        ax.set_yticks(range(0, max(y) + 5, max(1, max(y)//5)))
        ax.set_xticks(range(len(x)))
        ax.set_xticklabels(x, rotation=45,ha="right")
        plt.tight_layout()

        # Criação de uma nova janela para exibir o gráfico
        layout = [
            [sg.Canvas(key='canvas')]  # Canvas onde o gráfico será desenhado
        ]
        graph_window = sg.Window("Gráfico de Publicações por Autor", layout, finalize=True)

        # Chama a função para desenhar o gráfico na nova janela
        draw_figure(graph_window['canvas'], fig)

        # Aguarda até o usuário fechar a janela de gráfico
        while True:
            event, _ = graph_window.read()
            if event == sg.WIN_CLOSED:
                break

        graph_window.close()


    #ANÁLISE DE PUBLICAÇÕES POR AUTOR
    def layout_autores(authors):
        return[
            [sg.Text("Autores ordenados decrescentemente por número de publicações", font="Arial 13 bold")],
            [sg.Text("Selecione um autor", font="Arial 11")],
            [sg.Listbox(authors, size = (20,10), key="-AUTHOR-", enable_events=True)],
            [sg.Button("Ver Publicações", font= "Arial 11", size= (13,1)), sg.Button("Sair", font="Arial 11", size = (5,1))]
        ]

    def layout_publicacoes(listofPubs, autor):
            i = 1
            layout = [[sg.Text(f"Publicações de {autor}", font="Arial 13 bold")]]
            for public in listofPubs:
                layout.append([sg.Text(f"Artigo {i}", font="Arial 13 bold")])
                if "title" in public:
                    layout.append([sg.Text("Título:", font="Arial 11 bold"), sg.Text(public["title"], font="Arial 10")])
                if "publish_date" in public:
                    layout.append([sg.Text("Data de publicação:", font="Arial 11 bold"), sg.Text(public["publish_date"], font="Arial 10")])
                if "authors" in public:
                    layout.append([sg.Text("Autores", font="Arial 11 bold")])

                    # Dados
                    nomes = "\n".join([autor.get("name", "N/A") for autor in public["authors"]])
                    afiliacoes = "\n".join([autor.get("affiliation", "N/A") for autor in public["authors"]])
                    orcids = "\n".join([autor.get("orcid", "N/A") for autor in public["authors"]])

                    # Layout das colunas
                    authors_layout = [
                        [
                            sg.Text("Nome", font="Arial 11 bold", pad=(3, 0)), 
                            sg.Text("Afiliação", font="Arial 11 bold", pad=(120, 0)), 
                            sg.Text("ORCID", font="Arial 11 bold", pad=(195, 0))
                        ],
                        [
                            sg.Multiline(
                                nomes, 
                                size=(20, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True,
                                key="ColunaNomes"
                            ),
                            sg.Multiline(
                                afiliacoes, 
                                size=(50, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True, 
                                key="ColunaAfil"
                            ),
                            sg.Multiline(
                                orcids, 
                                size=(30, 7), 
                                disabled=True, 
                                font="Arial 10", 
                                horizontal_scroll=True,
                                key="ColunaOrcid"
                            ),
                        ]
                    ]
                    layout.extend(authors_layout)
                if "abstract" in public:
                    layout.append([sg.Text("Resumo:", font="Arial 11 bold")])
                    layout.append([sg.Multiline(public["abstract"], size=(80, 10), disabled=True, font="Arial 10")])
                if "doi" in public:
                    layout.append([sg.Text("DOI:", font="Arial 11 bold"), sg.Text(public["doi"], font="Arial 10")])
                if "pdf" in public:
                    layout.append([sg.Text("PDF:", font="Arial 11 bold"), sg.Text(public["pdf"], font="Arial 10")])
                if "url" in public:
                    layout.append([sg.Text("URL:", font="Arial 11 bold"), sg.Text(public["url"], font="Arial 10")])
                i = i + 1
                layout.append([sg.Text("")])
                
        
            return [
                [sg.Column(
                    layout,
                    size=(900, 600),  # Define a área visível (largura x altura)
                    scrollable=True,
                    vertical_scroll_only=False
                )],
                [sg.Button("Sair", font="Arial 11", size = (5,1))]
            ]

    def analiseauthor(databank):
        
        freq = {}
        for public in databank:
            for author in public["authors"]:
                name = author["name"]
            
                if name in freq:
                    freq[name] += 1
                else:
                    freq[name] = 1 
        
        writers = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
        authors = [key for key,value in writers]

        window_autores = sg.Window("Análise de Publicações por Autores", layout_autores(authors) , font="Arial 14")
        
        while True:
            event, values = window_autores.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                break

            if event == "Ver Publicações":
                autor = values["-AUTHOR-"]
                if not autor:
                    sg.popup("Por favor, selecione um autor!")
                    continue

            
                listofPubs = [public for public in databank for author in public["authors"] if author["name"].lower() == autor[0].lower()]


                if not listofPubs:
                    sg.popup(f"Não foram encontradas publicações para o autor {autor}.")
                else:
                    
                    layout_pubs = layout_publicacoes(listofPubs, autor)
                    pub_window = sg.Window("Publicações por Autor", layout_pubs, font="Arial 14")
                    while True:
                        pub_event, pub_values = pub_window.read()
                        if pub_event == "Sair" or pub_event== sg.WINDOW_CLOSED :
                            pub_window.close()
                            break
                
        window_autores.close()
        return


    #ANÁLISE DE PUBLICAÇÕES POR PALAVRAS-CHAVE
    def layout_keywords(keywords):
        return [
            [sg.Text("Palavras-chave ordenadas decrescentemente por número de publicações", font="Arial 13 bold")],
            [sg.Text("Selecione uma palavra-chave", font="Arial 11")],
            [sg.Listbox(keywords, size=(30, 10), key="-KEYWORDS-", enable_events=True)],
            [sg.Button("Ver Publicações", font="Arial 11", size=(13, 1)), sg.Button("Sair", font="Arial 11", size=(5, 1))]
        ]

    def layout_publicacoes1(listofpub, keyword):
        i = 1
        layout = [[sg.Text(f"Publicações de {keyword}", font="Arial 13 bold")]]
        for public in listofpub:
            layout.append([sg.Text(f"Artigo {i}", font="Arial 13 bold", pad=(0, 10))])
            if "title" in public:
                layout.append([sg.Text("Título:", font="Arial 11 bold"), sg.Text(public["title"], font="Arial 10")])
            if "publish_date" in public:
                layout.append([sg.Text("Data de publicação:", font="Arial 11 bold"), sg.Text(public["publish_date"], font="Arial 10")])
            if "authors" in public:
                layout.append([sg.Text("Autores", font="Arial 11 bold")])

                # Dados
                nomes = "\n".join([autor.get("name", "N/A") for autor in public["authors"]])
                afiliacoes = "\n".join([autor.get("affiliation", "N/A") for autor in public["authors"]])
                orcids = "\n".join([autor.get("orcid", "N/A") for autor in public["authors"]])

                # Layout das colunas
                authors_layout = [
                    [
                        sg.Text("Nome", font="Arial 11 bold", pad=(3, 0)), 
                        sg.Text("Afiliação", font="Arial 11 bold", pad=(120, 0)), 
                        sg.Text("ORCID", font="Arial 11 bold", pad=(195, 0))
                    ],
                    [
                        sg.Multiline(
                            nomes, 
                            size=(20, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True,
                            key="ColunaNomes"
                        ),
                        sg.Multiline(
                            afiliacoes, 
                            size=(50, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True, 
                            key="ColunaAfil"
                        ),
                        sg.Multiline(
                            orcids, 
                            size=(30, 7), 
                            disabled=True, 
                            font="Arial 10", 
                            horizontal_scroll=True,
                            key="ColunaOrcid"
                        ),
                    ]
                ]
                layout.extend(authors_layout)   
            if "abstract" in public:
                layout.append([sg.Text("Resumo:", font="Arial 11 bold")])
                layout.append([sg.Multiline(public["abstract"], size=(80, 10), disabled=True, font="Arial 10")])
            if "doi" in public:
                layout.append([sg.Text("DOI:", font="Arial 11 bold"), sg.Text(public["doi"], font="Arial 10")])
            if "pdf" in public:
                layout.append([sg.Text("PDF:", font="Arial 11 bold"), sg.Text(public["pdf"], font="Arial 10")])
            if "url" in public:
                layout.append([sg.Text("URL:", font="Arial 11 bold"), sg.Text(public["url"], font="Arial 10")])
            i = i + 1
            layout.append([sg.Text("")])

        return [
            [sg.Column(
                layout,
                size=(900, 600),
                scrollable=True,
                vertical_scroll_only=True
            )],
            [sg.Button("Sair", font="Arial 11", size=(5, 1))]
        ]

    def analisekeyword(databank):
        skeywords = {}
        for public in databank:
            if "keywords" in public:
                unfiltered = public["keywords"].split(",")
                for wordy in unfiltered:
                    for word in wordy.split("/"):
                        word = word.strip().lower()
                        skeywords[word] = skeywords.get(word, 0) + 1

        dickeywords = dict(sorted(skeywords.items(), key=lambda pair: pair[1], reverse=True))
        keywords = list(dickeywords.keys())

        window = sg.Window("Análise de Publicações por Palavras-chave", layout_keywords(keywords), font="Arial 14")

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                break
            if event == "Ver Publicações":
                keyword = values["-KEYWORDS-"][0]

                listofpub = []
                for public in databank:
                    if "keywords" in public:
                        unfiltered = public["keywords"].split(",")
                        for wordy in unfiltered:
                            for word in wordy.split("/"):
                                if word.strip().lower() == keyword.lower():
                                    listofpub.append(public)

                window2 = sg.Window(f"Publicações de '{keyword}'", layout_publicacoes1(listofpub, keyword), font="Arial 14")
                while True:
                    event2, _ = window2.read()
                    if event2 in ("Sair", sg.WIN_CLOSED):
                        window2.close()
                        break

        window.close()
        return


    #IMPORTAR NOVOS DADOS
    def criar_layout_importar():
        return [
            [sg.Text("Insira o nome do ficheiro a importar:", font=("Arial", 13, "bold")), sg.InputText(key="-ficheiro-", font="Arial 11", do_not_clear=True)],
            [sg.Text("Exemplo: ata_medica_papers1.json", font=("Arial", 10))],
            [sg.Text("")],
            [sg.Text("Insira a localização do ficheiro a carregar:", font=("Arial", 13, "bold")), sg.InputText(key="-data-", do_not_clear=True, size=(80, 1))],
            [sg.Text("Exemplo: c:\\Users\\Nome_Utilizador\\Desktop\\Pasta", font=("Arial", 10))],
            [sg.Button("Ok", size=(4, 1), font="Arial 11"), sg.Button("Sair", size=(5, 1), font="Arial 11")]
        ]

    def importar(databank):
        layout = criar_layout_importar()
        window = sg.Window("Base de Dados", layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                break
            elif event == "Ok":
                filename = values["-ficheiro-"]
                data = values["-data-"]
                if not filename.endswith(".json"):
                    filename += ".json"
                # Ajustar o caminho do arquivo se necessário
                filename = os.path.join(data, filename)
                if os.path.isfile(filename):
                    databank.append(filename)
                    sg.popup("Ficheiro importado!", font="Arial 13 bold", title="Sucesso")
                    menu()
                    return
                else:
                    sg.popup_error("Ficheiro não importado!", font="Arial 13 bold", title="Fracasso")
        window.close()


    #EXPORTAR DADOS
    def criar_layout_exportar():
        return [
            [sg.Text("Introduza o nome do ficheiro:", font="Arial 13 bold"), sg.Input(key="nome", font="Arial 11", size=(30, 1))],
            [sg.Text("Exemplo: ata_atualizada.json", font=("Arial", 10))],
            [sg.Text("")],
            [sg.Text("Insira a localização do ficheiro:", font=("Arial", 13, "bold")), sg.InputText(key="data", do_not_clear=True, size=(80, 1))],
            [sg.Text("Exemplo: c:\\Users\\Nome_Utilizador\\Desktop\\Pasta", font=("Arial", 10))],
            [sg.Button("Salvar", font=("Arial", 11), size=(6, 1)), sg.Button("Cancelar", font=("Arial", 11), size=(8, 1))]
        ]

    def exportar(databank):
        layout = criar_layout_exportar()
        window = sg.Window("Exportar Dados", layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                window.close()
                break
            elif event == "Salvar":
                fnome = values["nome"]
                data = values["data"]
                if not fnome.endswith(".json"):
                    fnome += ".json"
                filename = os.path.join(data, fnome)
                try:
                    with open(filename, "w", encoding="utf-8") as file:
                        json.dump(databank, file, indent=4, ensure_ascii=False)
                    
                    sg.popup("Exportação concluída com sucesso!", f"Os dados foram salvos no arquivo: {fnome}")
                
                except Exception as e:
                    sg.popup_error(f"Ocorreu um erro ao exportar os dados: {e}")
            window.close()

    #AJUDA
    def ajuda():
        layout = [
            [sg.Text("Criar uma publicação:", font="Arial 11 bold"), sg.Text("Permite a criação de um novo artigo definido pelos parâmetros escolhidos pelo utilizador (título, resumo, palavras-chave, DOI, lista de autores com respetivos orcid e afiliação, url para ficheiro PDF do artigo, data de publicação e url do artigo)", font="Arial 11", size=(75, None))],
            [sg.Text("Atualizar uma publicação:", font="Arial 11 bold"), sg.Text("Possibilita a modificação das informações dos artigos tais como título, resumo, palavras-chave, DOI, lista de autores com respetivos orcid e afiliação, url para ficheiro PDF do artigo, data de publicação e url do artigo", font="Arial 11", size=(75, None))],
            [sg.Text("Consultar uma publicação:", font="Arial 11 bold"), sg.Text("Viabiliza a pesquisa de artigos através de filtros específicos", font="Arial 11", size=(75, None))],
            [sg.Text("Apagar uma publicação:", font="Arial 11 bold"), sg.Text("Permite a eliminação de um artigo escolhido pelo utilizador", font="Arial 11", size=(75, None))],
            [sg.Text("Relatório de estatísticas:", font="Arial 11 bold"), sg.Text("Apresenta relatórios que incluem gráficos que representam as distribuições de publicações por ano, de publicações por mês de um determinado ano, de publicações de um autor por ano, de palavras-chave pela sua frequência (top 20 palavras-chave), da palavra-chave mais frequente por ano e ainda o número de publicações por autor (top 20 autores)", font="Arial 11", size=(75, None))],
            [sg.Text("Análise de publicações por autor:", font="Arial 11 bold"), sg.Text("Permite a visualização de publicações de um autor específico", font="Arial 11", size=(75, None))],
            [sg.Text("Análise de publicações por palavras-chave:", font="Arial 11 bold"), sg.Text("Possibilita a visualização de publicações de uma palavra-chave específica", font="Arial 11", size=(75, None))],
            [sg.Text("Importar novos dados:", font="Arial 11 bold"), sg.Text("Viabiliza a importações de novos dados, que serão acrescentados à variável interna do programa", font="Arial 11", size=(75, None))],
            [sg.Text("Exportar dados:", font="Arial 11 bold"), sg.Text("Possibilita o armazenamento dos dados que inicialmente foram importados com as modificações realizadas pelo utilizador", font="Arial 11", size=(75, None))],
            [sg.Text("Sair:", font="Arial 11 bold"), sg.Text("Fecha o programa", font="Arial 11", size=(75, None))],
            [sg.Button("Sair", font="Arial 11", size=(5, 1))]
        ]

        window = sg.Window("Ajuda", layout, modal=True, finalize=True, size=(900, 500), resizable=False)

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "Sair"):
                window.close()
                break

    ficheiro()
    return


def inter_CLI():
#MENU PRINCIPAL
    def menuCLI():
        while True:
            print("""Escolha a opção que pretende:
            1) Ajuda
            2) Criar uma publicação
            3) Atualizar uma publicação
            4) Consultar publicações
            5) Eliminar uma publicação
            6) Relatório de Estatísticas
            7) Análise de Publicações por Autor 
            8) Análise de Publicações por Palavras-chave
            9) Exportar dados
            0) Sair
            """)
            op = int(input("Escolha uma opção: "))
            if op == 1:
                print("""
                    1) Ajuda: Mostra o menu de ajuda.
                    2) Criar uma publicação: Permite a criação de um novo artigo definido pelos parâmetros escolhidos pelo utilizador (título, resumo, palavras-chave, DOI, lista de autores com respetivos orcid e afiliação, url para ficheiro PDF do artigo, data de publicação e url do artigo.
                    3) Atualizar uma publicação: Possibilita a modificação das informações dos artigos tais como título, resumo, palavras-chave, DOI, lista de autores com respetivos orcid e afiliação, url para ficheiro PDF do artigo, data de publicação e url do artigo.
                    4) Consultar publicações: Viabiliza a pesquisa de artigos através de filtros específicos.
                    5) Eliminar uma publicação: Permite a eliminação de um artigo escolhido pelo utilizador.
                    6) Relatório de Estatísticas: Apresenta relatórios que incluem gráficos que representam as distribuições de publicações por ano, de publicações por mês de um determinado ano, de publicações de um autor por ano, de palavras-chave pela sua frequência (top 20 palavras-chave), da palavra-chave mais frequente por ano e ainda o número de publicações por autor (top 20 autores).
                    7) Análise de Publicações por Autor: Permite a visualização de publicações de um autor específico
                    8) Análise de Publicações por Palavras-chave: Possibilita a visualização de publicações de uma palavra-chave específica.
                    9) Exportar dados: Possibilita o armazenamento dos dados que inicialmente foram importados com as modificações realizadas pelo utilizador.
                    0) Sair: Fecha o programa.
                    """)
            elif op == 2:
                criarCLI(databank)
            elif op == 3:
                atualizarCLI(databank)
            elif op == 4:
                procurarCLI(databank)
            elif op == 5:
                apagarCLI(databank)
            elif op == 6:
                rel_EstatisCLI(databank)
            elif op == 7:
                analiseauthorCLI(databank)
            elif op == 8:
                analisekeywordCLI(databank)
            elif op == 9:
                exportarCLI(databank)
            elif op == 0:
                exportarCLI(databank)
                print("O programa foi encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    #CARREGAR FICHEIRO
    def carregar_jsonCLI(fnome):
        if not fnome.endswith(".json"):
            fnome += ".json"
        try:
            file = open(fnome, "r", encoding="utf-8")
            return json.load(file)
        except FileNotFoundError:
            print(f"Arquivo {fnome} não encontrado.")
            return None
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None

    def ficheiroCLI():
        global databank
        fnome = input("Insira o nome do ficheiro a carregar: ")
        data = input("Insira a localização do ficheiro a carregar: ")
        if not fnome.endswith(".json"):
            fnome += ".json"
        filename = os.path.join(data, fnome)
        if os.path.isfile(filename):
            databank = carregar_jsonCLI(filename)
            if databank is not None:
                print("Ficheiro carregado com sucesso!")
                menuCLI()  
            else:
                print("Falha ao carregar o ficheiro.")

    #CRIAR PUBLICAÇÃO
    def criarCLI(databank):
        título = input("Introduza o título da publicação: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        resumo = input("Introduza o resumo da publicação: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        keywords = input("Introduza as keywords da publicação: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        data = input("Introduza a data da publicação em formato aaaa-mm-dd: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        doi = input("Introduza o DOI da publicação: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        pdf = input("Introduza o URL do ficheiro PDF: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        url = input("Introduza o URL do artigo: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
        autores = []
        num = int(input("Introduza o número de autores da publicação: "))
        i = 1
        while i <= num:
            nome = input(f"Introduza o nome do autor {i}/{num}: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
            afiliação = input(f"Introduza a afiliação do autor {nome}: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
            orcid = input(f"Introduza o orcid do autor {nome}: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
            autor = {"name": nome, "affiliation": afiliação, "orcid": orcid}
            autor_sem_vazios = {chave: valor for chave, valor in autor.items() if valor}
            autores.append(autor_sem_vazios)
            i = i + 1

        dicionario = {"abstract": resumo, "keywords": keywords, "authors": autores, "doi": doi, "pdf": pdf, "publish_date": data, "title": título, "url": url}
        dicionario_sem_vazios = {chave: valor for chave, valor in dicionario.items() if valor}
            
        return databank.append(dicionario_sem_vazios)

    #ATUALIZAR PUBLICAÇÃO
    #Definir por extenso 
    def extensoCLI(public):
        if "title" in public:
            print("Título: " + public['title'])
        if "publish_date" in public:
            print("Data de publicação: " + public['publish_date'])
        if "authors" in public:
            print("De: ")
            for autor in public["authors"]:
                print(f"  * Nome: {autor['name']}")
                if 'orcid' in autor:
                    print(f"    ORCID: {autor['orcid']}")
                if 'affiliation' in autor:
                    print(f"    Afiliação: {autor['affiliation']}")
        if 'abstract' in public:
            print("Resumo: " + public['abstract'])
        if "doi" in public:
            print("DOI: " + public["doi"])
        if "pdf" in public:
            print("PDF: " + public["pdf"])
        if "url" in public:
            print("URL: " + public["url"] + "\n")


    # Função intermédia: Procurar1
    def procurar1CLI(databank):
        chave = int(input ("""Escolha o filtro que pretende utilizar para procurar o artigo?
                            1) Título
                            2) Autores
                            3) Afiliação
                            4) Data de publicação
                            5) Palavras-chave
                            """))
        
        if chave == 1:
            res = []
            título = input("Insira o título do artigo: ")
            contador = 0
            
            for public in databank:
                if "title" in public and título.lower() in public['title'].lower():
                    contador = contador + 1
                    res.append(public)
    
            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                opção = int(input("Escolha o número do artigo escolhido: "))
                for i, artigo in enumerate(res):
                    if i == opção - 1:
                        return artigo

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo com o título "{título}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurar1CLI(databank)

        elif chave == 2:
            nome = input("Insira os nomes dos autores: (Nota: Separe os nomes com vírgulas.) ")
            autores_nome = [autor.strip().lower() for autor in nome.split(",")]
            res = []

            for public in databank:
                if "authors" in public:
                    names = [author["name"].strip().lower() for author in public["authors"] if "name" in author]
                    if any(autor in names for autor in autores_nome):
                        res.append(public)

            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                opção = int(input("Escolha o número do artigo escolhido: "))
                for i, artigo in enumerate(res):
                    if i == opção - 1:
                        return artigo

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pelo(s) autor(es) "{autores_nome}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurar1CLI(databank)

    
        elif chave == 3:
            nome = input("Insira a afiliação: (Nota: Separe os nomes com pontos.) ")
            autores_afiliação = [autor.strip().lower() for autor in nome.split(".")]
            res = []

            for public in databank:
                if "authors" in public:
                    nomes_afiliacoes = [
                        aff.strip().lower()
                        for author in public["authors"]
                        if author.get("affiliation")
                        for aff in author["affiliation"].split(".")
                    ]
                    if any(autor in nomes_afiliacoes for autor in autores_afiliação):
                        res.append(public)

            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                opção = int(input("Escolha o número do artigo escolhido: "))
                for i, artigo in enumerate(res):
                    if i == opção - 1:
                        return artigo

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pela afiliação "{nome}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurar1CLI(databank)
    
        elif chave == 4:
            res = []
            data = input("Insira a data da publicação: (Nota: Insira a data no formado aaaa-mm-dd)")

            for public in databank:
                if "publish_date" in public and public["publish_date"] == data:
                    res.append(public)
            
            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                opção = int(input("Escolha o número do artigo escolhido: "))
                for i, artigo in enumerate(res):
                    if i == opção - 1:
                        return artigo

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pela data de publicação "{data}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurar1CLI(databank)
        
        elif chave == 5:
            nome = input("Insira as palavras-chave: ")
            keywords_nome = [keyword.strip().lower() for keyword in nome.split(",")]
            res = []

            for public in databank:
                if "keywords" in public:
                    keywords_public = [keyword.strip().lower() for keyword in public['keywords'].split(",")]
                    if any(keyword in keywords_public for keyword in keywords_nome):
                        res.append(public)

            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                opção = int(input("Escolha o número do artigo escolhido: "))
                for i, artigo in enumerate(res):
                    if i == opção - 1:
                        return artigo

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo com a afiliação "{nome}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurar1CLI(databank)

    def atualizarCLI(public):
        public = procurar1CLI(databank)
        num = int(input ("""Escolha a informação que pretende atualizar?
                            1) Título
                            2) Autores
                            3) Afiliação
                            4) Data de publicação
                            5) Palavras-chave
                            """))
        
        if num == 1:
            if "title" in public:
                título = input("Introduza o novo título do artigo: ")
                public["title"] = título
        
        if num == 2:
            if "authors" in public:
                autores = []
                i = 1
                while i <= num:
                    nome = input(f"Introduza o nome do autor {i}/{num}: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
                    afiliação = input(f"Introduza a afiliação do autor {nome}: (Nota: Caso a publicação não tenha este parâmetro, faça 'Enter')")
                    autor = {"name": nome, "affiliation": afiliação}
                    autor_sem_vazios = {chave: valor for chave, valor in autor.items() if valor}
                    autores.append(autor_sem_vazios)
                    i = i + 1
                public["authors"] = autores
        
        if num == 3:
            if "authors" in public:
                for autor in public["authors"]:
                    afiliação = input(f"""Introduza a afiliação do autor "{autor["name"]}": """)
                    orcid = input(f"""Introduza o orcid do autor "{autor["name"]}": """)
                    autor["affiliation"] = afiliação
                    autor["orcid"] = orcid

        if num == 4:
            if "publish_date" in public:
                data = input("Introduza a nova data de publicação do artigo: (Nota: escreva a data no formato aaaa-mm-dd)")
                public["publish_date"] = data
        
        if num == 5:
            if "keywords" in public:
                palavras_chave = input("Introduza as novas palavras-chave do artigo: (Nota: Separe as palavras com um '.')")
                public["keywords"] = palavras_chave

        return public


    #CONSULTA DE PUBLICAÇÕES
    def procurarCLI(databank):
        chave = int(input ("""Escolha o filtro que pretende utilizar para procurar o artigo?
                            1) Título
                            2) Autores
                            3) Afiliação
                            4) Data de publicação
                            5) Palavras-chave
                            """))
        
        if chave == 1:
            res = []
            título = input("Insira o título do artigo: ")
            contador = 0
            
            for public in databank:
                if "title" in public and título.lower() in public['title'].lower():
                    contador = contador + 1
                    res.append(public)
    
            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                exportacao_parcialCLI(res)

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pelo título "{título}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurarCLI()

        elif chave == 2:
            nome = input("Insira os nomes dos autores: (Nota: Separe os nomes com vírgulas.)")
            res = []
            autores_nome = [autor.strip().lower() for autor in nome.split(",")]

            for public in databank:
                if "authors" in public:
                    names = "".join(author["name"].replace(" ", "").lower() for author in public["authors"] if "name" in author)
                    if any(autor in names for autor in autores_nome):
                        res.append(public)

            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                exportacao_parcialCLI(res)
            
            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pelo(s) autor(es) "{autores_nome}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurarCLI(databank)

        elif chave == 3:
            nome = input("Insira a afiliação: ")
            res = []

            for public in databank:
                if "authors" in public:
                    for autor in public["authors"]:
                        if "affiliation" in autor and autor["affiliation"].lower().split(".") == nome.lower().split(","):
                            res.append(public)
            
            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                exportacao_parcialCLI(res)

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pelo título "{título}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurarCLI()
    
        elif chave == 4:
            res = []
            data = input("Insira a data da publicação: (Nota: Insira a data no formado aaaa-mm-dd)")

            for public in databank:
                if "publish_date" in public and public["publish_date"] == data:
                    res.append(public)
            
            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                exportacao_parcialCLI(res)

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo pela data de publicação "{data}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurarCLI(databank) 
        
        elif chave == 5:
            nome = input("Insira as palavras-chave: ")
            keywords_nome = [keyword.strip().lower() for keyword in nome.split(",")]
            res = []

            for public in databank:
                if "keywords" in public:
                    keywords_public = [keyword.strip().lower() for keyword in public['keywords'].split(",")]
                    if any(keyword in keywords_public for keyword in keywords_nome):
                        res.append(public)

            if res != []:
                for i, artigo in enumerate(res):
                    print(f"Artigo {i+1}")
                    extensoCLI(artigo)
                exportacao_parcialCLI(res)

            elif res == []:
                print(f"""Não foi encontrado nenhum artigo com a afiliação "{nome}".""")
                res = input("Deseja voltar a procurar? (s/n) ")
                if res == ("s"):
                    procurarCLI(databank)

    #EXPORTAÇÃO PARCIAL DE DADOS
    def exportacao_parcialCLI(res):
        opção = input(("Deseja exportar os resultados desta pesquisa) (s/n)"))
        if opção == "s":
            exportarCLI(res)
        elif opção == "n":
            print("Os resultados não foram exportados.")

    #EXPORTAR DADOS
    def exportarCLI(databank):
        print("Exportação de dados")
        fnome = input("Insira o nome do ficheiro: ")
        data = input("Insira a localização do ficheiro: ")
        if not fnome.endswith(".json"):
            fnome += ".json"
        filename = os.path.join(data, fnome)
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(databank, file, indent=4, ensure_ascii=False)
                print(f"Os resultados foram exportados para o ficheiro {fnome} com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar os dados: {e}")

    #APAGAR UMA PUBLICAÇÃO
    def apagarCLI(databank):
        public = procurar1CLI(databank)
        opção = input("Tem a certeza que deseja apagar esta publicação? (s/n)")
        print(public)
        if opção == "s":
            databank.remove(public)
            print("A publicação foi apagada com sucesso!")
        elif opção == "n":
            print("A publicação não foi apagada.")

    def analiseauthorCLI(databank):
        freq = {}
        for public in databank:
            for author in public["authors"]:
                name = author["name"]
            
                if name in freq:
                    freq[name] += 1
                else:
                    freq[name] = 1 

        writers = sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))
        authors = [key for key, value in writers]
        print("")
        print("Autores ordenados por frequência:", authors)

        autor = input("Deseja ver as Publicações de que autor?").strip()
        listofPubs = []

        for public in databank:
            for author in public["authors"]:
                name = author["name"]
                if name.lower() == autor.lower():
                    listofPubs.append(public)
        
        print(f"As Publicações por {autor} :")
        print("")
        for pub in listofPubs:
            extensoCLI(pub)
        return

    def analisekeywordCLI(biglist):
        skeywords = {}

        for public in biglist:
            if "keywords" in public:
                unfiltered = public["keywords"].split(",")
                for wordy in unfiltered:
                    for word in wordy.split("/"):
                        word = word.strip() 
                        if word in skeywords:
                            skeywords[word] += 1
                        else:
                            skeywords[word] = 1

        dickeywords = dict(sorted(skeywords.items(), key=lambda pair: pair[1], reverse=True))
        print("Palavras-chave ordenadas por frequência:", dickeywords)

        keyword = input("Insira uma Palavra-chave: ").strip()
        listofpub = []

        for public in biglist:
            if "keywords" in public:
                unfiltered = public["keywords"].split(",")
                for wordy in unfiltered:
                    for word in wordy.split("/"): 
                        if word.strip() == keyword:
                            listofpub.append(public)

        print("Publicações encontradas:")
        print("")
        
        for pub in listofpub:
            extensoCLI(pub)
            
        return

    #RELATÓRIO DE ESTATÍSTICAS
    def estatis_menuCLI():
        print("""\nSelecione uma opção: \n1. Distribuição de publicações por ano \n2. Distribuição de publicações por mês em um ano \n3. Top 20 autores por número de publicações \n4. Publicações por um autor específico ao longo dos anos \n5. Top 20 palavras-chave \n6. Palavras-chave mais frequentes por ano. \n0. Sair""")
        return
    def yearlyDistrubCLI(biglist):
        dic={}
        for public in biglist:
            
            if "publish_date" in public:
                #fulldate = public['publish_date']
                date = public['publish_date'][0:4]
                if date in dic:
                    dic[date] += 1
                else:
                    dic[date] = 1
        dicti = dict(sorted(dic.items()))
        x = list(dicti.keys())
        y = list(dicti.values())
        plt.bar(x, y, color='blue')
        plt.yticks([50,100, 150])
        plt.xticks(rotation=45)
        plt.title("Distribuição de Publicações por Ano")
        plt.xlabel("Anos")
        plt.ylabel("Numeros de Publicações")
        plt.show()
        return

    def pubDISmesPanoCLI(biglist):
        year = int(input("Escolhe um ano:"))
        gragh={}
        month = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sept",10:"Oct", 11:"Nov", 12:"Dec"}

        for public in biglist:
            if "publish_date" in public:
                strdate = public["publish_date"]
                date_part = strdate.split("—")[0].strip()
                try:
                    datefrm = datetime.strptime(date_part, "%Y-%m-%d")
                    if datefrm.year == year:
                        if month[datefrm.month] in gragh:
                            gragh[month[datefrm.month]] += 1
                        else:
                            gragh[month[datefrm.month]] = 1
                except ValueError:
                    print(f"Invalid date format found: {strdate}.")
        legragh = dict(sorted(gragh.items(), key= lambda x: list(month.values()).index(x[0])))
        x = list(legragh.keys())
        y = list(legragh.values())
        plt.bar(x, y, color='pink')
        plt.yticks([5, 10, 15])
        plt.title(f"Distribuição de Publicações por mês de {year}")
        plt.xlabel("Meses")
        plt.ylabel("Numeros de Publicações")
        plt.show()
        return 

    def dis20pubporArthorCLI(biglist):
        leauthor = {}
        for public in biglist:
            for autor in public["authors"]:                
                    if autor["name"] in leauthor:
                        leauthor[autor["name"]] += 1
                    else:
                        leauthor[autor["name"]] = 1

        almostd = sorted(leauthor.items(), key = lambda pair: pair[1], reverse=True)
        theauthor = dict(almostd[:20])
        x = list(theauthor.keys())
        y = list(theauthor.values())
        plt.bar(x, y, color='grey')
        plt.yticks([5, 10, 15, 20, 25, 30, 35, 40])
        plt.xticks(rotation=45, ha="right", fontsize=9)
        plt.tight_layout()    
        plt.title("Distribuição de Publicações por Autor")
        plt.xlabel("Autor")
        plt.ylabel("Numeros de Publicações")
        plt.show()
        return

    def disPUBarthorPerYearCLI(biglist):
        pubyear = {}
        authorname=input("Escolhe um autor")
        for public in biglist:
            for autor in public["authors"]:
                if autor["name"].lower()== authorname.lower():
                    if "publish_date" in public:
                        pday = datetime.strptime(public["publish_date"],"%Y-%m-%d")
                        if pday.year in pubyear:
                            pubyear[pday.year] += 1
                        else:
                            pubyear[pday.year] = 1
        pubpyear = dict(sorted(pubyear.items()))
        x = list(pubpyear.keys())
        y = list(pubpyear.values())
        plt.xticks(x)
        plt.yticks(y)
        plt.bar(x, y, color='gold')
        plt.title(f"Distribuição de Publicação de {authorname} por Ano")
        plt.xlabel("Anos")
        plt.ylabel("Numeros de Publicações")
        plt.show()
        return

    def dis20KeyWordCLI(biglist):
        lekeywords = {}
        for public in biglist:       
            if "keywords" in public:
                keyword = public["keywords"].split(",")
                for word in keyword:
                    subwd = word.split("/")
                    for wd in subwd:
                        if wd in lekeywords:
                            lekeywords[wd] += 1
                        else:
                            lekeywords[wd] = 1           

        yettocome = sorted(lekeywords.items(), key = lambda pair: pair[1], reverse=True)
        thekeywords = dict(yettocome[:20])
        x = list(thekeywords.keys())
        y = list(thekeywords.values())
        plt.bar(x, y, color='green')
        plt.yticks([10, 50, 100, 300])
        plt.xticks(rotation=45, ha="right", fontsize=9)
        plt.tight_layout()
        plt.title("Distribuição de Frequencias das top 20 Palavras-chaves")
        plt.xlabel("Palavras-chaves")
        plt.ylabel("Frequência")
        plt.show()
        return

    def disKWperANOCLI(biglist):
        kwpyear = {}
        for public in biglist:
            valid = True  
            if "publish_date" not in public or "keywords" not in public:
                valid = False
            if valid:
                try:
                    leyear = datetime.strptime(public["publish_date"], "%Y-%m-%d").year
                except ValueError:
                    print(f"Invalid date format in: {public['publish_date']}")
                    valid = False
            if valid:  
                kword = public["keywords"].split(",")
                for wrd in kword:
                    for keyword in wrd.split("/"):
                        if leyear not in kwpyear:
                            kwpyear[leyear] = {}
                        kwpyear[leyear][keyword] = kwpyear[leyear].get(keyword, 0) + 1

        freqword = []
        keywordpyear = {}
        keywordy = dict(sorted(kwpyear.items(), key=lambda pair: pair[0]))
        for leyear in keywordy:
            lelist = sorted(keywordy[leyear].items(), key=lambda pair: pair[1], reverse=True)
            freqword.append(lelist[0][0])
            keywordpyear[leyear] = lelist[0][1]
        x = list(keywordpyear.keys())
        y = list(keywordpyear.values())
        bars = plt.bar(x, y, color='indigo')
        plt.yticks(y)
        plt.xticks(x)
        plt.tight_layout()
        for bar, word in zip(bars, freqword):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, word, ha='center', va='bottom', fontsize=10)
        plt.title("Distribuição das Top Palavras-Chave por Ano")
        plt.xlabel("Ano")
        plt.ylabel("Frequencia da Palavra-chave")
        plt.show()
        return


    def rel_EstatisCLI(databank):
        while True:
            estatis_menuCLI()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                yearlyDistrubCLI(databank)
            elif opcao == "2":
                pubDISmesPanoCLI(databank)
            elif opcao == "3":
                dis20pubporArthorCLI(databank)
            elif opcao == "4":
                disPUBarthorPerYearCLI(databank)
            elif opcao == "5":
                dis20KeyWordCLI(databank)
            elif opcao == "6":
                disKWperANOCLI(databank)
            elif opcao == "0":
                print("Encerrando o programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    #ANÁLISE DE PUBLICAÇÕES POR AUTOR
    def analiseauthorCLI(databank):
        freq = {}
        for public in databank:
            for author in public["authors"]:
                name = author["name"]
            
                if name in freq:
                    freq[name] += 1
                else:
                    freq[name] = 1 

        writers = sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))
        authors = [key for key, value in writers]
        print("")
        print("Autores ordenados por frequência:", authors)

        autor = input("Deseja ver as Publicações de que autor?").strip()
        listofPubs = []

        for public in databank:
            for author in public["authors"]:
                name = author["name"]
                if name.lower() == autor.lower():
                    listofPubs.append(public)
        
        print(f"As Publicações por {autor} :")
        print("")
        for pub in listofPubs:
            extensoCLI(pub)
        return

    #ANÁLISE DE PUBLICAÇÕES POR PALAVRAS-CHAVE
    def analisekeywordCLI(biglist):
        skeywords = {}

        for public in biglist:
            if "keywords" in public:
                unfiltered = public["keywords"].split(",")
                for wordy in unfiltered:
                    for word in wordy.split("/"):
                        word = word.strip() 
                        if word in skeywords:
                            skeywords[word] += 1
                        else:
                            skeywords[word] = 1

        dickeywords = dict(sorted(skeywords.items(), key=lambda pair: pair[1], reverse=True))
        print("Palavras-chave ordenadas por frequência:", dickeywords)

        keyword = input("Insira uma Palavra-chave: ").strip()
        listofpub = []

        for public in biglist:
            if "keywords" in public:
                unfiltered = public["keywords"].split(",")
                for wordy in unfiltered:
                    for word in wordy.split("/"): 
                        if word.strip() == keyword:
                            listofpub.append(public)

        print("Publicações encontradas:")
        print("")
        
        for pub in listofpub:
            extensoCLI(pub)
        return

    ficheiroCLI()
    return

first_menu()