
class GetRequests:

    @staticmethod
    def parse_input_data(param: str):
        result = {}
        if param:
            params = param.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result


    @staticmethod
    def get_request_params(environ):
        # получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # превращаем их в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:

    @staticmethod
    def parse_input_data(param: str) -> dict:
        result = {}
        if param:
            params = param.split('&')

        for item in params:
            k, v = item.split('=')
            result[k] = v
        return result


    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data


    def parse_wsgi_input_data(self, bytes: bytes) -> dict:
        result = {}
        if bytes:
            data_str = bytes.decode(encoding='utf-8')
            print(data_str)
            result = self.parse_input_data(data_str)
        return result


    def get_request_params(self, environ):
        # получаем данные
        data = self.get_wsgi_input_data(environ)
        # превращаем данные в словарь
        data = self.parse_wsgi_input_data(data)
        return data
