from django.db import models

class TypeOfPost(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.email}"

class ProjectPost(models.Model):
    type_of_post = models.ForeignKey(TypeOfPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contents/' )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        self.type_of_post   