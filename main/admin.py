from django.contrib import admin
from .models import Driver, Client, Order
# Register your models here.
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(Order)
