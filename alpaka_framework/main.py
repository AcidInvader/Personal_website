from castom_request import GetRequests, PostRequests
from quopri import decodestring


class PageNotFound404:
    def __call__(self, request):
        return '404 WTF', '404 Page Not Found'


class Application:

    def __init__(self, routes, front_obj):
        self.routes = routes
        self.front_lst = front_obj


    def __call__(self, environ, start_response):
        # получаем адрес, по которому выполнен переход
        path = environ["PATH_INFO"]

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method
        print(f'{method=}')

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = Application.decode_value(data)
            print(f'We have got POST request {Application.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = Application.decode_value(request_params)
            print(f'We have got GET request {Application.decode_value(request_params)}')

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        # наполняем словарь request элементами
        # этот словарь получат все контроллеры
        # отработка паттерна front controller
        for front in self.front_lst:
            front(request)

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
        


