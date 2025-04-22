# test_room_list.py
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

# Função auxiliar de login
def fazer_login(driver, wait):
    driver.get("https://automationintesting.online/admin")

    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("admin")
    password.send_keys("password")
    login_button.click()

# Teste POSITIVO: verifica se há quartos listados
def test_listagem_quartos():
    print("\n🔵 Teste de listagem de quartos POSITIVO iniciado...")

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        fazer_login(driver, wait)
        room_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="roomlisting"]')))

        if room_element:
            salvar_evidencia(driver, "listagem_quartos.png")
            print("✅ Quarto visível identificado com sucesso.")

    except Exception as e:
        salvar_evidencia(driver, "erro_listagem_quartos.png")
        print(f"❌ Erro durante o teste positivo de listagem: {e}")

    finally:
        print("🔚 Teste de listagem positivo finalizado.\n")

# Teste NEGATIVO: tenta acessar uma seção inválida
def test_listagem_quartos_negativo():
    print("\n🔴 Teste de listagem de quartos NEGATIVO iniciado...")

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        fazer_login(driver, wait)

        # Navega para uma rota inválida
        driver.get("https://automationintesting.online/admin/invalidsection")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="roomlisting"]')))

    except Exception:
        salvar_evidencia(driver, "listagem_quartos_negativo.png")
        print("🚫 Página inválida acessada com falha intencional detectada.")

    finally:
        print("🔚 Teste de listagem negativo finalizado.\n")


# EXECUÇÃO
if __name__ == "__main__":
    test_listagem_quartos()
    test_listagem_quartos_negativo()
