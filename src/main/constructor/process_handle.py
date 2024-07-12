from src.main.composers.get_price_dolar_composer import get_price_dolar_composer
from src.main.adapters.request_adapter import request_adapter


def run():
    controller = get_price_dolar_composer()
    response = request_adapter(controller)
    print(response)