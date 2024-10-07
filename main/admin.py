from django.contrib import admin


from main.models import Link, Product


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_arrears(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "city", "level", "supplier", "arrears", "created_at")
    list_filter = ("city",)
    search_fields = ("name",)
    actions = [clear_arrears,]
    list_display_links = ["supplier",]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_model", "release_date", "supplier")
    list_filter = ("supplier",)
    search_fields = ("name",)
    list_display_links = ["supplier"]