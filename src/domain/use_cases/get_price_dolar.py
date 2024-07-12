from typing import Dict
from abc import ABC, abstractmethod

class GetPriceDolar(ABC):
    @abstractmethod
    def execute(self, request) -> Dict: pass
