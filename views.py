from alpaka_framework.templater import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Blog:
    def __call__(self, request):
        return '200 OK', render('blog.html')


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contact.html')


class Portfolio:
    def __call__(self, request):
        return '200 OK', render('portfolio.html')


class Services:
    def __call__(self, request):
        return '200 OK', render('services.html')


class Testing:
    def __call__(self, request):
        return '200 OK', render('test.html')



