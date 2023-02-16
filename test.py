from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#salvar todos os dados da pagina
options = Options()
options.add_argument('--user-data-dir=PerfilWhatsapp')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com/')

driver.implicitly_wait(30)

# Faça o login escaneando o código QR com o seu celular


input()