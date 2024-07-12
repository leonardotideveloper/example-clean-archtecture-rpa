#pylint: disable=line-too-long
#pylint: disable=missing-class-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=missing-module-docstring
import requests
from src.presentation.http_types.http_request import HttpRequest

class ServiceCurrencies:
    def get_currencies(self, request: HttpRequest) -> str:
        headers = {
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
            'Referer': 'https://economia.uol.com.br/cotacoes/cambio/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Linux"',
        }

        response = requests.get(
            url=request.url,
            headers=headers,
            timeout=10
        )
        return response.text
