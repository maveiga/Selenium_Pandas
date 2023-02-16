from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import pandas as pd
from time import sleep



app =Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/execute")
def execute():
    wb = Workbook()
    ws = wb.active


    lista=[]
    navegador =webdriver.Firefox()

    link='https://www.linkedin.com/home'
    navegador.get(url=link)

    
    email='seu email'
    senha='sua senha'
   
 

    campo_email = (navegador.find_element(By.CSS_SELECTOR,'#session_key'))
    sleep(2)
    campo_email.send_keys(email)
    campo_senha = (navegador.find_element(By.CSS_SELECTOR,'#session_password'))
    sleep(2)
    campo_senha.send_keys(senha)

    botao_entrar =(navegador.find_element(By.XPATH,("//button[@type='submit']")))

    botao_entrar.click()

    sleep(4)

    busca = navegador.find_element(By.TAG_NAME,"input")
    busca.send_keys('python')
    sleep(3)
    busca.send_keys(Keys.ENTER)
    sleep(5)

    data = navegador.find_elements(By.TAG_NAME, 'a') 
    for i in data: 
        if i.text !='':
            lista.append([i.text])

    
    news =pd.DataFrame(lista, columns=['Vagas'])
    news.to_excel('vagas.xlsx', index=False)
   
    return render_template('login.html')



app.run('localhost',port=5000)

