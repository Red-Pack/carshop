# admin.py
from django.contrib import admin
from .models import Brand, CarModel, Car, CarImage


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 0

class CarAdmin(admin.ModelAdmin):
    list_display = ('get_brand', 'get_model', 'year', 'is_new', 'power_hp', 'transmission', 'drive', 'quantity')
    list_filter = ('model__brand', 'year', 'is_new', 'power_hp', 'drive', 'transmission', 'quantity')
    search_fields = ('vin', 'model__brand__name', 'model__name')
    inlines = [CarImageInline]


    def get_brand(self, obj):
        return obj.model.brand.name

    get_brand.short_description = 'Марка'

    def get_model(self, obj):
        return obj.model.name
    
    get_model.short_description = 'Модель'

admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
