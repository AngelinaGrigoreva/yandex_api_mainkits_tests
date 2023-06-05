import configuration
import requests
import data

#Функция на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
authToken = f"Bearer {response.json()['authToken']}"
headers_dict = data.headers.copy()
headers_dict["Authorization"] = "Bearer " + authToken

#Функция на создание нового набора
def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_SET,json=kit_body,
                         headers=headers_dict)


