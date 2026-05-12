from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code


class UrbanRoutesPage:

    # --- LOCALIZADORES ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    route_button = (By.CSS_SELECTOR, '.button.round')

    comfort_tariff = (By.XPATH, "//div[text()='Comfort']")

    phone_button = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, 'phone')
    next_button_phone = (By.XPATH, "//button[text()='Próximo']")

    sms_code_field = (By.XPATH, "//div[contains(@class,'number-picker')]//input[@id='code']")
    confirm_sms_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//div[text()='Adicionar cartão']")
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, "//div[contains(@class,'card-second-row')]//input[@id='code']")
    confirm_card_button = (By.XPATH, "//button[text()='Adicionar']")
    close_payment_modal = (By.CLASS_NAME, 'close-button')

    comment_field = (By.ID, 'comment')

    blanket_switch = (By.XPATH, "//div[contains(text(),'Manta')]//span")
    ice_cream_plus = (By.XPATH, "//div[contains(text(),'Sorvete')]//div[@class='counter-plus']")

    order_button = (By.CLASS_NAME, 'smart-button')
    searching_modal = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- MÉTODOS ---

    def click_set_route_button(self):
        self.wait.until(EC.element_to_be_clickable(self.route_button)).click()

    def set_address(self, address_from, address_to):
        self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(address_from)
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(address_to)
        self.click_set_route_button()

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_tariff)).click()

    def fill_phone_number(self, phone):
        self.wait.until(EC.element_to_be_clickable(self.phone_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(self.next_button_phone)).click()

    def enter_sms_code(self):
        import time
        time.sleep(2)  # Dá tempo para o log de performance registrar o SMS
        code = retrieve_phone_code(self.driver)

        # Se code vier vazio, o teste para aqui. Verifique se retrieve_phone_code está importado!
        self.wait.until(EC.visibility_of_element_located(self.sms_code_field)).send_keys(code)
        self.wait.until(EC.element_to_be_clickable(self.confirm_sms_button)).click()

    def add_credit_card(self, number, code):
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()

        # Número do cartão
        num_field = self.wait.until(EC.visibility_of_element_located(self.card_number_field))
        num_field.send_keys(number)

        # CVV
        cvv_field = self.wait.until(EC.visibility_of_element_located(self.card_code_field))
        cvv_field.send_keys(code)

        # FORÇAR PERDA DE FOCO: Clique no título do modal para o botão ativar
        self.driver.find_element(By.CLASS_NAME, 'card-wrapper').click()

        # Agora clica em Adicionar
        self.wait.until(EC.element_to_be_clickable(self.confirm_card_button)).click()

        # Fecha o modal de pagamento (o X)
        self.wait.until(EC.element_to_be_clickable(self.close_payment_modal)).click()

    def set_comment(self, message):
        self.wait.until(EC.visibility_of_element_located(self.comment_field)).send_keys(message)

    def toggle_blanket_and_tissues(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_switch)).click()

    def add_ice_creams(self, quantity):
        for _ in range(quantity):
            self.wait.until(EC.element_to_be_clickable(self.ice_cream_plus)).click()

    def click_order_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.order_button)).click()

    def is_searching_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.searching_modal)).is_displayed()