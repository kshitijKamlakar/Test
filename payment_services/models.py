from django.db import models

# Create your models here.
class Payment_Status(models.Model):

    id = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=50)
    sub_status = models.CharField(max_length=50)
    sub_purchase_data = models.DateTimeField(auto_now_add=True)
    price_id = models.CharField(max_length=50)
    
    def __init__(self,id,payment_method,customer_name,sub_status,price, status = None):
        super(Payment_Status, self).__init__()
        self.payment_method = payment_method
        self.customer_name = customer_name
        self.sub_status = sub_status
        self.price = price
        self.status = status

    class Meta:
        db_table = 'paymentStatus'
        app_label = 'paymentStatus'

    def store_payment_info(self):
        self.save()


