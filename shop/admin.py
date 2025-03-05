
from django.contrib import admin
from django.utils.html import format_html
from .models import Order, OrderItem, Car

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('get_brand', 'get_model', 'get_year', 'get_vin', 'quantity', 'price')

    def get_brand(self, obj):
        return obj.car.model.brand.name
    get_brand.short_description = 'Марка'

    def get_model(self, obj):
        return obj.car.model.name
    get_model.short_description = 'Модель'

    def get_year(self, obj):
        return obj.car.year
    get_year.short_description = 'Год выпуска'

    def get_vin(self, obj):
        return obj.car.vin
    get_vin.short_description = 'VIN-номер'

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('id', 'user', 'created_at', 'status', 'total_price')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)