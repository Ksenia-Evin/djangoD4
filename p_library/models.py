from django.db import models  
  
  
class Author(models.Model):  
    full_name = models.CharField(max_length=50)
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.CharField(max_length=128) 
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
    )
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    friend = models.ManyToManyField('Friend')
    cover = models.ImageField(upload_to='covers/', blank=True)
    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
    )


class Friend(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name