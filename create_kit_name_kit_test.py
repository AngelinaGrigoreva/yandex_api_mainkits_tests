import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert name == kit_response.json()["name"]

#Тест1 Успешное создание набора: Допустимое количество символов в параметре name (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
#Тест2 Успешное создание пользователя: Допустимое количество символов в параметре name (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda")
#Тест3 Успешное создание набора: Разрешены русские буквы в параметре name
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")
#Тест4 Успешное создание набора: Разрешены английские буквы в параметре name
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")
#Тест5 Успешное создание набора: Разрешены спецсимволы в параметре name
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")
#Тест6 Успешное создание набора: Разрешены пробелы в параметре name
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")
#Тест7 Успешное создание набора: Разрешены цифры в параметре name
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Функция для негативной проверки
def negative_assert(name):
        kit_body = get_kit_body(name)
        kit_response = sender_stand_request.post_new_client_kit(kit_body)
        assert kit_response.status_code == 400

#Тест8 Ошибка при создании набора: Количество символов больше допустимого в параметре name (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcAbcdabcdabcdaba")
#Тест9 Ошибка при создании набора: Количество символов меньше допустимого в параметре name (0)
def test_create_kit_none_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert(kit_body)
#Тест10 Ошибка при создании набора: Передан другой тип параметра name (число)
def test_create_kit_number_type_in_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
#Тест11 Ошибка при создании набора: Параметр name не передан в запросе
def test_create_kit_delete_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400




