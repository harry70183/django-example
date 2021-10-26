from django.contrib import admin
from ashinne.models import Category, Mission
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_type', )
    list_fields = ('product_type', )

class MissionAdmin(admin.ModelAdmin):
    list_display = ('module_id','answer','product_type')
    list_fields = ('module_id','answer','product_type')
    list_filter = ('product_type',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Mission, MissionAdmin)