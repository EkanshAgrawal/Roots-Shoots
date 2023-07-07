# from django.db import models
# from django.conf import settings
#



from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):


    category = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.category


class BlogPlant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'post_author')
    blog_title = models.CharField(max_length= 264)
    slug = models.SlugField(max_length=264, unique=True, default='',editable=False)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to= 'blog_image')
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name ='blog_cat')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title, allow_unicode=True)
        super().save(*args, **kwargs)
