from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Customer, SaleDeed , SettlementDeed


class SaleDeedAdmin(admin.ModelAdmin):
    list_display = "CustomerName"
    list_filter = 'CustomerName'

class SettlementDeedAdmin(admin.ModelAdmin):
    list_display = "CustomerName"
    list_filter = 'CustomerName'


class SaleDeedAdmin(admin.ModelAdmin):
    list_display = ('DocNo', 'ExecutedBy', 'FavourOf', 'LaterDate', 'SaidName', 'Property', 'To', 'BeforeSRO')
    list_filter = 'Customer'

class SaleDeedAdmin(admin.ModelAdmin):
    list_display = ('LaterDate', 'SaidName', 'ExecutedBy', 'Relation', 'Property', 'DocNo', 'BeforeSRO')
    list_filter = 'Customer'

admin.site.register(Customer)
admin.site.register(SaleDeed)
admin.site.register(SettlementDeed)
