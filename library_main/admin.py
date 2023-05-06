from django.contrib import admin
from library_main.models import Author, Category, Genre, Book, News, Quotes, Contacts

class BookInline(admin.TabularInline):
    model = Book

class GenreInline(admin.TabularInline):
    model = Genre


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions_on_bottom = True
    list_filter = ('name',)
    list_per_page = 20
    search_fields = ('name',)
    inlines = [BookInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions_on_bottom = True
    list_filter = ('name',)
    list_per_page = 20
    search_fields = ('name',)
    inlines = [GenreInline]

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    actions_on_bottom = True
    list_filter = ('name', 'category')
    list_per_page = 20
    search_fields = ('name',)
    inlines = [BookInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'description', 'linkLitress', 'linkDowload', 'linkOnline', 'ageRestriction', 'date_of_writing', 'value', 'isbn')
    actions_on_bottom = True
    list_filter = ('name', 'genre', 'author')
    list_per_page = 20
    search_fields = ('name', 'description')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'image', 'source', 'pudlicachia_date')
    actions_on_bottom = True
    list_filter = ('pudlicachia_date', 'source')
    list_per_page = 20
    search_fields = ('heading', 'description')

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('books', 'quotes')
    actions_on_bottom = True
    list_filter = ('books',)
    list_per_page = 20
    search_fields = ('quotes',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Contacts)
