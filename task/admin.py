from django.contrib import admin

# Register your models here.
from task.models import Todo, Product

# Register your models here.
admin.site.register(Todo)
admin.site.register(Product)
