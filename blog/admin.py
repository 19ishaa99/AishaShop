from django.contrib import admin

# Register your models here.
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = [
  # 'title ',
  'slug',
  # 'price',
  # 'description ',
  # 'created',
  # 'updated',
  ] # list_filter = ['description', 'title', 'price'] # list_editable = ['price', 'available'] # prepopulated_fields = {'slug': ('title',)}
  search_fields = ('name',) # ✅ Required for autocomplete_fields to work

