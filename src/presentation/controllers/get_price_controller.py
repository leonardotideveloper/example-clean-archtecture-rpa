from src.presentation.interfaces.get_price_controller_interface import (
    GetPriceDolarControllerInterface)
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest
from src.domain.use_cases.get_price_dolar import GetPriceDolar as GetPriceDolarInterface
class GetPriceController(GetPriceDolarControllerInterface):
    def __init__(self, use_case: GetPriceDolarInterface) -> None:
        self.__use_case = use_case
    def handle(self, request: HttpRequest) -> HttpResponse:
        response = self.__use_case.execute(request)
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
