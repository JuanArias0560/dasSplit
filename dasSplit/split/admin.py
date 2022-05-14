from django.contrib import admin
from .models import Payment,Pocket,Profile,Charge

admin.site.register(Payment)
admin.site.register(Charge)
admin.site.register(Pocket)
admin.site.register(Profile)
