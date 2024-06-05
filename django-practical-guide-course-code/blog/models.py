from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Tag(models.Model):
    caption = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=SET_NULL, null=True, related_name="posts")
