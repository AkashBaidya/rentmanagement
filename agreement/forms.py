
# from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from bootstrap_datepicker_plus import DatePickerInput



from .models import Site
from .models import Person
from .models import Properties
from .models import Agreement
from .models import Rentline
from .models import Securityline
from .models import AdvancePaymentline

class SiteForm(forms.ModelForm):
    site_code = forms.CharField(widget=forms.HiddenInput)
    # site_extension=forms.IntegerField(widget=forms.HiddenInput)
    display_area=forms.IntegerField(widget=forms.HiddenInput)
    storage_area_inside=forms.IntegerField(widget=forms.HiddenInput)
    storage_area_outside=forms.IntegerField(widget=forms.HiddenInput)
    lattitude=forms.DecimalField(widget=forms.HiddenInput)
    longitude=forms.DecimalField(widget=forms.HiddenInput)
    # entry_by=forms.CharField(widget=forms.HiddenInput)
    site_size=forms.IntegerField(widget=forms.HiddenInput)
    district=forms.CharField(widget=forms.HiddenInput)
    area=forms.CharField(widget=forms.HiddenInput)
    site_type=forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Site
        fields = ['site_code','display_area','storage_area_inside','storage_area_outside','lattitude','longitude','site_size','district','area','site_type']


class SiteEditForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ['site_code','site_extension','display_area','storage_area_inside','storage_area_outside','lattitude','longitude','site_size','district','area','site_type']

class PersonForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.HiddenInput)
    # person_type=forms.CharField(widget=forms.HiddenInput)
    # nid=forms.CharField(widget=forms.HiddenInput)
    # tin=forms.CharField(widget=forms.HiddenInput)
    # email=forms.CharField(widget=forms.HiddenInput)
    # phone=forms.CharField(widget=forms.HiddenInput)
    # dealing_person_status=forms.CharField(widget=forms.HiddenInput)
    # hasbankinfo=forms.CharField(widget=forms.HiddenInput)
    # sis_supplier_code=forms.CharField(widget=forms.HiddenInput)
    # name_of_dealing_person=forms.CharField(widget=forms.HiddenInput)
    # phone_number_of_dealing_person=forms.CharField(widget=forms.HiddenInput)
    # email_of_dealing_person=forms.CharField(widget=forms.HiddenInput)
    # relationship=forms.CharField(widget=forms.HiddenInput)
    # division=forms.CharField(widget=forms.HiddenInput)
    # district=forms.CharField(widget=forms.HiddenInput)
    # thana=forms.CharField(widget=forms.HiddenInput)
    # village=forms.CharField(widget=forms.HiddenInput)
    # postcode=forms.CharField(widget=forms.HiddenInput)


    class Meta:
        model = Person
        fields = []



class PersonEditForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name','person_type','nid','tin','email','phone','dealing_person_status','address','sis_supplier_code','name_of_dealing_person','phone_number_of_dealing_person','email_of_dealing_person','division','district','thana','postcode','village']

class PropertyForm(forms.ModelForm):
    type=forms.CharField(widget=forms.HiddenInput,required=False)
    desc=forms.CharField(widget=forms.HiddenInput,required=False)
    status=forms.CharField(widget=forms.HiddenInput,required=False)

    # property_size=forms.IntegerField(widget=forms.HiddenInput)

    division=forms.CharField(widget=forms.HiddenInput,required=False)
    district=forms.CharField(widget=forms.HiddenInput,required=False)
    thana=forms.CharField(widget=forms.HiddenInput,required=False)
    postcode=forms.CharField(widget=forms.HiddenInput,required=False)
    village=forms.CharField(widget=forms.HiddenInput,required=False)

    class Meta:
        model = Properties
        # fields=['']
        #fields = ['type','desc','status','division','district','thana','postcode','village','property_size','number_of_owner','owner1','percentage_of_first_owner','owner2','percentage_of_second_owner','owner3','percentage_of_third_owner','owner4','percentage_of_fourth_owner','owner5','percentage_of_fifth_owner','number_of_sites','site1','percentage_of_first_site','site2','percentage_of_second_site','site3','percentage_of_third_site','site4','percentage_of_fourth_site']
        fields = ['property_size','number_of_owner','owner1','percentage_of_first_owner','owner2','percentage_of_second_owner','owner3','percentage_of_third_owner','owner4','percentage_of_fourth_owner','owner5','percentage_of_fifth_owner','number_of_sites','site1','percentage_of_first_site','site2','percentage_of_second_site','site3','percentage_of_third_site','site4','percentage_of_fourth_site']
        # def clean_recipients(self):
        #     site1 = self.cleaned_data['site1']
        #     print("hello")
        #
        #     sep = '-'
        #     rest = site1.split(sep, 1)[0]
        #     site2=self.cleaned_data['site2']
        #     site3=self.cleaned_data['site3']
        #     site4=self.cleaned_data['site4']
        #     property_size=self.cleaned_data['property_size']
        #
        #     print(site1)
        #
        #     s1=Site.objects.get(site_code__contains==rest).aggregate(Sum('site_size'))
        #
        #     print(s1)
        #
        #     if s1!=property_size:
        #         raise forms.ValidationError("You have forgotten about Fred!")
        #     return None

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
class PropertyEditForm(forms.ModelForm):
    class Meta:
        model=Properties
        fields = ['type','desc','status','division','district','thana','postcode','village','property_size','number_of_owner','owner1','percentage_of_first_owner','owner2','percentage_of_second_owner','owner3','percentage_of_third_owner','owner4','percentage_of_fourth_owner','owner5','percentage_of_fifth_owner','number_of_sites','site1','percentage_of_first_site','site2','percentage_of_second_site','site3','percentage_of_third_site','site4','percentage_of_fourth_site']

class AgreementForm(forms.ModelForm):

    agrm_id=forms.CharField(widget=forms.HiddenInput,required=False)
    agreement_date=forms.DateField(widget=forms.HiddenInput,required=False)
    effected_date_as_actual=forms.DateField(widget=forms.HiddenInput,required=False)
    effected_date_as_per_agreement=forms.DateField(widget=forms.HiddenInput,required=False)
    expiry_date=forms.DateField(widget=forms.HiddenInput,required=False)
    total_months=forms.IntegerField(widget=forms.HiddenInput,required=False)
    agreement_cat_type=forms.CharField(widget=forms.HiddenInput,required=False)
    termination_clause=forms.CharField(widget=forms.HiddenInput,required=False)
    notice_date=forms.DateField(widget=forms.HiddenInput,required=False)
    notice_period=forms.CharField(widget=forms.HiddenInput,required=False)
    file_no=forms.CharField(widget=forms.HiddenInput,required=False)
    total_months=forms.CharField(widget=forms.HiddenInput,required=False)
    serial_no=forms.CharField(widget=forms.HiddenInput,required=False)
    agreement_advance_amount=forms.DecimalField(widget=forms.HiddenInput,label='Advance/Prepaid(BDT)',required=False)
    agreement_security_amount=forms.DecimalField(widget=forms.HiddenInput,label='Security Deposit(BDT)',required=False)
    employee_id=forms.CharField(widget=forms.HiddenInput,required=False)
    employee_name=forms.CharField(widget=forms.HiddenInput,required=False)
    employee_email=forms.EmailField(widget=forms.HiddenInput,required=False)
    employee_designation=forms.CharField(widget=forms.HiddenInput,required=False)
    employee_designation=forms.CharField(widget=forms.HiddenInput,required=False)
    properties=forms.ModelChoiceField(queryset=Properties.objects.all().filter(type__exact='available'),initial=0)

    # agrm_create_date=forms.DateField(input_formats=['%d %m-%Y'])
    # notice_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # agreement_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # effected_date_as_actual= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # effected_date_as_per_agreement= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # expiry_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    class Meta:
        model = Agreement
        fields = ['main_site','properties']

class AgreementEditForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ['agrm_id','agreement_date','effected_date_as_actual','effected_date_as_per_agreement','tenure_month','agreement_cat_type','termination_clause','notice_date','notice_period','file_no','total_months','serial_no','main_site','agreement_advance_amount','agreement_security_amount','employee_id','employee_name','employee_designation','employee_phone_number','employee_email','status','interest_rate','properties']

class RentlineForm(forms.ModelForm):
    start_period=forms.DateField(input_formats=['%m-%Y'])
    end_period=forms.DateField(input_formats=['%m-%Y'])
    # agreement_ref=forms.ChoiceField(widget=forms.HiddenInput())
    # print(RentlineForm)
    class Meta:
        model = Rentline
        fields = ['rent_rule_no','start_period','end_period','total_months','rent_per_month','advance_agreement_per_month']
        # widgets={
        #     'agreement_ref':RentlineForm.hiddenInput(),
        # }
class SecuritylineForm(forms.ModelForm):
    class Meta:
        model = Securityline
        fields = ['security_line_id','from_line_date','to_line_date','total_line_amount','agreement_ref']
class AdvancePaymentlineForm(forms.ModelForm):
    start_period=forms.DateField(input_formats=['%m-%Y'])
    end_period=forms.DateField(input_formats=['%m-%Y'])
    class Meta:
        model = AdvancePaymentline
        fields = ['advance_adjustment_rule_no','start_period','end_period','advance_adjustment_per_month']
