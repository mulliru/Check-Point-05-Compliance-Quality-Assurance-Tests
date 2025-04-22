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

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 15)

    driver.get("https://automationintesting.online/admin")
    print("🌐 Página de login carregada.")

    try:
        # Preencher login
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("admin")
        password.send_keys("password")
        login_button.click()

        # Esperar que vá pra próxima tela após login
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "roomName")))

        # Tirar screenshot da tela de login com sucesso
        screenshot_path = os.path.abspath("../evidencias/login_sucesso.png")
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot do login salva em: {screenshot_path}")

    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        evidencias_dir = os.path.abspath("../evidencias")
        os.makedirs(evidencias_dir, exist_ok=True)
        html_path = os.path.join(evidencias_dir, "page_source.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("📝 HTML da página salvo em evidencias/page_source.html")

    print("🔚 Teste finalizado.\n")

test_login_sucesso()
