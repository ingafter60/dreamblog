from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Model/table name: Author
class Author(models.Model):
    # -----table fields ---------
    # A post belongs to an author / user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The author / user has profile picture
    profile_picture = models.ImageField()

    # Displaying username in admin
    def __str__(self):
        return self.user.username

# Model/table name: Category
class Category(models.Model):
    # -----table fields ---------
    # Category name
    title = models.CharField(max_length=25)

    # Displaying category name in admin
    def __str__(self):
        return self.title

# Model/table name: Post
class Post(models.Model):
    # -----table fields ---------
    # Title
    title       = models.CharField(max_length=100)
    # Overview
    overview    = models.TextField()
    # Time added
    timestamp   = models.DateTimeField(auto_now_add=True)
    # Number of comment
    comment_count = models.IntegerField(default=0)
    # Author
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Thumbnail / image
    thumbnail   = models.ImageField()
    # Categoris (a post has many categories - can grab as many categories as we like in the db)
    categories  = models.ManyToManyField(Category)
    # featurued
    featured   = models.BooleanField()

    # Displaying category name in admin
    def __str__(self):
        return self.title

