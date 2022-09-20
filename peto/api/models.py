from django.db import models
class PetoCreate(models.Model):
    petname=models.CharField(max_length=100,null=True)
    species=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=150,null=True)
    age=models.CharField(max_length=10,null=True)
    image=models.ImageField(upload_to="api/images/",null=True )



    def __str__(self):
        return self.petname



