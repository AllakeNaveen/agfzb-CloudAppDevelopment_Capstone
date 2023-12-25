from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'dealer_id', 'name', 'type', 'year')

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
