import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login_sucesso():
    print("🔵 Iniciando teste de login...")

    # Configuração do navegador
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 15)

    # Acessa a página de login
    driver.get("https://automationintesting.online/admin")
    print("🌐 Página de login carregada.")

    # Garante que a pasta de evidências existe
    evidencias_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidencias"))
    os.makedirs(evidencias_dir, exist_ok=True)

    try:
        # Preenche e submete o login
        username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("admin")
        password.send_keys("password")
        login_button.click()

        # Espera por elemento na tela de sucesso
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "room-form")))

        # Salva screenshot
        screenshot_path = os.path.join(evidencias_dir, "login_sucesso.png")
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot salva em: {screenshot_path}")

    except Exception as e:
        # Salva HTML em caso de erro
        html_path = os.path.join(evidencias_dir, "page_source.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("📝 HTML salvo em evidencias/page_source.html")
        print(f"❌ Erro durante o teste: {e}")

    print("🔚 Teste finalizado.\n")

test_login_sucesso()
