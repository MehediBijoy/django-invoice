from django.contrib import admin
from django.urls import path
from .views import InvoiceListView, createInvoice, generate_PDF, view_PDF, invoice_send

app_name = 'invoice'
urlpatterns = [
    path('', InvoiceListView, name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', generate_PDF, name='invoice-download'),
    path('invoice-send/<id>', invoice_send, name='invoice-send')
]
