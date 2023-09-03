from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
RESIDENCE_OWNED_CHOICES = (
    ('owned by parent/sibling','owned by parent/sibling'),
    ('owned by self/spouse','owned by self/spouse'),
    ('rented - staying alone','rented - staying alone'),
    ('rented with family','rented with family'),
)
EMPLOYMENT_DETAILS_CHOICES =(
    ('self employeed business','self employeed business'),
    ('self employeed professional','self employeed professional'),
)

ACCOUNTING_PROVIDER = (
    ('Xero','Xero'),
    ('MYOB','MYOB'),
)
class UserData(models.Model):
    userId = models.IntegerField(primary_key = True)
    firstName = models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    lastName = models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    city = models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    state = models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    pincode = models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    address =models.CharField(validators=[MinLengthValidator(3)], max_length=200, blank= False)
    email =  models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    residence_owned_by = models.CharField(choices=RESIDENCE_OWNED_CHOICES, max_length=100)
    employment_Details = models.CharField(choices=EMPLOYMENT_DETAILS_CHOICES , max_length=100)
    occupation =  models.CharField(validators=[MinLengthValidator(3)], max_length=100 , blank = False)
    def __str__(self):
        return self.firstName + ' ' +self.lastName;



class LoanCategory(models.Model):
    loan_name = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_name


class LoanRequest(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        LoanCategory, on_delete=models.CASCADE, null=True)
    request_date = models.DateField(auto_now_add=True)
    status_date = models.CharField(
        max_length=150, null=True, blank=True, default=None)
    reason = models.TextField()
    status = models.CharField(max_length=100, default='pending')
    amount = models.PositiveIntegerField(default =0)
    year = models.PositiveIntegerField(default=1)
    accounting_provider = models.CharField(choices= ACCOUNTING_PROVIDER , max_length=100)


