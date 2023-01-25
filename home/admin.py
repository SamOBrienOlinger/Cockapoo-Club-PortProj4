from django.contrib import admin
from .models import index


admin.site.register(index)

# @admin.site.register(home())
# class home(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)

# admin.site.register(homepage)

# from CockapooClub.home.models import Author
# from .models import Post, Comment
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     pass
#     admin.site.register(Author, AuthorAdmin)
