from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ContactClient)
class ContactClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']







