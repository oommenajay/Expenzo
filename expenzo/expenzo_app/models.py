from django.db import models



class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # This field should be hashed
    role = models.IntegerField()  # Define choices for role if needed

    def __str__(self):
        return self.username  # Or any other field you want to represent the user

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type