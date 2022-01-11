from django.contrib import admin
from .models import(
    Region,Country,State,City,LocationData
)

# Register your models here.
admin.site.register(LocationData)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)