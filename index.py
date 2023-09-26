#anotações - python power up

import pyautogui
import time
import pandas

# pyautogui.click -> clicar  
# pyautogui.write -> escrever
# pyautogui.press -> pressionar
# pyautogui.hotkey -> atalho

pyautogui.PAUSE = 0.3
# abrir o chrome
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# #fazer login
pyautogui.click(x=672, y=399) #seleciona o campo do email
pyautogui.write("marinajensen@gmail.com")

pyautogui.press("tab") #seleciona o campo senha
pyautogui.write("umasenha")

pyautogui.press("tab") #submete o formulário
pyautogui.press("enter")

#espera a tela carregar
time.sleep(3)    

#importar a base de dados
tabela = pandas.read_csv("produtos.csv")

#cadastrar produto

for produto in tabela.index:
    pyautogui.click(x=771, y=276)
    pyautogui.write(str(tabela.loc[produto, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[produto, 'marca']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[produto, 'tipo']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[produto, 'categoria']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[produto, 'preco_unitario']))

    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[produto, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[produto, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)