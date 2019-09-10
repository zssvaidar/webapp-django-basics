from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    first_name = models.CharField(max_length=64, null=False, blank=True)
    last_name = models.CharField(max_length=64, null=False, blank=True)
    def __str__(self):
        if (self.first_name is '' and self.last_name is ''):
            return 'Hasn\'t'
        else:
            return '%s %s' % (self.first_name, self.last_name)
    def __unicode__(self):
        return '%d' % self.id
class Publisher(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    date_published = models.CharField(max_length=12, null=False, blank=False)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return '%d' % self.id
class Book(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    price =  models.IntegerField()
    description = models.CharField(max_length=1000, null=False, blank=True)
    book_isbn = models.CharField(max_length=15, null=True, blank=False)
    image = models.ImageField(upload_to='book_image', blank=True)
    author_fk = models.ForeignKey(Author, on_delete=models.CASCADE, null=True , blank=True)
    publisher_fk = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    def __str__(self):
        return self.title
class bookRibbon(models.Model):
    title_fk = models.ForeignKey(Category,null=True, on_delete=models.CASCADE)
    book_fk = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.book_fk.title, self.book_fk.author_fk.first_name)
class Cart(models.Model):
    book_fk = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.book_fk.title, self.user_fk.username)
