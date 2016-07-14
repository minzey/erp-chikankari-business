from django.contrib import admin
from .models import Assignment, Bill, Karigar, Product
# Register your models here.

admin.site.register(Karigar)
admin.site.register(Product)
admin.site.register(Assignment)
admin.site.register(Bill)

