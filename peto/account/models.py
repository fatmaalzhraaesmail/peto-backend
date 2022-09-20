from django.db import models
class AccountCreate(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    image=models.ImageField(upload_to="account/images",null=True ,)



    def __str__(self):
        return self.name
