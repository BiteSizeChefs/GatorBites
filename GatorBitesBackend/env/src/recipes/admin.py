from django.contrib import admin
from .models import Recipe, RecipeLike

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeLike)