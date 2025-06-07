import allure
from locators.order_page_locators import OrderPageLocators 
from pages.general_elements import GeneralElements


class OrderPage(GeneralElements):

    @allure.step('  Заполняем поле Имя на форме заказа')
    def set_name_field(self, name):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step('  Заполняем поле "Фамилия"')
    def set_surname_field(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('  Заполняем поле "Адресс"')
    def set_address_field(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('  Выбираем станцию метро')
    def choose_station_field(self, station_name):
        self.click_to_element(OrderPageLocators.METRO_DROPDOWN)
        self.scroll_to_element(OrderPageLocators.select_metro_station_from_dropdown(station_name))
        self.click_to_element(OrderPageLocators.select_metro_station_from_dropdown(station_name))

    @allure.step('  Заполняем поле "Номер телефона"')
    def set_phone_num_field(self, phone_num):
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, phone_num)

    @allure.step('  Выбираем "Когда доставить самокат"')
    @allure.description ('Считается как +{delivery_date} дней к текущей дате')
    def choose_delivery_date_field(self, delivery_date=1):
        self.add_date_to_element(OrderPageLocators.RENT_DATE_INPUT, delivery_date)

    @allure.step('  Выбираем "Срок аренды"')
    def choose_rent_period(self, rent_period):
        locators_q_formatted = self.format_locators(OrderPageLocators.RENT_TERMS_DAYS, rent_period)
        self.click_to_element(OrderPageLocators.RENT_TERMS_DROPDOWN)
        self.click_to_element(locators_q_formatted)
       
    @allure.step('  Выбираем черный "Цвет самоката"')
    def pick_black_color(self):
        self.click_to_element(OrderPageLocators.SCOOTER_COLOR_BLACK_CHECKBOX)

    @allure.step('  Выбираем серый "Цвет самоката"')
    def pick_grey_color(self):
        self.click_to_element(OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX)

    @allure.step('  Заполняем  "Комментарий для курьера"')
    def set_comment(self, comment):
        self.add_text_to_element(OrderPageLocators.COMMENTS_FIELD, comment)

    @allure.step('Заполняем форму заказа 1:')
    def fill_order_data_first(self, order_details):
        self.set_name_field(order_details.get('name'))
        self.set_surname_field(order_details.get('surname'))
        self.set_address_field(order_details.get('address'))
        self.choose_station_field(order_details.get('station_name'))
        self.set_phone_num_field(order_details.get('phone_num'))

    @allure.step('Заполняем форму заказа 2:')
    def fill_order_data_second(self, order_detailes):
        self.choose_delivery_date_field(order_detailes.get('delivery_date'))
        self.choose_rent_period(order_detailes.get('rent_period'))
        if order_detailes.get('colour').lower() == 'чёрный жемчуг':
            self.pick_black_color()
        else:
            self.pick_grey_color()
        self.set_comment(order_detailes.get('comment'))

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверяем модальную форму заказа')
    def check_modal_order(self, text):
        result_text = self.get_text_from_element(OrderPageLocators.COMPLITE_ORDER_MODAL_SUCCESS)
        if text in result_text:
            return True
        return False
