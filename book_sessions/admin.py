from django.contrib import admin
from .models import booking, BookingForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

admin.site.register(booking)


# @admin.register(booking)
# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     list_filter = ('status', 'created_on')
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)


# @admin.register(BookingForm)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)


# @admin.site.register(booking)
# class booking(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)


# @admin.site.register(home)
# class home(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)

# @admin.site.register(PersonalDataForm)
# class PersonalDataForm(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
