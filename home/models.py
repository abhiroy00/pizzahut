from django.db import models

# Create your models here.


class PizzaModel( models.Model):
    
    pizzaImage= models.ImageField(upload_to='pizzahut/images/')
    pizzaName=models.CharField(max_length=100)
    pizzaPrice=models.IntegerField()
    pizzaDescription=models.TextField()
    pizzaOffer=models.BooleanField(default=False)
    pizzaOfferPrice=models.IntegerField(default=0)
    pizzaRetting=models.FloatField(default=0)
    Sizepizza = [
            ('Small', 'Pizza Small'), 
            ('Medium', 'Pizza Medium'), 
            ('Large', 'Pizza Large'), 
        ] 
    SizeList=models.CharField(max_length=100,choices=Sizepizza)
    pizzaType=models.CharField(choices=(('veg','veg'),('nonveg','nonveg')),max_length=10)
    pizzaKcal=models.IntegerField()
    
    
    
