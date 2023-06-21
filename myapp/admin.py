from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)

class Bookingadmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phonenumber', 'p_email', 'doc_name', 'booking_date', 'booking_on')
admin.site.register(Booking, Bookingadmin)