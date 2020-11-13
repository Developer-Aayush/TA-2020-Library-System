from django.db import models

# Create your models here.


class allInformation(models.Model):
    Book_name = models.CharField(max_length=1000)
    Authors_Name = models.CharField(max_length=1000)
    Publication_Name = models.CharField(max_length=1000, null=True)
    Book_Type = models.CharField(max_length=1000)
    Book_serial_Number = models.CharField(max_length=1000)
    Book_Price = models.IntegerField()
    Book_Added_Date_and_Time = models.DateTimeField(
        auto_now_add=True, null=True)
    Book_Quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.Book_name
