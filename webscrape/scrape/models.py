from django.db import models
from django.contrib.auth.models import User

# Create your models here. a way of modeling/grabbing info/adding attributes, etc..
class ShoppingList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shoppingList", null=True) #every todo list create will be linked to a user
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

#the bottom class are the items contained in the list
class Item(models.Model):
	shoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	complete = models.BooleanField()
	#create a price variable
	def __str__(self):
		return self.text


#create a class that deals with input
