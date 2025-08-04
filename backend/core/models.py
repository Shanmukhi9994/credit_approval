from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15)
    monthly_income = models.IntegerField()
    approved_limit = models.IntegerField()
    current_debt = models.IntegerField(default=0)

class Loan(models.Model):
    customer = models.ForeignKey(Customer, related_name="loans", on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    tenure = models.IntegerField()
    interest_rate = models.FloatField()
    monthly_repayment = models.FloatField()
    emis_paid_on_time = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
