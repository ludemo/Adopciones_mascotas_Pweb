from django.contrib import admin
from .models import Mascotas,Usuario
# Register your models here.
admin.site.register([Mascotas,Usuario])