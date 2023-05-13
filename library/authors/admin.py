from django.contrib import admin

from .models import Author
# Register your models here.


class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birthday_year', 'data')
    list_display_links = ('id', 'first_name')
    search_fields = ('id', 'first_name', 'last_name', 'birthday_year')
    list_filter = ('first_name', 'last_name', 'birthday_year')


admin.site.register(Author, AutorAdmin)
