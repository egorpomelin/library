from library_main.models import Category, Genre, News


def category(request):
    category = Category.objects.all().order_by('name')
    genre = Genre.objects.all()
    news = News.objects.all().order_by('-pudlicachia_date')[:6]
    return {'category' : category, 'genre' : genre, 'news' : news}