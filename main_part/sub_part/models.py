from pyexpat import model
from django.db import models
from pymysql import Date

# Create your models here.
class contact_table(models.Model):
    your_name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email_id=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.your_name

class Regist_table(models.Model):
    username=models.CharField(max_length=100)
    email_id=models.EmailField()
    password=models.CharField(max_length=20)
    confrim_password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class prod_table(models.Model):
    Product_id=models.CharField(max_length=10)
    Product_name=models.CharField(max_length=100)
    Date_Time=models.DateField()
    Phone=models.CharField(max_length=50)
    Gender=models.CharField(max_length=100)
    Customer=models.CharField(max_length=200)
    Source=models.CharField(max_length=100)
    Inventos_Cust=models.CharField(max_length=20)
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.Customer

class device_table(models.Model):
    DeviceName=models.CharField(max_length=100)
    Product=models.CharField(max_length=100)
    ProductId=models.CharField(max_length=20)
    ManufacturingId=models.CharField(max_length=20)
    ManufactureDate=models.DateField()
    Comment=models.CharField(max_length=200)
    CustomerHelpLine=models.CharField(max_length=20)
    TotalProduct=models.CharField(max_length=500)

    def __str__(self):
        return self.DeviceName   

class Track_table(models.Model):
    ProductNo=models.CharField(max_length=10)
    ProductModel=models.CharField(max_length=50)
    ProductName=models.CharField(max_length=100)
    Customername=models.CharField(max_length=100)
    customerNo=models.CharField(max_length=10)
    Delivery_update=models.CharField(max_length=10)
    userText=models.TextField()   
    def __str__(self):
        return self.ProductName      
            
