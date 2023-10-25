# recipes/models.py
from django.db import models
from profiles.models import Profile
from django.core.validators import FileExtensionValidator

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, related_name='liked_recipes', blank=True)
    
    def __str__(self):
        return f"{self.title}-{self.created_at.strftime('%d-%m-%Y')}"

    def count_likes(self):
        return self.likes.count()

    def is_liked_by_user(self, user):
        return self.likes.filter(id=user.id).exists()

    def get_instruction_list(self):
        return self.instructions.split('\n')

    def get_ingredient_list(self):
        return self.ingredients.split('\n')

class RecipeLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.CharField(choices=(('Like', 'Like'), ('Unlike', 'Unlike')), max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.recipe}-{self.value}"

