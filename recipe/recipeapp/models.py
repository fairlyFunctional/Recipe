from django.db import models
from django.core.urlresolvers import reverse

#Ingredient Primitive
#--------------------------------------------------------------------
# This is here to allow the ingredient model to use the raw ingredient name only
class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

#Ingredient Model
#--------------------------------------------------------------------
#* Name
#* Quantity
#* Units
#  Super bonus item:
#  break the ingredients out, and add a search that lets me pick what i have in my house and shows what i can make ;)
class IngredientAmount(models.Model):
	CUP = 'C'
	GALLON = 'G'
	PINCH = 'p'
	TABLESPOON = 'T'
	TEASPOON = 't'
	UNIT_CHOICES = (
		(GALLON, 'Gallons'),
		(CUP, 'Cups'),
		(TABLESPOON, 'Tbsp'),
		(TEASPOON, 'tsp'),
		(PINCH, 'Pinch'))
	name = models.ForeignKey(Ingredient)
	quantity = models.FloatField()
	units = models.CharField(max_length=1,
		choices=UNIT_CHOICES)
	def __str__(self):
		return self.name.name

#Category Model
#--------------------------------------------------------------------
#* Name
#* Photo

class Category(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(blank=True)
	def __str__(self):
		return self.name
	def get_recipes(self):
		return Recipe.objects.filter(category=self)


#Recipe Model
#--------------------------------------------------------------------
#* Name
#* Author
#* Category (foreign key to category below)
#* Ingredient List (can just be a big text box)
#* Directions (can also just be a big text box)
#* Photo 

class Recipe(models.Model):
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	category = models.ForeignKey(Category)
	ingredients = models.ManyToManyField(IngredientAmount)
	directions = models.CharField(max_length=200)
	photo = models.ImageField(blank=True)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('recipe:detail', args={1,})

