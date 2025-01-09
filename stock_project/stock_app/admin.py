from django.contrib import admin
from .models import StockItem

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('medicine', 'scope_quantity', 'available_quantity', 'net_consumed', 'week1', 'week2', 'week3', 'week4', 'week5', 'total')

    # Add a search bar for 'name' and 'category'
    search_fields = ('medicine', 'scope_quantity')

    # Add a filter by 'category'
    list_filter = ('scope_quantity',)

    # Optional: Add functionality to edit 'total' (this is more for convenience in the admin)
    # In case you need to allow modification of the 'total' field directly in the admin interface.
    # However, typically, 'total' is calculated, so you might want to avoid editing it directly.
    readonly_fields = ('total',)  # To prevent editing the 'total' directly

    # Optional: Customize the form used in the admin to add validation, if needed.
    # form = StockItemForm  # Uncomment if you want to use a custom form.
