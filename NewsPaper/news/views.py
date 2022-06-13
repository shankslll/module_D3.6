from django.views.generic import ListView, DetailView
from .models import Post


class ProductsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'message.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'