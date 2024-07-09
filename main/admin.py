from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.Sushi)
class SushiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}