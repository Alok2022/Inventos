from django.contrib import admin

# Register your models here.
from . models import contact_table,Regist_table,prod_table,device_table,Track_table

admin.site.register(contact_table)
admin.site.register(Regist_table)
admin.site.register(prod_table)
admin.site.register(device_table)
admin.site.register(Track_table)
