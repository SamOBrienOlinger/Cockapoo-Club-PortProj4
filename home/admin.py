from django.contrib import admin
from myproject.myapp.models import Author

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Author, AuthorAdmin)
