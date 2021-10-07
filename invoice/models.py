from django.db import models

class Invoice(models.Model):
    statusChoice = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Due', 'Due')
    ]
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.CharField(choices=statusChoice, max_length=20)
    def __str__(self):
        return self.customer
    
    def get_status(self):
        return self.status

class LineItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.invoice.customer
   