import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import StockItem
from .forms import ExcelUploadForm, StockItemForm

# View to upload the Excel file and create StockItem entries
def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)

            for _, row in df.iterrows():
                # Create the StockItem, number will auto-generate
                StockItem.objects.create(
                    medicine=row['Medicine'],
                    scope_quantity=row['Scope Quantity'],
                    available_quantity=row['Available Quantity'],
                    net_consumed=row['Net Consumed'],
                )
            return redirect('stock-list')
    else:
        form = ExcelUploadForm()

    return render(request, 'upload_excel.html', {'form': form})

# Class-based views for listing, creating, updating, and deleting stock items


class StockListView(ListView):
    model = StockItem
    template_name = 'stock_list.html'
    context_object_name = 'stocks'

    # Overriding get_context_data to call update methods before rendering
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # Call the update methods on all stock items
    #     stock_items = StockItem.objects.all()
    #     for item in stock_items:
    #         item.update_available_qty()  # Update available quantity
    #         item.update_price()  # Update price
    #
    #     # Optionally, you can pass a message indicating that the update occurred
    #     context['stock_update'] = "Stock quantities and prices updated!"
    #
    #     return context


from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import StockItem
from .forms import StockItemForm

class StockCreateView(CreateView):
    model = StockItem
    fields = ['medicine', 'scope_quantity', 'available_quantity', 'net_consumed', 'week1', 'week2', 'week3', 'week4', 'week5']
    template_name = 'stock_form.html'
    success_url = reverse_lazy('stock-list')


class StockUpdateView(UpdateView):
    model = StockItem
    fields = ['medicine', 'scope_quantity', 'available_quantity', 'net_consumed', 'week1', 'week2', 'week3', 'week4', 'week5']
    template_name = 'stock_form.html'
    success_url = reverse_lazy('stock-list')


class StockDeleteView(DeleteView):
    model = StockItem
    template_name = 'stock_confirm_delete.html'
    success_url = reverse_lazy('stock-list')

# View to create or update a stock item (used for manual form handling outside CBVs)
def create_or_update_stock_item(request, pk=None):
    if pk:
        stock_item = StockItem.objects.get(id=pk)
        form = StockItemForm(request.POST or None, instance=stock_item)
    else:
        stock_item = None
        form = StockItemForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        stock_item = form.save()

        # Call the update_total method to update the 'total' field.
        stock_item.update_total()

        return redirect('stock-list')  # Redirect to the list page or another page

    return render(request, 'stock_form.html', {'form': form})

import pandas as pd
from django.http import HttpResponse
from .models import StockItem

def download_excel(request):
    # Query all stock items from the database
    stock_items = StockItem.objects.all()

    # Prepare data for the DataFrame
    data = []
    for item in stock_items:
        data.append({
            'Medicine': item.medicine,
            'Scope Quantity': item.scope_quantity,
            'Available Quantity': item.available_quantity,
            'NET CONSUMED': item.net_consumed,
            'Week 1': item.week1,
            'Week 2': item.week2,
            'Week 3': item.week3,
            'Week 4': item.week4,
            'Week 5': item.week5,
            # 'Total': item.total
        })

    # Create a pandas DataFrame
    df = pd.DataFrame(data)

    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=stock_items.xlsx'

    # Use pandas to write the DataFrame to the response
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    return response