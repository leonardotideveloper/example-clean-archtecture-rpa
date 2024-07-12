from typing import Callable
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest

def request_adapter(controller: Callable) -> HttpResponse:
    request = HttpRequest(
        url="https://api.cotacoes.uol.com/mixed/summary?&currencies=1,11,5&itens=1,435833,1168&fields=name,openbidvalue,askvalue,variationpercentbid,price,exchangeasset,open,pctChange,date,abbreviation&jsonp=jsonp"
    )
    response = controller(request)
    return response
