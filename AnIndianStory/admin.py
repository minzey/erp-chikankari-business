from django.contrib import admin
from .models import Assignment, Bill, Karigar, Product, Company
# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('challanid', 'product', 'karigar', 'assignmentdate', 'process', 'size', 'qty')
    list_filter = ('product__company', 'product__prodid', 'karigar__name', 'challanid', 'assignmentdate', 'process')
    search_fields = ('challanid', 'product__prodid', 'karigar__name', 'process')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('prodid', 'colour', 'fabric', 'photo')
    list_filter = ('company', 'prodid', 'colour', 'fabric')
    search_fields = ('prodid',)

admin.site.register(Karigar)
admin.site.register(Product, ProductAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Bill)
admin.site.register(Company)

