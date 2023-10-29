class ResponseBaseHandler:
    def __init__(self, response_json):
        self.response_json = response_json
        self.code = self.response_json.get("code", None)
        self.msg = self.response_json.get("msg", None)


class ResponseTaskHandler(ResponseBaseHandler):
    def __init__(self, response_json):
        super().__init__(response_json)
        self.cookie = self.response_json.get("cookie", None)
        self.blog = self.response_json.get("blog", None)
        self.input = self.response_json.get("input", None)


class ResponseTokenHandler(ResponseBaseHandler):
    def __init__(self, response_json):
        super().__init__(response_json)
        self.token = self.response_json.get("token", None)


class ResponseAnswerHandler(ResponseBaseHandler):
    def __init__(self, response_json):
        super().__init__(response_json)
        self.note = self.response_json.get("note", None)
