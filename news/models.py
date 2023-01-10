from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse_lazy


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postrating=Sum('rating'))
        pRate = 0
        pRate += postRat.get('postrating')

        comRate = self.user.comment_set.all().aggregate(commentrating=Sum('rating'))
        cRate = 0
        cRate += postRat.get('commentrating')

        self.rating = pRate * 3 + comRate


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    VIDEO = 'VI'
    TYPES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
        (VIDEO, 'Видео'),
    ]
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    type = models.CharField(max_length=2, choices=TYPES, default=ARTICLE)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    is_published = models.BooleanField(default=False)
    rating = models.SmallIntegerField(default=0)
    views = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text[0:50] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
