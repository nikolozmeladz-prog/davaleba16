from django.db.models import Q, F
from .models import Product


# Q Expressions

def q_example_1():
    return Product.objects.filter(
        Q(price__gt=50) | Q(quantity__lt=10)
    )


def q_example_2():
    return Product.objects.filter(
        Q(name__icontains="phone"),
        Q(price__range=(100, 500))
    )


def q_example_3():
    return Product.objects.filter(
        ~Q(price__lt=200)
    )


# F Expressions

def f_example_1():
    return Product.objects.update(
        price=F('price') + 10
    )


def f_example_2():
    return Product.objects.filter(
        price__gt=F('quantity')
    )


def f_example_3():
    return Product.objects.update(
        quantity=F('quantity') + 1
    )
