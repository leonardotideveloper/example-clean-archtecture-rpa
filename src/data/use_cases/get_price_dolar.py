from typing import Dict
from src.domain.use_cases.get_price_dolar import GetPriceDolar as GetPriceDolarInterface
from src.data.interfaces.get_price_dolar_repository import GetPriceDolarRepositoryInterface

class GetPriceDolar(GetPriceDolarInterface):

    def __init__(self, repository: GetPriceDolarRepositoryInterface):
        self.__repository = repository

    def execute(self, request) -> Dict:
        price_dolar = self.__get_price_dolar(request)
        return self.__format_response(price_dolar)

    def __get_price_dolar(self, request) -> Dict:
        return self.__repository.get_currencies(request)

    @classmethod
    def __format_response(cls, data: Dict) -> Dict:
        return {
            'data': data 
        }
