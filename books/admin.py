#Register your models here
from django.contrib import admin
from .models import Book, User, Category, ISBN, Tag
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "author")
    list_filter = ("category", )
    search_fields = ("title",)

class BookInline(admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(ISBN)
admin.site.register(Tag, TagAdmin)