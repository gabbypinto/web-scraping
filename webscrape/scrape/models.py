from django.db import models

# Create your models here. a way of modeling/grabbing info/adding attributes, etc..
class ShoppingList(models.Model):
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name

#the bottom class are the items contained in the list
class Item(models.Model):
	shoppinglist = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()
	#create a price variable
	def __str__(self):
		return self.text


#create a class that deals with input
