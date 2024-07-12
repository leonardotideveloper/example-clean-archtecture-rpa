class HttpRequest:

    def __init__(
        self,
        body = None,
        headers = None,
        url = None,
        params = None
        ):
        self.body = body
        self.headers = headers
        self.url = url
        self.params = params
