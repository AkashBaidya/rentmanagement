
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
    class Meta:
        model = Site
        fields = []

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = []
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
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

class AgreementForm(forms.ModelForm):
    # agrm_create_date=forms.DateField(input_formats=['%d %m-%Y'])
    # notice_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # agreement_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # effected_date_as_actual= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # effected_date_as_per_agreement= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    # expiry_date= forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ))
    class Meta:
        model = Agreement
        fields = ['agrm_id','main_site','properties']


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
