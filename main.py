import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

        # O ÚNICO .get() do projeto fica aqui
        cls.driver.get(data.URBAN_ROUTES_URL)
        # Criamos a instância da página uma única vez
        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # ---------------------------
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_select_comfort(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_comfort_tariff()


    def test_fill_phone(self):
        # Não use self.driver.get aqui!
        self.page.fill_phone_number(data.PHONE_NUMBER)
        self.page.enter_sms_code()

    def test_add_card(self):
        # O navegador já está na tela certa vindo do teste anterior
        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_message(self):
        self.page.set_comment(data.MESSAGE_FOR_DRIVER)

    def test_blanket(self):
        # Se você der .get() aqui, a tarifa Comfort some e o switch da manta some junto!
        self.page.toggle_blanket_and_tissues()

    def test_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_comfort_tariff()
        page.add_ice_creams(2)

    def test_order_taxi(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.select_comfort_tariff()
        page.fill_phone_number(data.PHONE_NUMBER)
        page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        page.set_comment(data.MESSAGE_FOR_DRIVER)
        page.toggle_blanket_and_tissues()
        page.add_ice_creams(2)
        page.click_order_taxi()