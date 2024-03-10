from datetime import date

from alpaka_framework.templater import render
from patterns.creational_patterns import Engine, Logger

site = Engine()
logger = Logger('main')


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


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


# the list of projects
class ProjectsList:
    def __call__(self, request):
        logger.log("List of projects")
        try:
            category = site.find_category_by_id(int(request["request_params"]["id"]))
            return '200 OK', render('projects-list.html', objects_list=category.projects,
                                    name=category.name, id=category.id)
        except KeyError:
            return "200 OK", render('portfolio.html', objects_list="No projects have been added yet")


# Controller for project creation
class CreateProject:
    category_id = -1

    def __call__(self, request):
        if request["method"] == "POST":
            data = request["data"]

            name = data["name"]
            name = site.decode_value(name)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                project = site.create_project("personal", name, category)
                site.projects.append(project)
            return "200 OK", render("projects-list.html",
                                    objects_list=category.projects,
                                    name=category.name,
                                    id=category.id
                                    )
        else:
            try:
                self.category_id = int(request["request_params"]["id"])
                category = site.find_category_by_id(int(self.category_id))

                return "200 OK", render("create_project.html",
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return "200 OK", "No projects have been added yet"


# Controller to create a category
class CreateCategory:
    def __call__(self, request):

        if request["method"] == "POST":
            data = request["data"]
            name = data["name"]
            name = site.decode_value(name)

            category_id = data.get("category_id")
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
            new_category = site.create_category(name, category)
            site.categories.append(new_category)

            return "200 OK", render("portfolio.html", objects_list=site.categories)
        else:
            categories = site.categories
            return "200 OK", render('create_category.html', categories=categories)


# Controller of categories list
class CategoryList:
    def __call__(self, request):
        if site.categories:
            logger.log("List of categories")
            return "200 OK", render("category_list.html", objects_list=site.categories)
        else:
            return "200 OK", render("category_list.html", objects_list="No category have been added yet")


# Controller of copy project
class CopyProject:
    def __call__(self, request):
        request_params = request["request_params"]

        try:
            name = request_params["name"]

            old_project = site.get_project(name)
            if old_project:
                new_name = f"copy_{name}"
                new_project = old_project.clone()
                new_project.name = new_name
                site.projects.append(new_project)

            return "200 OK", render("projects-list.html", objects_list=site.projects, name=new_project.category.name)
        except KeyError:
            return "200 OK", "No projects have been added yet"


class Services:
    def __call__(self, request):
        return '200 OK', render('services.html')


class Testing:
    def __call__(self, request):
        return '200 OK', render('test.html')



