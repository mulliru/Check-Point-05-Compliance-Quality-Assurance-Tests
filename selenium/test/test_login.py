# test_login.py
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Função para salvar prints na pasta 'evidencias'
def salvar_evidencia(driver, nome_arquivo):
    caminho = os.path.join("..", "evidencias", nome_arquivo)
    driver.save_screenshot(caminho)
    print(f"📸 Screenshot salva em: {caminho}")

# Teste de login positivo
def test_login_sucesso():
    print("\n🔵 Teste de login POSITIVO iniciado...")

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # Acessa a página de login
        driver.get("https://automationintesting.online/admin")
        print("🌐 Página de login acessada.")
        salvar_evidencia(driver, "login_tela.png")

        # Preenche e envia o formulário
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("admin")
        password.send_keys("password")
        login_button.click()

        # Espera pelo elemento que indica login bem-sucedido
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="roomlisting"]')))
        salvar_evidencia(driver, "login_sucesso.png")
        print("✅ Login realizado com sucesso.")

    except Exception as e:
        salvar_evidencia(driver, "login_erro.png")
        print(f"❌ Erro no login positivo: {e}")

    finally:
        print("🔚 Teste de login positivo finalizado.\n")

# Teste de login negativo
def test_login_negativo():
    print("\n🔴 Teste de login NEGATIVO iniciado...")

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Acessa a página de login
        driver.get("https://automationintesting.online/admin")
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Dados inválidos
        username.send_keys("usuario_errado")
        password.send_keys("senha_errada")
        login_button.click()

        # Aguarda a falha e tira print
        time.sleep(2)
        salvar_evidencia(driver, "login_negativo.png")
        print("🚫 Login inválido identificado com sucesso.")

    except Exception as e:
        print(f"❌ Erro no login negativo: {e}")

    finally:
        print("🔚 Teste de login negativo finalizado.\n")


# EXECUÇÃO
if __name__ == "__main__":
    test_login_sucesso()
    test_login_negativo()
