from django.db import models
from datetime import date
# from django.forms import ModelForm

# Create your modefrom django.db import models


class Site(models.Model):
    site_code= models.CharField(max_length=30)
    site_ext= models.CharField(max_length=20,blank=True)
    primary_area=models.IntegerField(max_length=20,blank=True)
    secondary_area=models.IntegerField(max_length=20,blank=True)
    tertiary_area=models.IntegerField(max_length=20,blank=True)
    # CharField(max_length=20,unique=True)
    site_desc = models.CharField(max_length=450)
    site_size = models.IntegerField(max_length=100,help_text='size of the site in ft', null=True)
    district = models.CharField(max_length=20)
    site_type=models.CharField(max_length=20)
    last_modified_by=models.CharField(max_length=20,blank=True)
    # last_modified_date=models.DateField(blank=True)
    # branch_manager = models.CharField(max_length=100)

    # category = models.CharField(max_length=200,choices=[
    #     ('site_allocation', 'site_allocation'),
    #     ('renew', 'renew')
    #
    # ])


    # quantity = models.CharField(max_length=20)
    # model_code = models.CharField(max_length=20,null=True)
    entry_date = models.DateField(null=True)

    # address=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.site_code+self.site_ext



class Person(models.Model):
    name=models.CharField(max_length=100)
    person_type=models.CharField(max_length=30,choices=[
        ('organization', 'organization'),
        ('person', 'person')])
    type=models.CharField(max_length=30,
    choices=[
        ('lessee', 'lessee'),
        ('lessor', 'lessor'),
        ('witness', 'witness')])
    nid=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=450)
    hasbankinfo=models.CharField(max_length=50)
    sis_supplier_code=models.CharField(max_length=50,blank=True)
    name_of_dealing_person=models.CharField(max_length=50,blank=True)
    phone_number_of_dealing_person=models.CharField(max_length=50,blank=True)
    email_of_dealing_person=models.EmailField(max_length=30,blank=True)
    relationship=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name

class Properties(models.Model):
    type=models.CharField(max_length=100)
    desc=models.CharField(max_length=450)
    status=models.CharField(max_length=30)
    area=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    property_size = models.IntegerField(max_length=100,help_text='size of the site in ft', null=True)
    district=models.CharField(max_length=20)
    division=models.CharField(max_length=20)
    owner1=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='first_person')
    percentage_of_first_owner=models.IntegerField()
    owner2=models.ForeignKey(Person,on_delete=models.CASCADE, related_name='second_person',null=True, blank=True)
    percentage_of_second_owner=models.IntegerField(max_length=20,null=True, blank=True)
    owner3=models.ForeignKey(Person,on_delete=models.CASCADE, related_name='third_person',null=True, blank=True)
    percentage_of_third_owner=models.IntegerField(max_length=20,null=True, blank=True)
    owner4=models.ForeignKey(Person,on_delete=models.CASCADE, related_name='fourth_person',null=True, blank=True)
    percentage_of_fourth_owner=models.IntegerField(max_length=20,null=True, blank=True)
    owner5=models.ForeignKey(Person,on_delete=models.CASCADE, related_name='fifth_person',null=True, blank=True)
    percentage_of_fifth_owner=models.IntegerField(max_length=20,null=True, blank=True)
    site1=models.ForeignKey(Site,on_delete=models.CASCADE,related_name='first_site')
    percentage_of_first_site=models.IntegerField(max_length=20)
    site2=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='second_site',null=True, blank=True)
    percentage_of_second_site=models.IntegerField(max_length=20,null=True)
    site3=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='third_site',null=True, blank=True)
    percentage_of_third_site=models.IntegerField(max_length=20,null=True, blank=True)
    site4=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='fourth_site',null=True, blank=True)
    percentage_of_fourth_site=models.IntegerField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.desc


class Agreement(models.Model):
    id= models.IntegerField(max_length=10000000, primary_key=True),
    agrm_id=models.CharField(max_length=10,unique=True)
    agrm_create_date = models.DateField(null=True)
    # tenure_year=models.IntegerField()
    tenure_month=models.IntegerField()
    eff_date = models.DateField(null=True)
    exp_date = models.DateField(null=True)
    notice_date = models.DateField(null=True)
    notice_period = models.CharField(max_length=2)
    file=models.CharField(max_length=7)
    total_months=models.IntegerField(default=1)
    file_no=models.CharField(max_length=8)
    main_site=models.ForeignKey(Site,on_delete=models.CASCADE)
    agrement_advance_amount=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    agrement_security_amount=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    employee_id=models.CharField(max_length=10,blank=True)
    employee_name=models.CharField(max_length=30,blank=True)
    employee_designation=models.CharField(max_length=50,blank=True)
    employee_phone_number=models.CharField(max_length=15,blank=True)
    employee_email=models.EmailField(max_length=30,blank=True)
    status=models.CharField(max_length=10,blank=True)
    interest_rate=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    properties=models.ForeignKey(Properties,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.agrm_id

    # first_witness=models.ForeignKey(Person,on_delete=models.CASCADE)
    # maturity=models.Datefield(null=True)
# class Rent(models.Model):
#     rent_id=models.CharField(max_length=10)
#     from_date=models.DateField(null=True)
#     to_date=models.DateField(null=True)
#     total_amount=models.IntegerField(null=True)
#     agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE)

class Rentline(models.Model):
    rent_rule_no=models.CharField(max_length=10)
    start_period=models.DateField(null=True)
    end_period=models.DateField(null=True)
    rent_per_month=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    total_months=models.IntegerField()
    advance_agreement_per_month=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    # total_amount=models.IntegerField(null=True)
    agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE,related_name='rentline',null=True, blank=True)

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
    advance_adjustment_rule_no=models.CharField(max_length=10)
    star_period=models.DateField(null=True)
    end_period=models.DateField(null=True)
    # total_amount=models.IntegerField(null=True)
    advance_adjustment_per_month=models.IntegerField(null=True)
    agreement_ref=models.ForeignKey(Agreement,on_delete=models.CASCADE,related_name='advanceline',null=True, blank=True)
