from src.services.requests.request_currencies import (
    ServiceCurrencies as ServiceCurrenciesRepository
)
from src.data.use_cases.get_price_dolar import GetPriceDolar
from src.presentation.controllers.get_price_controller import GetPriceController


def get_price_dolar_composer():
    repo = ServiceCurrenciesRepository()
    use_case = GetPriceDolar(repo)
    controller = GetPriceController(use_case)

    return controller.handle
