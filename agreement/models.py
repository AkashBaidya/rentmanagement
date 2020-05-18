from django.db import models
from datetime import date
# from django.forms import ModelForm

# Create your modefrom django.db import models


class Site(models.Model):
    site_code= models.CharField(max_length=30)
    site_ext= models.CharField(max_length=20)
    # CharField(max_length=20,unique=True)
    site_desc = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    site_type=models.CharField(max_length=20)
    branch_manager = models.CharField(max_length=100)
    comments = models.CharField(max_length=200)
    # quantity = models.CharField(max_length=20)
    # model_code = models.CharField(max_length=20,null=True)
    entry_date = models.DateField(null=True)

    # address=models.CharField(max_length=100,default="")



class Person(models.Model):
    name=models.CharField(max_length=100)
    person_type=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    nid=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    hasbankinfo=models.IntegerField(max_length=1)

    def __str__(self):
        return self.name

class Properties(models.Model):
    type=models.CharField(max_length=100)
    desc=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    area=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    division=models.CharField(max_length=20)
    person=models.ForeignKey(Person,on_delete=models.CASCADE)


class Agreement(models.Model):
    agrm_id=models.CharField(max_length=10)
    agrm_create_date = models.DateField(null=True)
    tenure_year=models.IntegerField()
    tenure_month=models.IntegerField()
    eff_date = models.DateField(null=True)
    exp_date = models.DateField(null=True)
    notice_date = models.DateField(null=True)
    notice_period = models.CharField(max_length=2)
    file=models.CharField(max_length=7)
    file_no=models.CharField(max_length=8)
    contact_person=models.ForeignKey(Person,on_delete=models.CASCADE)


    # first_witness=models.ForeignKey(Person,on_delete=models.CASCADE)
    # maturity=models.Datefield(null=True)
# class Rent(models.Model):
#     rent_id=models.CharField(max_length=10)
#     from_date=models.DateField(null=True)
#     to_date=models.DateField(null=True)
#     total_amount=models.IntegerField(null=True)
#     agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE)

class Rentline(models.Model):
    rent_line_id=models.CharField(max_length=10)
    from_line_date=models.DateField(null=True)
    to_line_date=models.DateField(null=True)
    total_line_amount=models.IntegerField(null=True)
    agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE,related_name='rentline')

# class Security(models.Model):
#     security_id=models.CharField(max_length=10)
#     from_date=models.DateField(null=True)
#     to_date=models.DateField(null=True)
#     total_amount=models.IntegerField(null=True)
#     agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE)

class Securityline(models.Model):
    security_line_id=models.CharField(max_length=10)
    from_line_date=models.DateField(null=True)
    to_line_date=models.DateField(null=True)
    total_line_amount=models.IntegerField(null=True)
    agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE,related_name='securityline')

# class AdvancePayment(models.Model):
#     advance_payment_id=models.CharField(max_length=10)
#     from_date=models.DateField(null=True)
#     to_date=models.DateField(null=True)
#     total_amount=models.IntegerField(null=True)
#     agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE)

class AdvancePaymentline(models.Model):
    advance_payment_line_id=models.CharField(max_length=10)
    from_line_date=models.DateField(null=True)
    to_line_date=models.DateField(null=True)
    total_line_amount=models.IntegerField(null=True)
    agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE,related_name='advanceline')
