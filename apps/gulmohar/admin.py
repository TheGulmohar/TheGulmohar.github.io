
# Register your models here.
from django.contrib import admin
from .models import Customer


# Register Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country')
admin.site.register(Customer, CustomerAdmin)
