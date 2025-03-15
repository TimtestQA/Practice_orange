import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")  # Запуск без UI
    options.add_argument("--no-sandbox")  # Отключение sandbox (для контейнера)
    options.add_argument("--disable-dev-shm-usage")  # Фикс shared memory
    options.add_argument("--window-size=1920,1080")  # Разрешение окна
    options.add_argument("--disable-gpu")  # Отключение GPU (важно для headless)
    options.add_argument("--remote-debugging-port=9222")  # Открываем порт отладки

    # Явно указываем путь к chromedriver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = driver
    yield
    driver.quit()
