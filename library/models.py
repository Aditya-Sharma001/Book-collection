from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)    

    def __str__(self):
        return self.title

