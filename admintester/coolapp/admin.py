from django.contrib import admin
from .models import Product,Category,Tag

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ( "price", "description", "name",)
    list_filter = ("category", "tag",)
class TagAdmin(admin.ModelAdmin):
    list_filter = ("barcode_num","test_field")
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("category","dummy_field")
admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin )
admin.site.register(Tag,TagAdmin)


'''
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)


'''

