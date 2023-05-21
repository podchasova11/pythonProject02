import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string


class TestFormRegistration:
    def setup(self):
        print("Выполняюсь до теста")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.freeconferencecall.com/ru/fr")

        self.email = self.generate_random_email()  # Генерация случайного адреса электронной почты
        self.password = self.generate_random_password()  # Генерация случайного пароля

    def generate_random_email(self):
        username = ''.join(random.choices(string.ascii_lowercase, k=10))
        email = f"{username}@yandex.ru"
        return email

    def generate_random_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return password

    def test_open_login_page(self):
        assert self.driver.current_url == "https://www.freeconferencecall.com/ru/fr", "Ошибка"

    # def test_check_availiability_after_refresh(self):
    #     self.driver.refresh()
    #     assert "Заголовок страницы" in self.driver.page_source, "Страница не загрузилась"

    def test_registration_form(self):
        # Ввод данных в форму регистрации
        email_field = self.driver.find_element("xpath", "//input[@id='main_email']")
        email_field.send_keys(self.email)

        password_field = self.driver.find_element("xpath", "//input[@id='password']")
        password_field.send_keys(self.password)

        # Добавьте остальные действия для заполнения формы регистрации

        # Отправка формы
        register_button = self.driver.find_element("xpath", "//*[@id='signupbutton']")
        register_button.click()

        # Проверка успешной регистрации (пример)
        assert "Бесплатные аудиоконференции | FreeConferenceCall.com" in self.driver.page_source

    def teardown(self):
        self.driver.close()
        print("Выполняюсь после теста")

