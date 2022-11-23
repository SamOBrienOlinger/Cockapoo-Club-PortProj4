from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# Create your models here.
# STATUS = ((0, "Draft"), (1, "Published"))


# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="blog_posts"
#     )
#     featured_image = CloudinaryField('image', default='placeholder')
#     excerpt = models.TextField(blank=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     likes = models.ManyToManyField(
#         User, related_name='blogpost_like', blank=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,
#                              related_name="comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

# class signup:

# create username and password

#   enter/register details:
#     Username
#     Password
#     User/Owner name
#     Dog name
#     Dog age
#     Vaccinated (Y/N)
#     user submit button


# class signin:

#   authenticate username and password to login

#   bring user to booking page
