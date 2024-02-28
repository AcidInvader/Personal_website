from base64 import decodestring
from copy import deepcopy


class Project:
    pass


class User:
    pass


class Guest:
    pass


class UserFactory:
    types = {
        "admin": User,
        "guest": Guest
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class ProjectPrototype:
    # прототип проектов

    def clone(self):
        return deepcopy(self)


class Project(ProjectPrototype):
    def __init__(self, name, category):
        self.name = name
        self.category.projects.append(self)


class PersonalSite(Project):
    pass


class GroupBlog(Project):
    pass


class ProjectFactory:
    types = {
        "personal": PersonalSite,
        "g_blog": GroupBlog
    }

    # порождающий паттерн фабричный метод
    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class Category:
    auto_id = 0  # автоинкремент как в базе данных

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.projects = []  # проекты принадлежащие этой категории

    def projects_count(self):
        result = len(self.projects)  # считаем количество проектов
        if self.category:
            result += self.category.projects_count()
        return result


class Engine:
    def __init__(self):
        self.user = []
        self.guests = []
        self.projects = []
        self.categories = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print(f"{item.id=}")
            if item.id == id:
                return item

        raise Exception(f"There're not category with id = {id}")

    @staticmethod
    def create_project(type_, name, category):
        return ProjectFactory.create(type_, name, category)

    def get_project(self, name):
        for item in self.projects:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace("%", "=").replace("+", " "), "UTF-8")
        val_decode_str = decodestring(val_b)
        return val_decode_str.decode("UTF-8")


# порождающий паттерн Singletone
class SingletoneByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs["name"]

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletoneByName):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print("log--->", text)
