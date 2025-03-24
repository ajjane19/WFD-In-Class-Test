from django.db import models
from django.utils import timezone
import datetime

from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
#PART C OF THE ASSIGNMENT

#ONE - SALES PERSON
class Salesperson(models.model):
    last_Name = models.CharField(max_length = 20)
    first_Name = models.CharField(max_length = 20)

#TWO MECHANIC
class Mechanic(models.model):
    last_Name = models.CharField(max_length = 20)
    first_Name = models.CharField(max_length = 20)

#THREE CAR
class Car(models.model):
    Car_ID = models.IntegerField(default=0)
    serial_Num = models.IntegerField(default=0)
    Make = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    colour = models.CharField(max_length = 20)
    year = models.DateTimeField('year')
    c_for_sale = models.CharField(max_length = 20)

#Creating customer
class Customer(models.model):
    customer_ID = models.IntegerField(default=0)
    last_Name = models.CharField(max_length = 20)
    first_Name = models.CharField(max_length = 20)
    PhoneNum = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    State_Province = models.CharField(max_length = 200)
    country = models.CharField(max_length = 25)
    postal_code = models.CharField(max_length = 200)

#Creating service
class Service(models.model):
    service_ID = models.IntegerField(default=0)
    service_Name = models.CharField(max_length = 20)
    hourlyRate = models.CharField(max_length = 20)
#FOUR SERVICE_TICKET  
class Service_TicketNum(models.model):
    Service_TicketID = models.IntegerField(default=0)
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)

#FIVE SERVICE MECHANIC
class ServiceMechanic(models.model):
    Service_TicketID = models.ForeignKey(Service_TicketNum, on_delete=models.CASCADE)
    first_Name = models.CharField(max_length = 20)

#SIX MECHANIC
class Mechanic(models.model):
    last_Name = models.CharField(max_length = 20)
    first_Name = models.CharField(max_length = 20)

# Creating a parts 
class Parts(models.model):
    part_ID = models.IntegerField(default=0)
    port_Num = models.IntegerField(default=0)
    description = models.CharField(max_length = 200)
    purchase_Price = models.CharField(max_length = 20)
    retail_Price = models.CharField(max_length = 20)
                                    
class partsUsed(models.model):
    part_ID = models.ForeignKey(Service_TicketNum, on_delete=models.CASCADE)
    Service_TicketID = models.ForeignKey(Service_TicketNum, on_delete=models.CASCADE)
    num_Used = models.IntegerField(default=0)
    price = models.CharField(max_length = 20)
