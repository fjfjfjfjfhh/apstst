# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:11:47 2022

@author: denilson aguiar
"""

from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from bs4 import BeautifulSoup

# agora -> webdriver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import asyncio
import telebot
from kivymd.toast.kivytoast.kivytoast import toast
from firebase import firebase
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label
import datetime
from kivy.clock import Clock
from packaging import version

Window.size = (400, 580)
click_branco = '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[2]/div'
click_add_valor = '//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div/div[1]/input'
click_valor = '//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div/div[1]/input'
click_confirmar_aposta = '//*[@id="roulette-controller"]/div[1]/div[3]/button'

Link_blaze = 'https://blaze.com/pt/games/double'
click_vermelho = '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[1]/div'
click_preto = '//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[3]/div'

click_entrar_blaze = '//*[@id="header"]/div/div[2]/div/div/div[1]/a'
click_email = '//*[@id="auth-modal"]/div/form/div[1]/div/input'
click_senha = '//*[@id="auth-modal"]/div/form/div[2]/div/input'
click_entrar = '//*[@id="auth-modal"]/div/form/div[4]/button'
api_key = '5692708316:AAHRwyOuDr_wGmdP8ygbe5T_uoZ1mdIxYLo'
############################################################3
automatico = 1
sequencia_automatica = 0
jogue_vermelho_automatico = 0
jogue_preto_automatico = 0
##############################################################

br = 0
br1 = 0
br2 = 0
g0 = 0
g1 = 0
g2 = 0

########################################################
analisar = 0
gale_atual = 0
analisar_open = 0
resultsDouble = []
######################################################3
margemacerto = 50
margemPRETO = 0
margemVERNELHO = 0
margemBRANCO = 0
margemaerror = 0


resultados_porcentagem = 1
branco_prc = 1
preto_prc = 1
vermelho_prc = 1
porc = "porc"
preto_porc = 1
verme_porc = 1
branco_porc = 10


# https://colab.research.google.com/drive/1b9gMzs6XAtxCtahxei4N0fWZk7xiPlVw?usp=sharing#scrollTo=Z1pqOWngHY0O

global logged_in_user
logged_in_user = ""

global ativar_sequencia
ativar_sequencia = 0
ultimo_numero = 1998
count = 0
sw_started = False
sw_seconds = 0
global finalcor
finalcor = "vazio"
global valornumcor
valornumcor = "vazio"
global progresso
progresso = 0
global nav
global entrada_confirmada_agora
entrada_confirmada_agora = "AGUARDANDO ENTRADA"
ultimo_numero = 5
popSound = None



botizao = 0
vitoriag0 = 0
vitoriag1 = 0
vitoriag2 = 0

brancog0 = 0
brancog1 = 0
brancog2 = 0

derrota_vermelho = 0
derrota_preto = 0
derrota_geral = 0

brancosaindo = 0
redsaindo = 0
blacksaindo = 0

QNT_ENTRADA = 0
ativar_loop = 0
sequencia_4_ligado = 0
sequencia_7_ligado = 0
sequencia_9_ligado = 0
sequencia_mega_ligado = 0
banca = 0
btn = 0
tempo_de_parar_vitoria = 0
tempo_de_parar_derrota = 0
resulROOL = "AGUARDANDO GIROS"
ativar = 0

status_on = "AGUANDANDO ATIVAÇÃO"
class LoginScreen(Screen):

    def validate_user(self):
        global ativar_sequencia
        global logged_in_user
        global uname
        from firebase import firebase
        firebase = firebase.FirebaseApplication("https://blazege-9e853-default-rtdb.firebaseio.com/")
        resultados = firebase.get("blazege-9e853-default-rtdb/Usuarios_blaze", '')
        uname = self.ids.uname_input.text
        pword = self.ids.pword_input.text
        is_found = (1, 2)
        self.ids.uname_input.text = "denya@gmail"
        self.ids.pword_input.text = "setset"
        if is_found:
            logged_in_user = uname + pword
            for i in resultados.keys():
                # toast("Aguardando...")
                if resultados[i]['email:'] == uname:
                    if resultados[i]['senha'] == pword:
                        toast(f"Bem vindo {uname}")
                        ativar_sequencia += 1
                        print("Usuario:" + uname + " e " + "Senha:" + pword + " Correto")
                        self.parent.current = "Tela_PrincipalScreen"
                        print(ativar_sequencia)

                if resultados[i]['email:'] != uname:
                    if resultados[i]['senha'] != pword:
                        print("Usuario:" + uname + " e " + "Senha:" + pword + " incorreto")
                        toast("usuario ou senha incorreto!")


class Tela_PrincipalScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.nome = Label()
        self.add_widget(self.nome)
        self.task = Clock.schedule_interval(self.chamandonome, 0.1)

    def chamandonome(self, dt):
        global logged_in_user
        global uname
        try:
            self.ids.nome.text = uname
        except:
            self.ids.nome.text = "Bem vindo"

    def chamando_tela_megablaze(self, text):
        global ativar_sequencia
        ativar_sequencia = 2
        global btn
        global nome_sequencia
        btn = 3
        print(f"valor do botao na chamada  {btn}")
        self.parent.current = 'tela_mega_digitos'
        print(ativar_sequencia)
        toast("Padrão blaze")

    def chamando_tela_3(self, text):
        global ativar_sequencia
        ativar_sequencia = 2
        global btn
        global nome_sequencia
        btn = 4
        print(f"valor do botao na chamada  {btn}")
        self.parent.current = 'tela_mega_digitos'
        print(ativar_sequencia)
        nome_sequencia = "Padrão 4 Sequencias"
        toast("Padrão de 4 sequencias")

    def jogada_padrao_sete(self):
        global ativar_sequencia
        ativar_sequencia = 2
        global btn
        global nome_sequencia
        btn = 7
        print(f"valor do botao na chamada  {btn}")
        self.parent.current = 'tela_mega_digitos'
        nome_sequencia = "Padrão 7 Sequencias"
        # print("chamando tela submenu de class  tela_submenuScreen")
        print(ativar_sequencia)
        toast("Padrão 7 sequencias")

    def jogada_padrao_nove(self):
        global ativar_sequencia
        ativar_sequencia = 2
        global btn
        global nome_sequencia
        btn = 9
        print(f"valor do botao na chamada  {btn}")
        self.parent.current = 'tela_mega_digitos'
        # print("chamando tela submenu de class  tela_submenuScreen")
        print(ativar_sequencia)
        toast("Padrão 9 sequencias")
        nome_sequencia = "Padrão 9 Sequencias"
        toast("em breve...")
        # toast("em breve sera adicionado o padrao de 7 sequencias...")

    def jogada_personalizada(self):
        global logged_in_user
        global nome_sequencia
        nome_sequencia = "Padrão Sequencias Personalizada"
        toast("em desevolvimento, aguarde...")


class ButtonFocus(MDRaisedButton):
    ...



###############PARA mega DIGITOS#################################
class tela_mega_digitos(Screen):
    sw_started = False
    sw_seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label()
        self.add_widget(self.label)
        self.task = Clock.schedule_interval(self.update_label, 0.1)

        self.resultado = Label()
        self.add_widget(self.resultado)
        self.task = Clock.schedule_interval(self.resultado_final, 0.1)

        self.resultado_cor = Label()
        self.add_widget(self.resultado_cor)
        self.task = Clock.schedule_interval(self.resultado_cor_sequencia, 0.1)

        self.entradas_disponiveis = Label()
        self.add_widget(self.entradas_disponiveis)

        self.giro = Label()
        self.add_widget(self.giro)

        self.acertividade = Label()
        self.add_widget(self.acertividade)

        self.acertividade1 = Label()
        self.add_widget(self.acertividade1)

        self.acertividade2 = Label()
        self.add_widget(self.acertividade2)

        self.ligadesliga = Label()
        self.add_widget(self.ligadesliga)
        self.task = Clock.schedule_interval(self.entradas_confirmadas, 0.1)

        self.qualsequencia = Label()
        self.add_widget(self.qualsequencia)
        self.task = Clock.schedule_interval(self.chamandonome, 0.1)


    def chamandonome(self, dt):
        global nome_sequencia
        try:
            self.ids.qualsequencia.text = nome_sequencia
        except:
            self.ids.qualsequencia.text = "Bem vindo"

    def entradas_confirmadas(self, dt):
        global entrada_confirmada_agora
        global resulROOL
        global resultados_porcentagem
        global branco_prc
        global preto_prc
        global vermelho_prc
        global porc
        global preto_porc
        global verme_porc
        global branco_porc
        global status_on

        self.ids.ligadesliga.text = status_on
        self.ids.entradas_disponiveis.text = entrada_confirmada_agora
        self.ids.giro.text = resulROOL
        self.ids.acertividade.text = f" VERMELHO:{float(verme_porc):,.2f}%"
        self.ids.acertividade1.text = f"PRETO:{float(preto_porc):,.2f}%"
        self.ids.acertividade2.text = f"BRANCO:{float(branco_porc):,.2f}%"


    def resultado_final(self, dt):
        global ultimo_numero
        global valor_de_saida
        global finalcor
        global progresso
        try:
            if valor_de_saida == 1:
                progresso = 100
                self.ids.resultado.text = ultimo_numero
                valor_de_saida = 0
                toast("Novo Resultado")
                if progresso == 100:
                    progresso = 0
                else:
                    "calma"

            elif valor_de_saida != 1:
                self.resultado.text = ultimo_numero
                self.ids.progress_bar.value = progresso
                progresso += 0.45
            else:
                'faço nada'
        except:
            self.ids.resultado.text = "Aguardando"

    def resultado_cor_sequencia(self, dt):
        global ultimo_numero
        global valor_de_saida
        global finalcor
        global valornumcor
        global resulROOL

        global resultados_porcentagem
        global branco_prc
        global preto_prc
        global vermelho_prc

        def qualnum(ultimo_numero):
            return int(ultimo_numero)

        def qualcor(ultimo_numero):
            try:
                if qualnum(ultimo_numero) <= 7:
                    self.ids.resultado.text = ultimo_numero
                    self.ids.resultado_cor.text = "VERMELHO"
                    return 'V'
                elif qualnum(ultimo_numero) > 7:
                    self.ids.resultado.text = ultimo_numero
                    self.ids.resultado_cor.text = "PRETO"
                    return 'P'
                elif qualnum(ultimo_numero) == 0:
                    self.ids.resultado.text = ultimo_numero
                    self.ids.resultado_cor.text = "Branco"
                    return 'B'
                elif qualnum(ultimo_numero) <= 1:
                    self.ids.resultado.text = ultimo_numero
                    self.ids.resultado_cor.text = "Branco"
                    return 'B'
                elif resulROOL == "Blaze Girou 0!":
                    self.ids.resultado.text = "0"
                    self.ids.resultado_cor.text = "BRANCO"
                    return 'B'

                elif resulROOL == "Blaze Girou 1!":
                    self.ids.resultado.text = "1"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 2!":
                    self.ids.resultado.text = "2"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"
                elif resulROOL == "Blaze Girou 3!":
                    self.ids.resultado.text = "3"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 4!":
                    self.ids.resultado.text = "4"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 5!":
                    self.ids.resultado.text = "5"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 6!":
                    self.ids.resultado.text = "6"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 7!":
                    self.ids.resultado.text = "7"
                    self.ids.resultado_cor.text = "VERMELHO"
                    return "vermelho_prc"

                elif resulROOL == "Blaze Girou 8!":
                    self.ids.resultado.text = "8"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"
                elif resulROOL == "Blaze Girou 9!":
                    self.ids.resultado.text = "9"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"

                elif resulROOL == "Blaze Girou 10!":
                    self.ids.resultado.text = "10"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"
                elif resulROOL == "Blaze Girou 11!":
                    self.ids.resultado.text = "11"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"

                elif resulROOL == "Blaze Girou 12!":
                    self.ids.resultado.text = "12"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"

                elif resulROOL == "Blaze Girou 13!":
                    self.ids.resultado.text = "13"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"


                elif resulROOL == "Blaze Girou 14!":
                    self.ids.resultado.text = "14"
                    self.ids.resultado_cor.text = "PRETO"
                    return "preto_prc"
                else:
                    "branco_prc"
            except:
                "ERROR"

        qualcor(ultimo_numero)

    def update_label(self, nap):
        now = datetime.datetime.now()
        if self.sw_started:
            self.sw_seconds += nap

        m, s = divmod(self.sw_seconds, 60)
        self.ids.stopwatch.text = ('%02d:[size=40]%02d[/size]' % (int(m), int(s)))

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def start_stop(self):
        global ativar_sequencia
        self.ids.start_stop.text = 'Iniciar' if self.sw_started else 'Parar'
        self.sw_started = not self.sw_started
        ativar_sequencia = 7
        print(ativar_sequencia)

    def reset(self):

        if self.sw_started:
            self.root.ids.start_stop.text = 'Iniciar'
            self.sw_started = True

        self.sw_seconds = 0

    def barra_de_progresso(self, progresso):
        if progresso == 100:
            progresso = 0
        else:
            progresso += 10
        self.ids.progress_bar.value = progresso

    def desativar_jogo_mega_digitos(self):
        global entry
        global ativar_sequencia
        global status_on
        ativar_sequencia = 7
        print(ativar_sequencia)
        status_on = "APOSTAS DESATIVADAS"
        toast("Desativando Aposta")

    def abrir_card(self):
        global ativar
        global status_on
        if ativar == 0:
            print(f"ativando e desa {ativar}")
            toast("faça suas apostas")
            self.ids.start_stop.text = 'desativar analise' if self.sw_started else '.....'
            status_on = "AGUARDANDO JOGO"
            self.add_widget(tela_aposta_mega())
        if ativar == 2:
            self.ids.start_stop.text = 'desativar analise' if self.sw_started else 'Jogar'
            print(f"ativando e desa {ativar}")
            status_on = "AGUARDANDO APOSTAS"
            toast("desligando Analises")
            ativar = 0

    def historico(self):
        global historio_acesso
        if btn == 3:
            historio_acesso = 10
            print(f"historico  valor de: {historio_acesso} com btn de {btn}")
            self.parent.current = "Tela_Historico"
        if btn == 9:
            historio_acesso = 9
            print(f"historico  valor de: {historio_acesso} com btn de {btn}")
            self.parent.current = "Tela_Historico"
        if btn == 7:
            historio_acesso = 7
            print(f"historico  valor de: {historio_acesso} com btn de {btn}")
            self.parent.current = "Tela_Historico"
        if btn == 4:
            historio_acesso = 4
            print(f"historico  valor de: {historio_acesso} com btn de {btn}")
            self.parent.current = "Tela_Historico"


    def abrir_card_dinheiro(self):
        self.add_widget(dinheiro_apostado())

############### PARA GERAL DIGITOS ##############################
class tela_aposta_mega(MDCard):
    sw_started = False
    sw_seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def fechar(self):
        global ativar
        ativar = 2
        print(f"ativando e desa {ativar}")
        status_on = "ANALISANDO SEM APOSTAR"
        self.parent.remove_widget(self)

    def fechar_btn(self):
        global ativar
        ativar = 2
        print(f"ativando e desa {ativar}")
        status_on = "ANALISANDO SEM APOSTAR"
        self.parent.remove_widget(self)

    def jogar_sequencia_mega(self):
        global ativar_sequencia
        global entry
        global g0
        global g1
        global g2
        global branco
        global br
        global br1
        global br2
        global nav
        global historico
        global ativar_loop
        global btn
        global tempo_de_parar
        global tempo_percas
        global ativar
        global status_on
        ativar = 2
        historico = 1
        print(historico)
        print(f"loop {ativar_loop}")

        tempo_de_parar = self.ids.stop_input.text
        tempo_percas = self.ids.stop1_input.text

        g0 = self.ids.G0_input.text
        g1 = self.ids.G1_input.text
        g2 = self.ids.G2_input.text
        br = self.ids.BRANCO_input.text
        br1 = self.ids.BRANCO_inputG1.text
        br2 = self.ids.BRANCO_inputG2.text

        self.ids.stop_input.text = ""
        self.ids.stop1_input.text = ""

        self.ids.G0_input.text = ""
        self.ids.G1_input.text = ""
        self.ids.G2_input.text = ""
        self.ids.BRANCO_input.text = ""
        self.ids.BRANCO_inputG1.text = ""
        self.ids.BRANCO_inputG2.text = ""
        # self.parent.current = popuop()
        print(f"valor do botao {btn}")
        if btn == 3:
            ativar_sequencia = 10
            status_on = "ANALISANDO JOGO"
            print(f"valor sec {ativar_sequencia}")
            print(f"valor do botao dentro do sec10 {btn}")
            if ativar_sequencia == 10:
                status_on = "APOSTAS ATIVADAS"
                ativar_loop = 1
                print(f"loop {ativar_loop}")
                self.ids.jogar_sequencia_mega.text = 'Iniciar' if self.sw_started else 'Apostado'
                toast("iniciando jogo, não saia das analises..")
                #toast(f"Começando o jogo!\napostas G0: {g0},00 \nG1:{g1},00 \nG2: {g2},00 \nbranco_prc G0: {br},00 \nbranco_prc G1: {br1},00 \nbranco_prc \nG2: {br2},00\nPARANDO COM: \nSTOPLOSS:2 LOSS\nSTOPWIN:{tempo_de_parar} ")
                self.parent.remove_widget(self)

        if btn == 4:
            ativar_sequencia = 4
            status_on = "ANALISANDO JOGO"
            print(f"valor sec {ativar_sequencia}")
            print(f"valor do botao dentro do sec10 {btn}")
            if ativar_sequencia == 4:
                ativar_loop = 1
                status_on = "APOSTAS ATIVADAS"
                print(f"loop {ativar_loop}")
                self.ids.jogar_sequencia_mega.text = 'Iniciar' if self.sw_started else 'Apostado'
                toast("iniciando jogo, não saia das analises..")
                # print(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 branco_prc: {br},00")
                #toast(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 \nbranco_prc G0: {br},00 branco_prc G1: {br1},00 branco_prc G2: {br2},00")
                # self.parent.current = 'notifica'
                self.parent.remove_widget(self)

        if btn == 7:
            ativar_sequencia = 6
            status_on = "ANALISANDO JOGO"
            print(f"valor sec {ativar_sequencia}")
            print(f"valor do botao dentro do sec10 {btn}")
            if ativar_sequencia == 6:
                ativar_loop = 1
                status_on = "APOSTAS ATIVADAS"
                print(f"loop {ativar_loop}")
                self.ids.jogar_sequencia_mega.text = 'Iniciar' if self.sw_started else 'Apostado'
                toast("iniciando jogo, não saia das analises..")
                # print(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 branco_prc: {br},00")
                #toast(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 \nbranco_prc G0: {br},00 branco_prc G1: {br1},00 branco_prc G2: {br2},00")
                # self.parent.current = 'notifica'
                self.parent.remove_widget(self)

        if btn == 9:
            ativar_sequencia = 9
            status_on = "ANALISANDO JOGO"
            print(f"valor sec {ativar_sequencia}")
            print(f"valor do botao dentro do sec10 {btn}")
            if ativar_sequencia == 9:
                ativar_loop = 1
                status_on = "APOSTAS ATIVADAS"
                print(f"loop {ativar_loop}")
                self.ids.jogar_sequencia_mega.text = 'Iniciar' if self.sw_started else 'Apostado'
                toast("iniciando jogo, não saia das analises..")
                # print(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 branco_prc: {br},00")
                #toast(f"Começando o jogo com apostas G0: {g0},00 G1:{g1},00 G2: {g2},00 \nbranco_prc G0: {br},00 branco_prc G1: {br1},00 branco_prc G2: {br2},00")
                # self.parent.current = 'notifica'
                self.parent.remove_widget(self)

    def desativar_jogo_mega_digitos(self):
        global ativar
        ativar = 2
        status_on = "APOSTAS DESATIVADAS"
        print(f"ativando e desa {ativar}")
        self.parent.remove_widget(self)


class Historico(Screen):
    sw_started = False
    sw_seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.VITORIAG0 = Label()
        self.add_widget(self.VITORIAG0)

        self.VITORIAG1 = Label()
        self.add_widget(self.VITORIAG1)

        self.VITORIAG2 = Label()
        self.add_widget(self.VITORIAG2)

        self.VITORIABRANCOG0 = Label()
        self.add_widget(self.VITORIABRANCOG0)

        self.VITORIABRANCOG1 = Label()
        self.add_widget(self.VITORIABRANCOG1)

        self.VITORIABRANCOG2 = Label()
        self.add_widget(self.VITORIABRANCOG2)

        self.LOSSRED = Label()
        self.add_widget(self.LOSSRED)

        self.LOSSBLACK = Label()
        self.add_widget(self.LOSSBLACK)

        self.LOSSGERAL = Label()
        self.add_widget(self.LOSSGERAL)

        self.VERMELHOSAINDO = Label()
        self.add_widget(self.VERMELHOSAINDO)

        self.PRETOSAINDO = Label()
        self.add_widget(self.PRETOSAINDO)

        self.BRANCOSAINDO = Label()
        self.add_widget(self.BRANCOSAINDO)

        self.ENTRADAS = Label()
        self.add_widget(self.ENTRADAS)

        self.task = Clock.schedule_interval(self.entradas_confirmadas, 5)

    def entradas_confirmadas(self, dt):
        global vitoriag0
        global vitoriag1
        global vitoriag2

        global brancog0
        global brancog1
        global brancog2

        global derrota_vermelho
        global derrota_preto
        global derrota_geral

        global redsaindo
        global blacksaindo
        global brancosaindo

        global QNT_ENTRADA
        global wins

        wins = str(vitoriag0) + str(vitoriag1) + str(vitoriag2)
        self.ids.VITORIAG0.text = str(vitoriag0)
        self.ids.VITORIAG1.text = str(vitoriag1)
        self.ids.VITORIAG2.text = str(vitoriag2)

        self.ids.VITORIABRANCOG0.text = str(brancog0)
        self.ids.VITORIABRANCOG1.text = str(brancog1)
        self.ids.VITORIABRANCOG2.text = str(brancog2)

        self.ids.LOSSRED.text = str(derrota_vermelho)
        self.ids.LOSSBLACK.text = str(derrota_preto)
        self.ids.LOSSGERAL.text = str(derrota_geral)

        self.ids.VERMELHOSAINDO.text = str(redsaindo)
        self.ids.PRETOSAINDO.text = str(blacksaindo)
        self.ids.BRANCOSAINDO.text = str(brancosaindo)

        self.ids.ENTRADAS.text = str(QNT_ENTRADA)




    def fechar_card_7(self):
        global historio_acesso
        if historio_acesso == 4:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 4 com o valor de: {historio_acesso}")
        if historio_acesso == 5:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 5 com o valor de: {historio_acesso}")
        if historio_acesso == 6:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 6 com o valor de: {historio_acesso}")
        if historio_acesso == 7:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 7 com o valor de: {historio_acesso}")
        if historio_acesso == 9:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 9 com o valor de: {historio_acesso}")
        if historio_acesso == 10:
            self.parent.current = "tela_mega_digitos"
            print(f"historico de tela 10 com o valor de: {historio_acesso}")
        else:
            "blz"

    def abrir_card_bot(self):
        self.add_widget(botizao_infor())


class botizao_infor(Screen):
    sw_started = False
    sw_seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def USAR_BOT(self):
        global botizao
        global api_key
        global chat_id_gp
        global caixa_bot
        botizao = 1
        print(f"to aqui {botizao}")
        #self.ids.abrir_card_bot = 'fkhu' if self.sw_started else 'DESLIGAR'
        chat_id_gp = self.ids.chat_id_input.text
        api_key = self.ids.api_key_input.text

        self.ids.chat_id_input.text = "5599575472"
        self.ids.api_key_input.text = "5431250074:AAF3Mz6YLhApPrRnxgr7N6gXKBzq7tgdjWE"
        caixa_bot = 2
        print(api_key)
        print(chat_id_gp)
        if caixa_bot == 2:
            try:
                bot = telebot.TeleBot(token=api_key)
                bot.send_message(chat_id=chat_id_gp, text="BOT INICIADO COM SUCESSO")
                toast("BOT INICIADO COM SUCESSO")
                #self.ids.abrir_card_bot = 'USAR BOT' if self.sw_started else 'DESLIGAR'
                self.parent.remove_widget(self)
                caixa_bot = 3
                print(f"caixa {caixa_bot}")
            except:
                print("chave bot error")
                toast("ERROR NA CHAVE OU KEY")








    def desativar_caixa_bot(self):
        self.parent.remove_widget(self)


class dinheiro_apostado(Screen):
    sw_started = False
    sw_seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.VALOR_G0 = Label()
        self.add_widget(self.VALOR_G0)

        self.VALOR_G1 = Label()
        self.add_widget(self.VALOR_G1)

        self.VALOR_G2 = Label()
        self.add_widget(self.VALOR_G2)

        self.VALOR_G0 = Label()
        self.add_widget(self.VALOR_G0)

        self.VITORIAS_GERAL = Label()
        self.add_widget(self.VITORIAS_GERAL)
        self.task = Clock.schedule_interval(self.dinheiro_confirmado, 2)

        self.VITORIAS_GERAL = Label()
        self.add_widget(self.VITORIAS_GERAL)
        self.task = Clock.schedule_interval(self.bancareal, 2)

    def bancareal(self, dt):
        global banca
        try:
            banca = navegador.find_element(
                By.XPATH, '//*[@id="header"]/div/div[2]/div/div[1]/div/a/div/div/div[1]').text
        except:
            "vazio"
        self.ids.bancablaze.text = str(banca)

    def dinheiro_confirmado(self, dt):
        global br
        global br1
        global br2
        global g0
        global g1
        global g2
        global vitoriag0
        global vitoriag1
        global vitoriag2

        TODASWINS = str(vitoriag0 + vitoriag1 + vitoriag2)
        self.ids.VALOR_G0.text = str(g0)
        self.ids.VALOR_G1.text = str(g1)
        self.ids.VALOR_G2.text = str(g2)

        self.ids.VALOR_BRANCOG0.text = str(br)
        self.ids.VALOR_BRANCOG1.text = str(br1)
        self.ids.VALOR_BRANCOG2.text = str(br2)

        self.ids.VITORIAS_GERAL.text = f"VITORIAS: {str(TODASWINS)}"

        if TODASWINS == 1:
            print("vitoria batemos meta")

    def USAR_BOT(self):
        global botizao
        global api_key
        global chat_id_gp
        global caixa_bot
        botizao = 1
        print(f"to aqui {botizao}")
        self.ids.botizaoauau = 'USAR BOT' if self.sw_started else 'DESLIGAR'
        chat_id_gp = self.ids.chat_id_input.text
        api_key = self.ids.api_key_input.text

        self.ids.chat_id_input.text = "5599575472"
        self.ids.api_key_input.text = "5431250074:AAF3Mz6YLhApPrRnxgr7N6gXKBzq7tgdjWE"

        caixa_bot = 2
        print(api_key)
        print(chat_id_gp)
        if caixa_bot == 2:
            try:
                bot = telebot.TeleBot(token=api_key)
                bot.send_message(chat_id=chat_id_gp, text="BOT INICIADO COM SUCESSO")
                toast("BOT INICIADO COM SUCESSO")
                self.parent.remove_widget(self)
                caixa_bot = 3
                print(f"caixa {caixa_bot}")
            except:
                print("chave bot error")
                toast("ERROR NA CHAVE OU KEY")

    def desativar_caixa_dinheiro(self):
        self.parent.remove_widget(self)


class tela_splas_pop(Screen):
    pass


class error404(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MegaBlazer(MDApp):
    sw_started = False
    sw_seconds = 0

    def build(self):
        global sm
        sm = Builder.load_file('main.kv')

        self.theme_cls.theme_style = "Dark"

        return sm

    def on_start(self):

        Clock.schedule_once(self.login, 10)

    def login(*args):
        global nav
        global navegador
        global resultados

        try:
            print("iniciando web")
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
            nav.get('https://blaze.com/pt/games/double')

            from firebase import firebase
            firebase = firebase.FirebaseApplication("https://blazege-9e853-default-rtdb.firebaseio.com/")
            resultados = firebase.get("blazege-9e853-default-rtdb/Usuarios_blaze", '')

            # abri o navegador para apostar automatico
            navegador = Service(ChromeDriverManager().install())
            navegador = webdriver.Chrome(service=navegador)
            navegador.get(Link_blaze)
            print("carregou web")
            sm.current = "login_screen"
        except:
            sm.current = "error404net"
            "Não foi possivel conectar a internet, verifique se sua rede esta ativa."

    async def kivyCoro(self):  # This is the method that's gonna launch your kivy app
        await self.async_run(async_lib='asyncio')

        print('todos os asyc fechados...')
        global navegador
        global nav
        navegador.close()
        nav.close()
        print('fechamos os navegadores...')

        try:
            bot = telebot.TeleBot(token=api_key)
            bot.send_message(chat_id=chat_id_gp,
                             text=f"Desligando... foram ({QNT_ENTRADA}) entradas \n•RESULTADOS:\n•VITORIAS: ({vitoriag0})\n•LOSS: ({derrota_geral}) \n🎲➖ (insta:@denny_braga1998) ➖🎲\n\n")
        except:
            "bot desligado"

    async def GlobalTask(self):

        while True:
            global ativar_sequencia
            global resulROOL
            global entry
            global g0
            global g1
            global g2
            global br
            global br1
            global br2
            global ultimo_numero
            global valor_de_saida
            global analisar_open
            global automatico
            global sequencia_automatica
            global jogue_vermelho_automatico
            global jogue_preto_automatico
            global navegador
            global nav
            global progresso
            global entrada_confirmada_agora
            global entrada_confirmada
            global vitoriag0

            global brancosaindo
            global redsaindo
            global blacksaindo

            global QNT_ENTRADA
            global caixa_bot
            global ativar_loop

            global sequencia_4_ligado
            global sequencia_7_ligado
            global sequencia_9_ligado
            global sequencia_mega_ligado

            global resultados_porcentagem
            global branco_prc
            global preto_prc
            global vermelho_prc
            global preto_porc
            global verme_porc
            global branco_porc

            global stopwin
            global stoploss
            global tempo_de_parar
            global tempo_percas
            global tempo_de_parar_vitoria
            global tempo_de_parar_derrota

            analisar = 0
            gale_atual = 0
            analisar_open = 0
            resultsDouble = []

            await asyncio.sleep(.1)

 #########################################################################################################3
            while True:
                if ativar_loop == 1:
                    while True:

                        def qualnum(valornumcor):
                            if valornumcor == '0':
                                return 0

                            if valornumcor == '1':
                                return 1

                            if valornumcor == '2':
                                return 2

                            if valornumcor == '3':
                                return 3

                            if valornumcor == '4':
                                return 4

                            if valornumcor == '5':
                                return 5

                            if valornumcor == '6':
                                return 6

                            if valornumcor == '7':
                                return 7

                            if valornumcor == '8':
                                return 8

                            if valornumcor == '9':
                                return 9

                            if valornumcor == '10':
                                return 10

                            if valornumcor == '11':
                                return 11

                            if valornumcor == '12':
                                return 12

                            if valornumcor == '13':
                                return 13

                            if valornumcor == '14':
                                return 14

                        def qualcor(valornumcor):
                            global resultados_porcentagem
                            global branco_prc
                            global preto_prc
                            global vermelho_prc
                            if valornumcor == '0':
                                branco_prc += 1
                                return 'B'

                            if valornumcor == '1':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '2':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '3':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '4':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '5':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '6':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '7':
                                vermelho_prc += 1
                                return 'V'

                            if valornumcor == '8':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '9':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '10':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '11':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '12':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '13':
                                preto_prc += 1
                                return 'P'

                            if valornumcor == '14':
                                preto_prc += 1
                                return 'P'

                        try:
                            resulROOL = nav.find_element(
                                By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
                        except Exception:
                            print('ERRO 404')

                        analisar_open = 0
                        if resulROOL == 'Girando...':
                            analisar_open = 1
                            print(resulROOL)
                            entrada_confirmada_agora = "AGUARDANDO ANALISE.."
                            await asyncio.sleep(13)
                            c = nav.page_source
                            resultsDouble.clear()
                            soup = BeautifulSoup(c, 'html.parser')
                            go = soup.find('div', class_="entries main")
                            entries_div = soup.find("div", {"class": "entries main"})
                            entrys = entries_div.find_all("div", {"class": "roulette-tile"})
                            entrys = entrys[0:1]
                            box_list = []
                            for entry in entrys:
                                if 'red' in entry.__str__():
                                    box_list.append(('VERMELHO', entry.text))
                                    valor_de_saida = 1
                                    progresso = 100
                                    redsaindo += 1


                                elif 'black' in entry.__str__():
                                    box_list.append(('PRETO', entry.text))
                                    valor_de_saida = 1
                                    progresso = 100
                                    blacksaindo += 1
                                else:
                                    box_list.append(('BRANCO', '0'))
                                    print(*box_list, sep=' ')
                                    valor_de_saida = 1
                                    brancosaindo += 1
                                    branco_prc += 1
                                    progresso = 100

                            if valor_de_saida == 1:
                                try:
                                    ultimo_numero = entry.text
                                    print(f"Ultimo numero:{ultimo_numero}")

                                except:
                                    print('sem valor de saida')

                            else:
                                'continua'


                            if resultados_porcentagem == 1:
                                saidas_total = preto_prc + vermelho_prc + branco_prc
                                if preto_prc >= 0:
                                    verme_porc = float(preto_prc / saidas_total) * 100
                                    if verme_porc >= 100.00:
                                        verme_porc = 75.00

                                if vermelho_prc >= 1:
                                    preto_porc = float(vermelho_prc / saidas_total) * 100
                                    if preto_porc >= 100.00:
                                        preto_porc = 75.00

                                if branco_prc >= 1:
                                    branco_porc = (saidas_total) / branco_prc
                                await asyncio.sleep(.1)

                            for i in go:
                                if i.getText():
                                    resultsDouble.append(i.getText())
                                else:
                                    resultsDouble.append('0')

                            resultsDouble = resultsDouble[:-1]

                            if analisar_open == 1:
                                default = resultsDouble
                                mapeando = map(qualnum, default)
                                mapeando2 = map(qualcor, default)
                                finalnum = list(mapeando)
                                finalcor = list(mapeando2)

                                if ativar_sequencia == 4:
                                    print(f"entrei na sec {ativar_sequencia}")
                                    sequencia_4_ligado = 1

                                    if sequencia_4_ligado == 1:
                                        try:
                                            async def CHECK_VERSION(default):
                                                global analisar
                                                global gale_atual
                                                global automatico
                                                global sequencia_automatica
                                                global jogue_vermelho_automatico
                                                global jogue_preto_automatico
                                                global navegador
                                                global entrada_confirmada_agora

                                                global vitoriag0
                                                global vitoriag1
                                                global vitoriag2

                                                global brancog0
                                                global brancog1
                                                global brancog2

                                                global br
                                                global br1
                                                global br2

                                                global derrota_vermelho
                                                global derrota_preto
                                                global derrota_geral

                                                global QNT_ENTRADA
                                                global ultimo_numero

                                                global wins
                                                global stopwin
                                                global stoploss
                                                global tempo_percas
                                                global tempo_de_parar
                                                global tempo_de_parar_vitoria
                                                global tempo_de_parar_derrota

                                                ####################################################################################################
                                                # CHAMADA DE SEQUENCIA JOGUE NO:

                                                if analisar == 0:
                                                    # 04. SEQUENCIA JOGUE VERMELHO[CODIGO01]:
                                                    if default[0:5] == ['P', 'P', 'P', 'P', 'V']:
                                                        analisar = 1
                                                        gale_atual = 0
                                                        print("jogue VERMELHO")
                                                        # APOSTAR NO VERMELHO elemento para clicar no preto_prc
                                                        await asyncio.sleep(1)
                                                        navegador.find_element(By.XPATH, click_vermelho).click()
                                                        await asyncio.sleep(1)
                                                        # elemento para clicar na caixa de add valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # clique adicionando money para apostar
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            g0)
                                                        await asyncio.sleep(2)
                                                        # elemento para confirmar entrada na cor
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        await asyncio.sleep(1)
                                                        # confirmando branco_prc
                                                        navegador.find_element(By.XPATH, click_branco).click()
                                                        await asyncio.sleep(1)
                                                        # clicando no imput valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # adicionando valor no branco_prc reais
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            br)
                                                        await asyncio.sleep(1)
                                                        # clique para apostar
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        print("joguei vermelho_prc  auto")
                                                        entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO VERMELHO COD:04"
                                                        QNT_ENTRADA += 1
                                                        toast(f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                        try:
                                                            bot = telebot.TeleBot(token=api_key)
                                                            bot.send_message(chat_id=chat_id_gp,
                                                                             text="🚨Estratégia Confirmada🚨 \n \n Jogue:    🟥🟥🟥 \n Proteja:  ⬜⬜⬜ \n\n🎲➖( CODIGO:04 )➖🎲  \n ")

                                                        except:
                                                            "bot desligado"
                                                        return
                                                    # 03. SEQUENCIA JOGUE PRETO[CODIGO03]:
                                                    if default[0:5] == ['V', 'P', 'V', 'P', 'V']:
                                                            print("jogue preto_prc")
                                                            gale_atual = 0
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            gale_atual = 0
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return
                                                    # 01. SEQUENCIA JOGUE PRETO[CODIGO04]:
                                                    if default[0:5] == ['V', 'V', 'V', 'V', 'P']:
                                                            gale_atual = 0
                                                            print("jogue preto_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return


                                                ###################################################################################################

                                                if analisar == 1:
                                                    await asyncio.sleep(.5)
                                                    if gale_atual == 0:
                                                        # 04. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:5] == ['P', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:01"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:5] == ['B', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:01"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:5] == ['V', 'V', 'V', 'V', 'V']:

                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei preto_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:01"
                                                            print("indo para g1 continue no preto_prc")
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                            # 02. VITORIA SEM GALE [CODIGO02]

                                                        # 03. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:5] == ['P', 'V', 'P', 'V', 'P']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:03"
                                                                print("ganhou sem gale")
                                                                vitoriag0 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        if default[0:5] == ['B', 'V', 'P', 'V', 'P']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:03"
                                                                print("ganhou sem gale BRANCO")
                                                                vitoriag0 += 1
                                                                brancog0 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_percas += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        if default[0:5] == ['V', 'V', 'P', 'V', 'P']:

                                                                await asyncio.sleep(1)
                                                                navegador.find_element(By.XPATH, click_preto).click()
                                                                await asyncio.sleep(1)
                                                                # elemento para clicar na caixa de add valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # clique adicionando money para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(g1)
                                                                await asyncio.sleep(2)
                                                                # elemento para confirmar entrada na cor
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                # confirmando branco_prc
                                                                navegador.find_element(By.XPATH, click_branco).click()
                                                                await asyncio.sleep(1)
                                                                # clicando no imput valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(0.5)
                                                                # adicionando valor no branco_prc reais
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(br1)
                                                                await asyncio.sleep(1)
                                                                # clique para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                print("joguei preto_prc auto g1")
                                                                entrada_confirmada_agora = "INDO PARA O GALE 01 COD:03"
                                                                print("indo para g1 continue no preto_prc")
                                                                gale_atual = 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                                # 02. VITORIA SEM GALE [CODIGO02]

                                                        # 04. VITORIA SEM GALE [CODIGO04]
                                                        if default[0:5] == ['V', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO SEM GALE! COD:04"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(🟥🟥🟥)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:5] == ['B', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:04"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:INDO PARA GALE1
                                                        if default[0:5] == ['P', 'P', 'P', 'P', 'P']:

                                                            print("indo para g1 continue no vermelho_prc")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei vermelho_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:04"
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################

                                                    if gale_atual == 1:
                                                            await asyncio.sleep(.5)
                                                            # 04. VITORIA COM GALE 1[CODIGO01]
                                                            if default[0:5] == ['P', 'V', 'V', 'V', 'V']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:01"
                                                                print("VITORIA COM GALE 1")
                                                                vitoriag1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            if default[0:5] == ['B', 'V', 'V', 'V', 'V']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:01"
                                                                print("VITORIA COM GALE 1")
                                                                vitoriag1 += 1
                                                                brancog1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            # 04. DERROTA[CODIGO01]:INDO PARA GALE2
                                                            if default[0:5] == ['V', 'V', 'V', 'V', 'V']:
                                                                print("joguei preto_prc auto g2")
                                                                # APOSTAR NO VERMELHO elemento para clicar
                                                                await asyncio.sleep(1)
                                                                navegador.find_element(By.XPATH, click_preto).click()
                                                                await asyncio.sleep(1)
                                                                # elemento para clicar na caixa de add valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # clique adicionando money para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(g2)
                                                                await asyncio.sleep(2)
                                                                # elemento para confirmar entrada na cor
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                # confirmando branco_prc
                                                                navegador.find_element(By.XPATH, click_branco).click()
                                                                await asyncio.sleep(1)
                                                                # clicando no imput valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # adicionando valor no branco_prc reais
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(br2)
                                                                await asyncio.sleep(1)
                                                                # clique para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)

                                                                entrada_confirmada_agora = "INDO PARA O GALE 02 COD:01"
                                                                print("indo para g2 continue no preto_prc")
                                                                gale_atual = 2
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                            # 03. VITORIA COM GALE 1[CODIGO01]'P', 'V', 'V', 'P'
                                                            if default[0:5] == ['P', 'V', 'V', 'P', 'V']:
                                                                    analisar = 0
                                                                    entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:03"
                                                                    print("VITORIA COM GALE 1")
                                                                    vitoriag1 += 1
                                                                    tempo_de_parar_vitoria += 1
                                                                    #tempo_de_parar -= 1

                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                    except:
                                                                        "bot desligado"
                                                                    return
                                                            if default[0:5] == ['B', 'V', 'V', 'P', 'V']:
                                                                    analisar = 0
                                                                    gale_atual = 0
                                                                    entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:03"
                                                                    print("VITORIA COM GALE 1")
                                                                    vitoriag1 += 1
                                                                    brancog1 += 1
                                                                    tempo_de_parar_vitoria += 1
                                                                   # tempo_de_parar -= 1

                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                    except:
                                                                        "bot desligado"
                                                                    return
                                                            # 03. DERROTA[CODIGO01]:INDO PARA GALE2
                                                            if default[0:5] == ['V', 'V', 'V', 'P', 'V']:
                                                                    print("joguei preto_prc auto g2")
                                                                    # APOSTAR NO VERMELHO elemento para clicar
                                                                    await asyncio.sleep(1)
                                                                    navegador.find_element(By.XPATH, click_preto).click()
                                                                    await asyncio.sleep(1)
                                                                    # elemento para clicar na caixa de add valor
                                                                    navegador.find_element(By.XPATH, click_valor).click()
                                                                    await asyncio.sleep(1)
                                                                    # clique adicionando money para apostar
                                                                    navegador.find_element(By.XPATH,
                                                                                           click_add_valor).send_keys(g2)
                                                                    await asyncio.sleep(2)
                                                                    # elemento para confirmar entrada na cor
                                                                    navegador.find_element(By.XPATH,
                                                                                           click_confirmar_aposta).click()
                                                                    await asyncio.sleep(1)
                                                                    # confirmando branco_prc
                                                                    navegador.find_element(By.XPATH, click_branco).click()
                                                                    await asyncio.sleep(1)
                                                                    # clicando no imput valor
                                                                    navegador.find_element(By.XPATH, click_valor).click()
                                                                    await asyncio.sleep(1)
                                                                    # adicionando valor no branco_prc reais
                                                                    navegador.find_element(By.XPATH,
                                                                                           click_add_valor).send_keys(br2)
                                                                    await asyncio.sleep(1)
                                                                    # clique para apostar
                                                                    navegador.find_element(By.XPATH,
                                                                                           click_confirmar_aposta).click()
                                                                    await asyncio.sleep(1)

                                                                    entrada_confirmada_agora = "INDO PARA O GALE 02 COD:03"
                                                                    print("indo para g2 continue no preto_prc")
                                                                    gale_atual = 2
                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                                    except:
                                                                        "bot desligado"
                                                                    return

                                                            # 01. VITORIA COM GALE [CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                            if default[0:5] == ['V', 'P', 'P', 'P', 'P']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 1! COD:04"
                                                                print("VITORIA COM GALE 1")
                                                                vitoriag1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                            if default[0:5] == ['B', 'P', 'P', 'P', 'P']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:04"
                                                                print("VITORIA COM GALE 1 BRANCO")
                                                                vitoriag1 += 1
                                                                brancog1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            # 01. DERROTA[CODIGO04]:INDO PARA GALE2
                                                            if default[0:5] == ['P', 'P', 'P', 'P', 'P']:
                                                                print("indo para g2 continue no vermelho_prc")
                                                                await asyncio.sleep(1)
                                                                # APOSTAR NO VERMELHO elemento para clicar
                                                                navegador.find_element(By.XPATH, click_vermelho).click()
                                                                await asyncio.sleep(1)
                                                                # elemento para clicar na caixa de add valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # clique adicionando money para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(g2)
                                                                await asyncio.sleep(2)
                                                                # elemento para confirmar entrada na cor
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                # confirmando branco_prc
                                                                navegador.find_element(By.XPATH, click_branco).click()
                                                                await asyncio.sleep(1)
                                                                # clicando no imput valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # adicionando valor no branco_prc reais
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(br2)
                                                                await asyncio.sleep(1)
                                                                # clique para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                print("joguei vermelho_prc auto g2")
                                                                entrada_confirmada_agora = "INDO PARA O GALE 02 COD:04"
                                                                gale_atual = 2
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                        #########################################################################################################
                                                    if gale_atual == 2:
                                                            await asyncio.sleep(.5)
                                                            # 01. VITORIA COM GALE 2[CODIGO01]'V', 'V', 'V', 'V', 'V'
                                                            if default[0:5] == ['P', 'V', 'V', 'V', 'V']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 2! COD:01"
                                                                print("VITORIA COM GALE 2")
                                                                vitoriag2 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"

                                                                return
                                                            if default[0:5] == ['B', 'V', 'V', 'V', 'V']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:01"
                                                                print("VITORIA COM GALE 2 BRANCO")
                                                                vitoriag2 += 1
                                                                brancog2 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            # 01. DERROTA[CODIGO01]:PERDEMOS
                                                            if default[0:5] == ['V', 'V', 'V', 'V', 'V']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                tempo_de_parar_derrota += 1
                                                                entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:01"
                                                                print("perdeu totalmente ")
                                                                derrota_vermelho += 1
                                                                derrota_geral += 1
                                                                #tempo_percas -= 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                            # 03. VITORIA COM GALE 2[CODIGO01]'V', 'V', 'V', 'P'
                                                            if default[0:5] == ['P', 'V', 'V', 'V', 'P']:
                                                                    analisar = 0
                                                                    entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 2! COD:03"
                                                                    print("VITORIA COM GALE 2")
                                                                    vitoriag2 += 1
                                                                    tempo_de_parar_vitoria += 1
                                                                    # tempo_de_parar -= 1

                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬛⬛⬛)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                    except:
                                                                        "bot desligado"

                                                                    return
                                                            if default[0:5] == ['B', 'V', 'V', 'V', 'P']:
                                                                    analisar = 0
                                                                    gale_atual = 0
                                                                    entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:03"
                                                                    print("VITORIA COM GALE 2 BRANCO")
                                                                    vitoriag2 += 1
                                                                    brancog2 += 1
                                                                    tempo_de_parar_vitoria += 1
                                                                    # tempo_de_parar -= 1

                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                    except:
                                                                        "bot desligado"
                                                                    return
                                                            # 03. DERROTA[CODIGO01]:PERDEMOS
                                                            if default[0:5] == ['V', 'V', 'V', 'V', 'P']:
                                                                    analisar = 0
                                                                    gale_atual = 0
                                                                    tempo_de_parar_derrota += 1
                                                                    entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:01"
                                                                    print("perdeu totalmente ")
                                                                    derrota_vermelho += 1
                                                                    derrota_geral += 1
                                                                    # tempo_percas -= 1
                                                                    try:
                                                                        bot = telebot.TeleBot(token=api_key)
                                                                        bot.send_message(chat_id=chat_id_gp,
                                                                                         text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                                    except:
                                                                        "bot desligado"
                                                                    return


                                                            # 04. VITORIA COM GALE 2[CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                            if default[0:4] == ['V', 'P', 'P', 'P', 'P']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                #tempo_de_parar -= 1
                                                                entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 2! COD:04"
                                                                print("VITORIA COM GALE 2")
                                                                vitoriag2 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            if default[0:4] == ['B', 'P', 'P', 'P', 'P']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                #tempo_de_parar -= 1
                                                                tempo_de_parar_vitoria += 1
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:02"
                                                                print("VITORIA COM GALE 2 BRANCO")
                                                                vitoriag2 += 1
                                                                brancog2 += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                            # 04. DERROTA[CODIGO04]:PERDEMOS
                                                            if default[0:4] == ['P', 'P', 'P', 'P', 'P']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                tempo_de_parar_derrota += 1
                                                                #tempo_percas -= 1
                                                                entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:04"
                                                                print("perdeu totalmente ")
                                                                derrota_preto += 1
                                                                derrota_geral += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return


                                                            ###############################################################################################


                                                await asyncio.sleep(1)

                                            await CHECK_VERSION(finalcor)

                                            if tempo_de_parar_vitoria == float(tempo_de_parar):
                                                toast("Meta Concluida com sucesso")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de win: {tempo_de_parar}\nparando apostas...")

                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text= f"Meta atingiada!: Vitorias: {tempo_de_parar}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break


                                                await asyncio.sleep(.1)

                                            if tempo_de_parar_derrota == float(tempo_percas):
                                                toast("Limite de perca Atingido, lamentamos!")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de percas: {tempo_percas}\nparando apostas...")
                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text= f"Limite de percas atingido!: Loss: {tempo_percas}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break


                                                await asyncio.sleep(.1)

                                            #print(f"sequencia de x - 3:{default}")
                                            if tempo_de_parar_vitoria != float(tempo_de_parar):
                                                falta_qnt_parar = int(tempo_de_parar) - int(tempo_de_parar_vitoria)
                                                print(f"Meta configurada: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")
                                                toast(f"Meta configurada para: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")


                                            await asyncio.sleep(1)
                                        except:
                                            try:
                                                bot = telebot.TeleBot(token=api_key)
                                                entrada_confirmada_agora = f"CONEXÃO COM A INTERNET TURBULENTA, RECOMENDAMOS REINICIAR O JOGO."
                                                print(f"Algum error x - 2:{finalcor}")
                                                bot.send_message(chat_id=chat_id_gp, text="SEQUENCIA MEGA: \n alto consumo de memoria, isso esta afetando o desempenho, reinicie o programa")
                                            except: ""
                                    if sequencia_4_ligado != 1:
                                        print("desligado 4")
                                        try:
                                            bot = telebot.TeleBot(token=api_key)
                                            bot.send_message(chat_id=chat_id_gp,text="DESATIVANDO SEQUENCIA 4: \n OBS: Quando trocamos a sequencia é recomendado reiniciar o Programa para evitar Bugs e consumo de memoria desnecessario.")
                                        except:
                                            "..."

                                if ativar_sequencia == 6:
                                    print(f"entrei na sec {ativar_sequencia}")
                                    sequencia_7_ligado = 1

                                    if sequencia_7_ligado == 1:
                                        try:
                                            async def CHECK_VERSION(default):
                                                global analisar
                                                global gale_atual
                                                global automatico
                                                global sequencia_automatica
                                                global jogue_vermelho_automatico
                                                global jogue_preto_automatico
                                                global navegador
                                                global entrada_confirmada_agora

                                                global vitoriag0
                                                global vitoriag1
                                                global vitoriag2

                                                global brancog0
                                                global brancog1
                                                global brancog2

                                                global br
                                                global br1
                                                global br2

                                                global derrota_vermelho
                                                global derrota_preto
                                                global derrota_geral

                                                global QNT_ENTRADA
                                                global ultimo_numero

                                                global wins
                                                global stopwin
                                                global stoploss
                                                global tempo_percas
                                                global tempo_de_parar
                                                global tempo_de_parar_vitoria
                                                global tempo_de_parar_derrota

                                                ####################################################################################################
                                                # CHAMADA DE SEQUENCIA JOGUE NO:

                                                if analisar == 0:
                                                    # 04. SEQUENCIA JOGUE VERMELHO[CODIGO01]:
                                                    if default[0:8] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'V']:
                                                        analisar = 1
                                                        gale_atual = 0
                                                        print("jogue VERMELHO")
                                                        # APOSTAR NO VERMELHO elemento para clicar no preto_prc
                                                        await asyncio.sleep(1)
                                                        navegador.find_element(By.XPATH, click_vermelho).click()
                                                        await asyncio.sleep(1)
                                                        # elemento para clicar na caixa de add valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # clique adicionando money para apostar
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            g0)
                                                        await asyncio.sleep(2)
                                                        # elemento para confirmar entrada na cor
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        await asyncio.sleep(1)
                                                        # confirmando branco_prc
                                                        navegador.find_element(By.XPATH, click_branco).click()
                                                        await asyncio.sleep(1)
                                                        # clicando no imput valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # adicionando valor no branco_prc reais
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            br)
                                                        await asyncio.sleep(1)
                                                        # clique para apostar
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        print("joguei vermelho_prc  auto")
                                                        entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO VERMELHO COD:04"
                                                        QNT_ENTRADA += 1
                                                        toast(f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                        try:
                                                            bot = telebot.TeleBot(token=api_key)
                                                            bot.send_message(chat_id=chat_id_gp,
                                                                             text="🚨Estratégia Confirmada🚨 \n \n Jogue:    🟥🟥🟥 \n Proteja:  ⬜⬜⬜ \n\n🎲➖( CODIGO:04 )➖🎲  \n ")

                                                        except:
                                                            "bot desligado"
                                                        return
                                                    # 01. SEQUENCIA JOGUE PRETO[CODIGO04]:
                                                    if default[0:8] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'P']:
                                                            gale_atual = 0
                                                            print("jogue preto_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return


                                                ###################################################################################################

                                                if analisar == 1:
                                                    await asyncio.sleep(.5)
                                                    if gale_atual == 0:
                                                        # 04. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:8] == ['P', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:01"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:8] == ['B', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:01"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:8] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:

                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei preto_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:01"
                                                            print("indo para g1 continue no preto_prc")
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                            # 02. VITORIA SEM GALE [CODIGO02]


                                                        # 01. VITORIA SEM GALE [CODIGO04]
                                                        if default[0:8] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO SEM GALE! COD:04"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(🟥🟥🟥)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:8] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:04"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:INDO PARA GALE1
                                                        if default[0:8] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:

                                                            print("indo para g1 continue no vermelho_prc")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei vermelho_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:04"
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################

                                                    if gale_atual == 1:
                                                        await asyncio.sleep(.5)
                                                        # 04. VITORIA COM GALE 1[CODIGO01]
                                                        if default[0:8] == ['P', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:8] == ['B', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO01]:INDO PARA GALE2
                                                        if default[0:8] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            print("joguei preto_prc auto g2")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)

                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:01"
                                                            print("indo para g2 continue no preto_prc")
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return



                                                        # 01. VITORIA COM GALE [CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:8] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                        if default[0:8] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1 BRANCO")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO04]:INDO PARA GALE2
                                                        if default[0:8] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            print("indo para g2 continue no vermelho_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            print("joguei vermelho_prc auto g2")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:04"
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################
                                                    if gale_atual == 2:
                                                        await asyncio.sleep(.5)
                                                        # 01. VITORIA COM GALE 2[CODIGO01]'V', 'V', 'V', 'V', 'V'
                                                        if default[0:8] == ['P', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"

                                                            return
                                                        if default[0:8] == ['B', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO01]:PERDEMOS
                                                        if default[0:8] == ['V','V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:01"
                                                            print("perdeu totalmente ")
                                                            derrota_vermelho += 1
                                                            derrota_geral += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        # 04. VITORIA COM GALE 2[CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:8] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 2! COD:04"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            tempo_de_parar_vitoria += 1
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:02"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:PERDEMOS
                                                        if default[0:8] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            #tempo_percas -= 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:04"
                                                            print("perdeu totalmente ")
                                                            derrota_preto += 1
                                                            derrota_geral += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        ###############################################################################################


                                                await asyncio.sleep(1)

                                            await CHECK_VERSION(finalcor)

                                            if tempo_de_parar_vitoria == float(tempo_de_parar):
                                                toast("Meta Concluida com sucesso")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de win: {tempo_de_parar}\nparando apostas...")

                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Meta atingiada!: Vitorias: {tempo_de_parar}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            if tempo_de_parar_derrota == float(tempo_percas):
                                                toast("Limite de perca Atingido, lamentamos!")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de percas: {tempo_percas}\nparando apostas...")
                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Limite de percas atingido!: Loss: {tempo_percas}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            #print(f"sequencia de x - 3:{default}")
                                            if tempo_de_parar_vitoria != float(tempo_de_parar):
                                                falta_qnt_parar = int(tempo_de_parar) - int(tempo_de_parar_vitoria)
                                                print(f"Meta configurada: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")
                                                toast(f"Meta configurada para: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")

                                            await asyncio.sleep(1)
                                        except:
                                            try:
                                                bot = telebot.TeleBot(token=api_key)
                                                entrada_confirmada_agora = f"CONEXÃO COM A INTERNET TURBULENTA, RECOMENDAMOS REINICIAR O JOGO."
                                                print(f"Algum error x - 2:{finalcor}")
                                                bot.send_message(chat_id=chat_id_gp, text="SEQUENCIA 7 DIGITOS: \n alto consumo de memoria, isso esta afetando o desempenho, reinicie o programa")
                                            except: ""
                                    if sequencia_7_ligado != 1:
                                        print("desligado SEC 7")
                                        try:
                                            bot = telebot.TeleBot(token=api_key)
                                            bot.send_message(chat_id=chat_id_gp,text="DESATIVANDO 7 DIGITOS: \n OBS: Quando trocamos a sequencia é recomendado reiniciar o Programa para evitar Bugs e consumo de memoria desnecessario.")
                                        except:
                                            "..."

                                if ativar_sequencia == 9:
                                    print(f"entrei na sec {ativar_sequencia}")
                                    sequencia_9_ligado = 1

                                    if sequencia_9_ligado == 1:
                                        try:
                                            async def CHECK_VERSION(default):
                                                global analisar
                                                global gale_atual
                                                global automatico
                                                global sequencia_automatica
                                                global jogue_vermelho_automatico
                                                global jogue_preto_automatico
                                                global navegador
                                                global entrada_confirmada_agora

                                                global vitoriag0
                                                global vitoriag1
                                                global vitoriag2

                                                global brancog0
                                                global brancog1
                                                global brancog2

                                                global br
                                                global br1
                                                global br2

                                                global derrota_vermelho
                                                global derrota_preto
                                                global derrota_geral

                                                global QNT_ENTRADA
                                                global ultimo_numero

                                                global wins
                                                global stopwin
                                                global stoploss
                                                global tempo_percas
                                                global tempo_de_parar
                                                global tempo_de_parar_vitoria
                                                global tempo_de_parar_derrota

                                                ####################################################################################################
                                                # CHAMADA DE SEQUENCIA JOGUE NO:

                                                if analisar == 0:
                                                    # 04. SEQUENCIA JOGUE VERMELHO[CODIGO01]:
                                                    if default[0:10] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'V']:
                                                        analisar = 1
                                                        gale_atual = 0
                                                        print("jogue VERMELHO")
                                                        # APOSTAR NO VERMELHO elemento para clicar no preto_prc
                                                        await asyncio.sleep(1)
                                                        navegador.find_element(By.XPATH, click_vermelho).click()
                                                        await asyncio.sleep(1)
                                                        # elemento para clicar na caixa de add valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # clique adicionando money para apostar
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            g0)
                                                        await asyncio.sleep(2)
                                                        # elemento para confirmar entrada na cor
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        await asyncio.sleep(1)
                                                        # confirmando branco_prc
                                                        navegador.find_element(By.XPATH, click_branco).click()
                                                        await asyncio.sleep(1)
                                                        # clicando no imput valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # adicionando valor no branco_prc reais
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            br)
                                                        await asyncio.sleep(1)
                                                        # clique para apostar
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        print("joguei vermelho_prc  auto")
                                                        entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO VERMELHO COD:04"
                                                        QNT_ENTRADA += 1
                                                        toast(f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                        try:
                                                            bot = telebot.TeleBot(token=api_key)
                                                            bot.send_message(chat_id=chat_id_gp,
                                                                             text="🚨Estratégia Confirmada🚨 \n \n Jogue:    🟥🟥🟥 \n Proteja:  ⬜⬜⬜ \n\n🎲➖( CODIGO:04 )➖🎲  \n ")

                                                        except:
                                                            "bot desligado"
                                                        return
                                                    # 01. SEQUENCIA JOGUE PRETO[CODIGO04]:
                                                    if default[0:10] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'P']:
                                                            gale_atual = 0
                                                            print("jogue preto_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return


                                                ###################################################################################################

                                                if analisar == 1:
                                                    await asyncio.sleep(.5)
                                                    if gale_atual == 0:
                                                        # 04. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:10] == ['P', 'V', 'V',  'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:01"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:10] == ['B', 'V', 'V',  'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:01"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:10] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:

                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei preto_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:01"
                                                            print("indo para g1 continue no preto_prc")
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                            # 02. VITORIA SEM GALE [CODIGO02]


                                                        # 01. VITORIA SEM GALE [CODIGO04]
                                                        if default[0:10] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO SEM GALE! COD:04"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(🟥🟥🟥)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:10] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:04"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:INDO PARA GALE1
                                                        if default[0:10] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:

                                                            print("indo para g1 continue no vermelho_prc")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei vermelho_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:04"
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################

                                                    if gale_atual == 1:
                                                        await asyncio.sleep(.5)
                                                        # 04. VITORIA COM GALE 1[CODIGO01]
                                                        if default[0:10] == ['P', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:10] == ['B', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO01]:INDO PARA GALE2
                                                        if default[0:10] == ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            print("joguei preto_prc auto g2")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)

                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:01"
                                                            print("indo para g2 continue no preto_prc")
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return



                                                        # 01. VITORIA COM GALE [CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:10] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                        if default[0:10] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1 BRANCO")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO04]:INDO PARA GALE2
                                                        if default[0:10] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            print("indo para g2 continue no vermelho_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            print("joguei vermelho_prc auto g2")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:04"
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################
                                                    if gale_atual == 2:
                                                        await asyncio.sleep(.5)
                                                        # 01. VITORIA COM GALE 2[CODIGO01]'V', 'V', 'V', 'V', 'V'
                                                        if default[0:10] == ['P', 'V', 'V', 'V','V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"

                                                            return
                                                        if default[0:10] == ['B', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO01]:PERDEMOS
                                                        if default[0:10] == ['V','V', 'V','V', 'V', 'V', 'V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:01"
                                                            print("perdeu totalmente ")
                                                            derrota_vermelho += 1
                                                            derrota_geral += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        # 04. VITORIA COM GALE 2[CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:10] == ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 2! COD:04"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:10] == ['B', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            tempo_de_parar_vitoria += 1
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:02"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:PERDEMOS
                                                        if default[0:10] == ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            #tempo_percas -= 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:04"
                                                            print("perdeu totalmente ")
                                                            derrota_preto += 1
                                                            derrota_geral += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        ###############################################################################################


                                                await asyncio.sleep(1)

                                            await CHECK_VERSION(finalcor)

                                            if tempo_de_parar_vitoria == float(tempo_de_parar):
                                                toast("Meta Concluida com sucesso")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de win: {tempo_de_parar}\nparando apostas...")

                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Meta atingiada!: Vitorias: {tempo_de_parar}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            if tempo_de_parar_derrota == float(tempo_percas):
                                                toast("Limite de perca Atingido, lamentamos!")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                print(f"limite de percas: {tempo_percas}\nparando apostas...")
                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Limite de percas atingido!: Loss: {tempo_percas}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            #print(f"sequencia de x - 3:{default}")
                                            if tempo_de_parar_vitoria != float(tempo_de_parar):
                                                falta_qnt_parar = int(tempo_de_parar) - int(tempo_de_parar_vitoria)
                                                print(f"Meta configurada: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")
                                                toast(f"Meta configurada para: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")

                                            await asyncio.sleep(1)
                                        except:
                                            try:
                                                bot = telebot.TeleBot(token=api_key)
                                                entrada_confirmada_agora = f"CONEXÃO COM A INTERNET TURBULENTA, RECOMENDAMOS REINICIAR O JOGO."
                                                print(f"Algum error x - 9:{finalcor}")
                                                bot.send_message(chat_id=chat_id_gp, text="SEQUENCIA 9 DIGITOS: \n alto consumo de memoria, isso esta afetando o desempenho, reinicie o programa")
                                            except: ""
                                    if sequencia_7_ligado != 1:
                                        print("desligado SEC 7")
                                        try:
                                            bot = telebot.TeleBot(token=api_key)
                                            bot.send_message(chat_id=chat_id_gp,text="DESATIVANDO 9 DIGITOS: \n OBS: Quando trocamos a sequencia é recomendado reiniciar o Programa para evitar Bugs e consumo de memoria desnecessario.")
                                        except:
                                            "..."

                                if ativar_sequencia == 10:
                                    print(f"entrei na sec {ativar_sequencia}")
                                    sequencia_mega_ligado = 1

                                    if sequencia_mega_ligado == 1:
                                        try:
                                            async def CHECK_VERSION(default):
                                                global analisar
                                                global gale_atual
                                                global automatico
                                                global sequencia_automatica
                                                global jogue_vermelho_automatico
                                                global jogue_preto_automatico
                                                global navegador
                                                global entrada_confirmada_agora

                                                global vitoriag0
                                                global vitoriag1
                                                global vitoriag2

                                                global brancog0
                                                global brancog1
                                                global brancog2

                                                global br
                                                global br1
                                                global br2

                                                global derrota_vermelho
                                                global derrota_preto
                                                global derrota_geral

                                                global QNT_ENTRADA
                                                global ultimo_numero

                                                global wins
                                                global stopwin
                                                global stoploss
                                                global tempo_percas
                                                global tempo_de_parar
                                                global tempo_de_parar_vitoria
                                                global tempo_de_parar_derrota

                                                ####################################################################################################
                                                # CHAMADA DE SEQUENCIA JOGUE NO:

                                                if analisar == 0:
                                                    # 04. SEQUENCIA JOGUE VERMELHO[CODIGO01]:
                                                    if default[0:4] == ['P', 'P', 'P', 'V']:
                                                        analisar = 1
                                                        gale_atual = 0
                                                        print("jogue VERMELHO")
                                                        # APOSTAR NO VERMELHO elemento para clicar no preto_prc
                                                        await asyncio.sleep(1)
                                                        navegador.find_element(By.XPATH, click_vermelho).click()
                                                        await asyncio.sleep(1)
                                                        # elemento para clicar na caixa de add valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # clique adicionando money para apostar
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            g0)
                                                        await asyncio.sleep(2)
                                                        # elemento para confirmar entrada na cor
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        await asyncio.sleep(1)
                                                        # confirmando branco_prc
                                                        navegador.find_element(By.XPATH, click_branco).click()
                                                        await asyncio.sleep(1)
                                                        # clicando no imput valor
                                                        navegador.find_element(By.XPATH, click_valor).click()
                                                        await asyncio.sleep(1)
                                                        # adicionando valor no branco_prc reais
                                                        navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                            br)
                                                        await asyncio.sleep(1)
                                                        # clique para apostar
                                                        navegador.find_element(By.XPATH,
                                                                               click_confirmar_aposta).click()
                                                        print("joguei vermelho_prc  auto")
                                                        entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO VERMELHO COD:04"
                                                        QNT_ENTRADA += 1
                                                        toast(f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                        try:
                                                            bot = telebot.TeleBot(token=api_key)
                                                            bot.send_message(chat_id=chat_id_gp,
                                                                             text="🚨Estratégia Confirmada🚨 \n \n Jogue:    🟥🟥🟥 \n Proteja:  ⬜⬜⬜ \n\n🎲➖( CODIGO:04 )➖🎲  \n ")

                                                        except:
                                                            "bot desligado"
                                                        return
                                                    # 03. SEQUENCIA JOGUE PRETO[CODIGO03]:
                                                    if default[0:4] == ['V', 'P', 'V', 'P']:
                                                            print("jogue preto_prc")
                                                            gale_atual = 0
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            gale_atual = 0
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return
                                                    # 01. SEQUENCIA JOGUE PRETO[CODIGO04]:
                                                    if default[0:4] == ['V', 'V', 'V', 'P']:
                                                            gale_atual = 0
                                                            print("jogue preto_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar no vermelho_prc
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                g0)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH, click_add_valor).send_keys(
                                                                br)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            entrada_confirmada_agora = "SEQUENCIA ENCONTRADA NO PRETO COD:01"
                                                            print("joguei preto_prc auto")
                                                            analisar = 1
                                                            QNT_ENTRADA += 1
                                                            toast(
                                                                f"Meta do jogo: {tempo_de_parar} WIN\nParando jogo se: {tempo_percas} LOSS")
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🚨Estratégia Confirmada🚨 \n\n Jogue:   ⬛⬛⬛️ \n Proteja: ⬜⬜⬜ \n\n🎲➖( CODIGO:01 )➖🎲  \n ")


                                                            except:
                                                                "bot desligado"
                                                            return


                                                ###################################################################################################

                                                if analisar == 1:
                                                    await asyncio.sleep(.5)
                                                    if gale_atual == 0:
                                                        # 04. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:4] == ['P', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:01"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['B', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:01"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['V', 'V', 'V', 'V']:

                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei preto_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:01"
                                                            print("indo para g1 continue no preto_prc")
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                            # 02. VITORIA SEM GALE [CODIGO02]

                                                        # 03. VITORIA SEM GALE [CODIGO02]
                                                        if default[0:4] == ['P', 'V', 'P', 'V']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO PRETO SEM GALE! COD:03"
                                                                print("ganhou sem gale")
                                                                vitoriag0 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(⬛⬛⬛)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        if default[0:4] == ['B', 'V', 'P', 'V']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:03"
                                                                print("ganhou sem gale BRANCO")
                                                                vitoriag0 += 1
                                                                brancog0 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_percas += 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        if default[0:4] == ['V', 'V', 'P', 'V']:

                                                                await asyncio.sleep(1)
                                                                navegador.find_element(By.XPATH, click_preto).click()
                                                                await asyncio.sleep(1)
                                                                # elemento para clicar na caixa de add valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # clique adicionando money para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(g1)
                                                                await asyncio.sleep(2)
                                                                # elemento para confirmar entrada na cor
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                # confirmando branco_prc
                                                                navegador.find_element(By.XPATH, click_branco).click()
                                                                await asyncio.sleep(1)
                                                                # clicando no imput valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(0.5)
                                                                # adicionando valor no branco_prc reais
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(br1)
                                                                await asyncio.sleep(1)
                                                                # clique para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                print("joguei preto_prc auto g1")
                                                                entrada_confirmada_agora = "INDO PARA O GALE 01 COD:03"
                                                                print("indo para g1 continue no preto_prc")
                                                                gale_atual = 1
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                                # 02. VITORIA SEM GALE [CODIGO02]

                                                        # 04. VITORIA SEM GALE [CODIGO04]
                                                        if default[0:4] == ['V', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO SEM GALE! COD:04"
                                                            print("ganhou sem gale")
                                                            vitoriag0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE\n(🟥🟥🟥)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['B', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO SEM GALE! COD:04"
                                                            print("ganhou sem gale BRANCO")
                                                            vitoriag0 += 1
                                                            brancog0 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS SEM GALE \n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:INDO PARA GALE1
                                                        if default[0:4] == ['P', 'P', 'P', 'P']:

                                                            print("indo para g1 continue no vermelho_prc")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g1)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(0.5)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br1)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            print("joguei vermelho_prc auto g1")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 01 COD:04"
                                                            gale_atual = 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (01/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################

                                                    if gale_atual == 1:
                                                        await asyncio.sleep(.5)
                                                        # 04. VITORIA COM GALE 1[CODIGO01]
                                                        if default[0:4] == ['P', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['B', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:01"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO01]:INDO PARA GALE2
                                                        if default[0:4] == ['V', 'V', 'V', 'V']:
                                                            print("joguei preto_prc auto g2")
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            await asyncio.sleep(1)
                                                            navegador.find_element(By.XPATH, click_preto).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)

                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:01"
                                                            print("indo para g2 continue no preto_prc")
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                        # 03. VITORIA COM GALE 1[CODIGO01]'P', 'V', 'V', 'P'
                                                        if default[0:4] == ['P', 'V', 'V', 'P']:
                                                                analisar = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 1! COD:03"
                                                                print("VITORIA COM GALE 1")
                                                                vitoriag1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                                #tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬛⬛⬛)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        if default[0:4] == ['B', 'V', 'V', 'P']:
                                                                analisar = 0
                                                                gale_atual = 0
                                                                entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:03"
                                                                print("VITORIA COM GALE 1")
                                                                vitoriag1 += 1
                                                                brancog1 += 1
                                                                tempo_de_parar_vitoria += 1
                                                               # tempo_de_parar -= 1

                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:03 )➖🎲  \n ")
                                                                except:
                                                                    "bot desligado"
                                                                return
                                                        # 03. DERROTA[CODIGO01]:INDO PARA GALE2
                                                        if default[0:4] == ['V', 'V', 'V', 'P']:
                                                                print("joguei preto_prc auto g2")
                                                                # APOSTAR NO VERMELHO elemento para clicar
                                                                await asyncio.sleep(1)
                                                                navegador.find_element(By.XPATH, click_preto).click()
                                                                await asyncio.sleep(1)
                                                                # elemento para clicar na caixa de add valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # clique adicionando money para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(g2)
                                                                await asyncio.sleep(2)
                                                                # elemento para confirmar entrada na cor
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)
                                                                # confirmando branco_prc
                                                                navegador.find_element(By.XPATH, click_branco).click()
                                                                await asyncio.sleep(1)
                                                                # clicando no imput valor
                                                                navegador.find_element(By.XPATH, click_valor).click()
                                                                await asyncio.sleep(1)
                                                                # adicionando valor no branco_prc reais
                                                                navegador.find_element(By.XPATH,
                                                                                       click_add_valor).send_keys(br2)
                                                                await asyncio.sleep(1)
                                                                # clique para apostar
                                                                navegador.find_element(By.XPATH,
                                                                                       click_confirmar_aposta).click()
                                                                await asyncio.sleep(1)

                                                                entrada_confirmada_agora = "INDO PARA O GALE 02 COD:03"
                                                                print("indo para g2 continue no preto_prc")
                                                                gale_atual = 2
                                                                try:
                                                                    bot = telebot.TeleBot(token=api_key)
                                                                    bot.send_message(chat_id=chat_id_gp,
                                                                                     text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'🟥🟥🟥\n•Permaneça na Cor:⬛⬛⬛\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                                except:
                                                                    "bot desligado"
                                                                return

                                                        # 01. VITORIA COM GALE [CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:4] == ['V', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1")
                                                            vitoriag1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                        if default[0:4] == ['B', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 1! COD:04"
                                                            print("VITORIA COM GALE 1 BRANCO")
                                                            vitoriag1 += 1
                                                            brancog1 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 1\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO04]:INDO PARA GALE2
                                                        if default[0:4] == ['P', 'P', 'P', 'P']:
                                                            print("indo para g2 continue no vermelho_prc")
                                                            await asyncio.sleep(1)
                                                            # APOSTAR NO VERMELHO elemento para clicar
                                                            navegador.find_element(By.XPATH, click_vermelho).click()
                                                            await asyncio.sleep(1)
                                                            # elemento para clicar na caixa de add valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # clique adicionando money para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(g2)
                                                            await asyncio.sleep(2)
                                                            # elemento para confirmar entrada na cor
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            # confirmando branco_prc
                                                            navegador.find_element(By.XPATH, click_branco).click()
                                                            await asyncio.sleep(1)
                                                            # clicando no imput valor
                                                            navegador.find_element(By.XPATH, click_valor).click()
                                                            await asyncio.sleep(1)
                                                            # adicionando valor no branco_prc reais
                                                            navegador.find_element(By.XPATH,
                                                                                   click_add_valor).send_keys(br2)
                                                            await asyncio.sleep(1)
                                                            # clique para apostar
                                                            navegador.find_element(By.XPATH,
                                                                                   click_confirmar_aposta).click()
                                                            await asyncio.sleep(1)
                                                            print("joguei vermelho_prc auto g2")
                                                            entrada_confirmada_agora = "INDO PARA O GALE 02 COD:04"
                                                            gale_atual = 2
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text=f"•Estamos no: ({ultimo_numero})\n•Cor do Resultado:'⬛⬛⬛\n•Permaneça na Cor:🟥🟥🟥\n \n🎲➖ (02/02) ➖🎲\n\n")
                                                            except:
                                                                "bot desligado"
                                                            return

                                                    #########################################################################################################
                                                    if gale_atual == 2:
                                                        await asyncio.sleep(.5)
                                                        # 01. VITORIA COM GALE 2[CODIGO01]'V', 'V', 'V', 'V', 'V'
                                                        if default[0:4] == ['P', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO PRETO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬛⬛⬛)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"

                                                            return
                                                        if default[0:4] == ['B', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:01"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            #tempo_de_parar -= 1

                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 01. DERROTA[CODIGO01]:PERDEMOS
                                                        if default[0:4] == ['V', 'V', 'V', 'V']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:01"
                                                            print("perdeu totalmente ")
                                                            derrota_vermelho += 1
                                                            derrota_geral += 1
                                                            #tempo_percas -= 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:01 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        # 04. VITORIA COM GALE 2[CODIGO04]'V', 'P', 'P', 'P', 'P'
                                                        if default[0:4] == ['V', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            entrada_confirmada_agora = "GANHAMOS NO VERMELHO GALE 2! COD:04"
                                                            print("VITORIA COM GALE 2")
                                                            vitoriag2 += 1
                                                            tempo_de_parar_vitoria += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(🟥🟥🟥)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        if default[0:4] == ['B', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            #tempo_de_parar -= 1
                                                            tempo_de_parar_vitoria += 1
                                                            entrada_confirmada_agora = "GANHAMOS NO BRANCO GALE 2! COD:02"
                                                            print("VITORIA COM GALE 2 BRANCO")
                                                            vitoriag2 += 1
                                                            brancog2 += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="✅✅✅ GREEN ✅✅✅ \nGANHAMOS COM GALE 2\n(⬜ ⬜ ⬜)\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return
                                                        # 04. DERROTA[CODIGO04]:PERDEMOS
                                                        if default[0:4] == ['P', 'P', 'P', 'P']:
                                                            analisar = 0
                                                            gale_atual = 0
                                                            tempo_de_parar_derrota += 1
                                                            #tempo_percas -= 1
                                                            entrada_confirmada_agora = "NÃO FOI DESTA VEZ, PERDEMOS..! COD:04"
                                                            print("perdeu totalmente ")
                                                            derrota_preto += 1
                                                            derrota_geral += 1
                                                            try:
                                                                bot = telebot.TeleBot(token=api_key)
                                                                bot.send_message(chat_id=chat_id_gp,
                                                                                 text="🤖 LOSS 🤖 \n Diminua as percas, volte mais tarde'\n\n🎲➖( CODIGO:04 )➖🎲  \n ")
                                                            except:
                                                                "bot desligado"
                                                            return


                                                        ###############################################################################################


                                                await asyncio.sleep(1)

                                            await CHECK_VERSION(finalcor)

                                            if tempo_de_parar_vitoria == float(tempo_de_parar):
                                                toast("Meta Concluida com sucesso")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Meta atingiada!: Vitorias: {tempo_de_parar}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            if tempo_de_parar_derrota == float(tempo_percas):
                                                toast("Limite de perca Atingido, lamentamos!")
                                                progresso = 0
                                                self.sw_seconds = 0
                                                analisar = 0
                                                sequencia_4_ligado = 0
                                                sequencia_7_ligado = 0
                                                sequencia_9_ligado = 0
                                                sequencia_mega_ligado = 0
                                                navegador.close()
                                                await asyncio.sleep(4)
                                                toast("Reinicie o sistemas...")
                                                try:
                                                    bot = telebot.TeleBot(token=api_key)
                                                    bot.send_message(chat_id=chat_id_gp,
                                                                     text=f"Limite de percas atingido!: Loss: {tempo_percas}\nparando apostas...")
                                                except:
                                                    "bot desligado"
                                                break

                                                await asyncio.sleep(.1)

                                            #print(f"sequencia de x - 3:{default}")
                                            if tempo_de_parar_vitoria != float(tempo_de_parar):
                                                falta_qnt_parar = int(tempo_de_parar) - int(tempo_de_parar_vitoria)
                                                toast(f"Meta configurada para: {tempo_de_parar} win \nfalta: {falta_qnt_parar}")


                                            await asyncio.sleep(1)
                                        except:
                                            try:
                                                bot = telebot.TeleBot(token=api_key)
                                                entrada_confirmada_agora = f"CONEXÃO COM A INTERNET TURBULENTA, RECOMENDAMOS REINICIAR O JOGO."
                                                print(f"Algum error x - 2:{finalcor}")
                                                bot.send_message(chat_id=chat_id_gp, text="SEQUENCIA MEGA: \n alto consumo de memoria, isso esta afetando o desempenho, reinicie o programa")
                                            except: ""
                                    if sequencia_mega_ligado != 1:
                                        print("desligado Mega")
                                        try:
                                            bot = telebot.TeleBot(token=api_key)
                                            bot.send_message(chat_id=chat_id_gp,text="DESATIVANDO SEQUENCIA MEGA: \n OBS: Quando trocamos a sequencia é recomendado reiniciar o Programa para evitar Bugs e consumo de memoria desnecessario.")
                                        except:
                                            "..."

                                #print(f"limite de percas: {tempo_percas} \nmeta de win: {tempo_de_parar}")

    #########################################DESATIVAR SEC####################################################################

                                if ativar_sequencia == 7:
                                        progresso = 0
                                        self.sw_seconds = 0
                                        analisar = 0
                                        sequencia_4_ligado = 0
                                        if sequencia_4_ligado == 0:
                                            print('Sistema de apostas 4 desativado ')
                                            sequencia_4_ligado = None
                                            break
                                        sequencia_7_ligado = 0
                                        if sequencia_7_ligado == 0:
                                            print('Sistema de apostas 7 desativado ')
                                            sequencia_7_ligado = None
                                            break
                                        sequencia_9_ligado = 0
                                        if sequencia_9_ligado == 0:
                                            print('Sistema de apostas 9 desativado ')
                                            sequencia_9_ligado = None
                                            break
                                        sequencia_mega_ligado = 0
                                        if sequencia_mega_ligado == 0:
                                            print('Sistema de apostas 4 desativado ')
                                            sequencia_mega_ligado = None
                                            break
                                        print('Sistema de apostas desativado')
                                        toast("sistema em pausa")
                                        break



                                else:
                                    "qualque coisa"
                        if resulROOL != 'Girando...':
                            await asyncio.sleep(.01)
                    await asyncio.sleep(.1)

                await asyncio.sleep(.1)

            await asyncio.sleep(.1)

    async def base(self):
        (done, pending) = await asyncio.wait({self.kivyCoro(), self.GlobalTask()},
                                             return_when='FIRST_COMPLETED')

        try:
            bot = telebot.TeleBot(token=api_key)
            bot.send_message(chat_id=chat_id_gp,
                             text=f"sistema desligado\n\n")
        except:
            "bot desligado"


if __name__ == '__main__':
    async def mainThread():
        instanceApp = MegaBlazer()  # Instanciate your App class
        a = asyncio.create_task(instanceApp.base())  # Run kivyApp as a task
        (done, pending) = await asyncio.wait({a}, return_when='FIRST_COMPLETED')
        # (done, pending) = await asyncio.wait({b}, return_when='FIRST_COMPLETED')


    asyncio.run(mainThread())
