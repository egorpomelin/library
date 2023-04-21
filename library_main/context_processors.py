from models import Category, Genre


def category(request):
    category = Category.objects.all().order_by('name')
    genre = Genre.objects.all()
    return {'category' : category, 'genre' : genre}