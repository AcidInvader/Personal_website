from datetime import date
import views as view


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    "/": view.Index(),
    "/about/": view.About(),
    "/blog/": view.Blog(),
    '/contacts/': view.Contacts(),
    '/portfolio/': view.Portfolio(),
    '/projects-list/': view.ProjectsList(),
    "/create-project/": view.CreateProject(),
    "/create-category/": view.CreateCategory(),
    "/category-list/": view.CategoryList(),
    "/copy-project/": view.CopyProject(),
    '/services/': view.Services(),
    '/test/': view.Testing(),
}

