from .models import *


def default(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }