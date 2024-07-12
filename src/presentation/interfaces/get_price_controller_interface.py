from abc import ABC, abstractmethod
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest


class GetPriceDolarControllerInterface(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse: pass
