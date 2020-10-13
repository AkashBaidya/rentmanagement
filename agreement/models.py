from django.db import models
from datetime import date
# from django.forms import ModelForm

# Create your modefrom django.db import models


class Site(models.Model):
    site_code= models.CharField(max_length=4)
    site_extension= models.IntegerField(max_length=20,blank=True,null=True)
    display_area=models.IntegerField(max_length=20,null=True,blank=True,help_text='size of the site in sft',default=0)
    storage_area_inside=models.IntegerField(max_length=20,null=True,blank=True, help_text='size of the site in sft')
    storage_area_outside=models.IntegerField(max_length=20,null=True,blank=True, help_text='size of the site in sft')
    lattitude=models.DecimalField(blank=True,null=True,max_digits=30,decimal_places=4)
    longitude=models.DecimalField(blank=True,null=True,max_digits=30,decimal_places=4)
    # CharField(max_length=20,unique=True)
    # site_description = models.CharField(max_length=450)
    site_size = models.IntegerField(max_length=100,help_text='size of the site in sft', null=True)
    district = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    site_type=models.CharField(max_length=20,choices=[
        ('SHOP', 'SHOP'),
        ('WAREHOUSE', 'WAREHOUSE'),
        ('SERVICE CENTER','SERVICE CENTER'),
        ('RESIDENT','RESIDENT'),
        ('STORE','STORE' ),
        ('OFFICE','OFFICE')])
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
        if str(self.site_extension)=='':
            return self.site_code
        else:
            return self.site_code+'-'+str(self.site_extension)



class Person(models.Model):
    name=models.CharField(max_length=100)
    person_type=models.CharField(max_length=30,choices=[
        ('Organization', 'Organization'),
        ('Individual', 'Individual'),
        ('Others','Others')])
    # type=models.CharField(verbose_name='Lessor type',max_length=30,
    # choices=[
    #     ('lessee', 'lessee'),
    #     ('lessor', 'lessor'),
    #     ('witness', 'witness')], )
    nid=models.CharField(verbose_name='NID',null=True,max_length=20,blank=True)
    tin=models.CharField(verbose_name='TIN',null=True,blank=True,max_length=20)
    email=models.CharField(max_length=40,null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    # address=models.CharField(max_length=450)
    dealing_person_status=models.CharField(max_length=10,verbose_name='Is there any dealing person other than lessor?', choices=[('Yes','Yes'),('No','No')])
    address=models.CharField(max_length=50,blank=True, null=True)
    sis_supplier_code=models.CharField(max_length=50,blank=True,default='RNT')
    name_of_dealing_person=models.CharField(max_length=50,blank=True,null=True)
    phone_number_of_dealing_person=models.CharField(max_length=50,blank=True,null=True)
    email_of_dealing_person=models.EmailField(max_length=30,blank=True,null=True)
    relationship=models.CharField(max_length=30,blank=True,null=True)
    division=models.CharField(max_length=40)
    district=models.CharField(max_length=40)
    thana=models.CharField(max_length=40)
    postcode=models.CharField(max_length=40)
    village=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Properties(models.Model):
    type=models.CharField(verbose_name='Availability',max_length=100,blank=True,null=True,choices=[
        ('available', 'available'),
        (' not available', ' not available')])
    desc=models.CharField(max_length=450, verbose_name='Address',blank=True,null=True)
    status=models.CharField(max_length=30, blank=True,null=True,choices=[
        ('active', 'active'),
        (' not active', ' not active')])

    property_size = models.IntegerField(max_length=100,help_text='size of the site in sft', blank=True,null=True)
    # area=models.CharField(max_length=20)
    # city=models.CharField(max_length=20)
    # district=models.CharField(max_length=20)
    # division=models.CharField(max_length=20)

    division=models.CharField(max_length=40,blank=True,null=True)
    district=models.CharField(max_length=40,blank=True,null=True)
    thana=models.CharField(max_length=40,blank=True,null=True)
    postcode=models.CharField(max_length=40,blank=True,null=True)
    village=models.CharField(max_length=40,blank=True,null=True)
    number_of_owner=models.IntegerField(max_length=20,choices=[
        (1, 1),
        (2, 2),
        (3,3),
        (4,4),
        (5,5 )])
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

    number_of_sites=models.IntegerField(max_length=20,choices=[
        (1, 1),
        (2, 2),
        (3,3),
        (4,4)])
    site1=models.ForeignKey(Site,on_delete=models.CASCADE,related_name='first_site')
    percentage_of_first_site=models.IntegerField(max_length=20)
    site2=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='second_site',null=True, blank=True)
    percentage_of_second_site=models.IntegerField(max_length=20,null=True,blank=True)
    site3=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='third_site',null=True, blank=True)
    percentage_of_third_site=models.IntegerField(max_length=20,null=True, blank=True)
    site4=models.ForeignKey(Site,on_delete=models.CASCADE, related_name='fourth_site',null=True, blank=True)
    percentage_of_fourth_site=models.IntegerField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.division+' '+self.district+' '+self.thana+' '+self.village


class Agreement(models.Model):
    id= models.IntegerField(max_length=10000000, primary_key=True),
    agrm_id=models.CharField(max_length=30,null=True,blank=True,default="hello")
    agreement_date = models.DateField(null=True,blank=True)
    # tenure_year=models.IntegerField()
    effected_date_as_actual= models.DateField(null=True,blank=True,verbose_name='Effective date as actual')
    effected_date_as_per_agreement = models.DateField(null=True,blank=True,verbose_name='Effective date as per agreement')
    expiry_date = models.DateField(null=True,blank=True,verbose_name='Expiry date')
    tenure_month=models.IntegerField(null=True,blank=True)
    agreement_cat_type=models.CharField(verbose_name='Agreement category type',max_length=30,choices=[
        ('Relocation', 'Relocation'),
        ('New', 'New'),
        ('Renewal','Renewal'),
        ('Extension','Extension')])
    termination_clause=models.CharField(max_length=70,choices=[
            ('Both parties agree to uninterrupted tenancy period', 'Both parties agree to uninterrupted tenancy period'),
            ('Both parties negotiator', 'Both parties negotiator'),

            ('Both parties  1 month  prior written notice','Both parties  1 month  prior written notice'),
            ('Both parties  2 month  prior written notice','Both parties  2 month  prior written notice'),
            ('Both parties  3 month  prior written notice','Both parties  3 month  prior written notice'),
            ('Both parties  4 month prior written notice','Both parties  4 month prior written notice'),
            ('Both parties  6 month prior written notice','Both parties  6 month prior written notice'),
            ('Lessee  only 1 month prior written notice','Lessee  only 1 month prior written notice'),
            ('Lessee  only 3 month prior written notice','Lessee  only 3 month prior written notice'),
            ('Lessee  only 4 month prior written notice','Lessee   only 4 month prior written notice'),
            ('Lessee  only 6 month prior written notice','Lessee  only 6 month prior written notice'),
            ('Possesion Purchase','Possesion Purchase')])



    notice_date = models.DateField(null=True,verbose_name='Notice date')
    notice_period = models.CharField(max_length=2)
    file_no=models.CharField(max_length=7)
    total_months=models.IntegerField(default=1)
    serial_no=models.CharField(max_length=8)
    main_site=models.ForeignKey(Site,on_delete=models.CASCADE)
    agreement_advance_amount=models.DecimalField(verbose_name='Advance/Prepaid(BDT)',null=True,max_digits=30,decimal_places=4)
    agreement_security_amount=models.DecimalField(verbose_name='Security Deposit(BDT)',null=True,max_digits=30,decimal_places=4)
    employee_id=models.CharField(max_length=10,blank=True)
    employee_name=models.CharField(max_length=30,blank=True)
    employee_designation=models.CharField(max_length=50,blank=True)
    employee_phone_number=models.CharField(max_length=15,blank=True)
    employee_email=models.EmailField(max_length=30,blank=True)
    status=models.CharField(max_length=10,blank=True)
    interest_rate=models.DecimalField(null=True,max_digits=30,decimal_places=4)
    properties=models.ForeignKey(Properties,on_delete=models.CASCADE,blank=True)

    # def __str__(self):
    #     return self.agrm_id

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


class SingerArea(models.Model):
    district=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
class LocalArea(models.Model):
    division=models.CharField(max_length=40)
    district=models.CharField(max_length=40)
    thana=models.CharField(max_length=40)
    postcode=models.CharField(max_length=40)
    village=models.CharField(max_length=40)
