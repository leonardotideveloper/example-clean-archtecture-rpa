from abc import ABC, abstractmethod
from typing import Dict

class GetPriceDolarRepositoryInterface(ABC):
    @abstractmethod
    def get_currencies(self, request) -> Dict: pass
