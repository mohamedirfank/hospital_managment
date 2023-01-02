from django.contrib import admin
from .models import Department, Docter, Booking

# Register your models here.

admin.site.register(Department)
admin.site.register(Docter)

class BookingDetails(admin.ModelAdmin):
    list_display = ('id','p_name')

admin.site.register(Booking)
