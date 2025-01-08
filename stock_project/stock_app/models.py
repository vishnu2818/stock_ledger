from django.db import models

class StockItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.IntegerField() #SCOPE QUANTITY
    quantity = models.IntegerField() #Avalaible Quantity
    price = models.DecimalField(max_digits=10, decimal_places=2) #NET CONSUMED

    # Week fields
    week1 = models.IntegerField(default=0)
    week2 = models.IntegerField(default=0)
    week3 = models.IntegerField(default=0)
    week4 = models.IntegerField(default=0)
    week5 = models.IntegerField(default=0)

    # Total field
    total = models.IntegerField(default=0, editable=False)

    def update_available_qty(self):
        # self.quantity = 0
        self.quantity = self.category - self.price
        print(self.category,self.price)
        # self.save()


    def update_price(self):
        # self.price = 0.0
        self.price = self.week1 + self.week2 + self.week3 + self.week4 + self.week5
        # self.save()


    def save(self, *args, **kwargs):
        self.update_price()
        self.update_available_qty()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
