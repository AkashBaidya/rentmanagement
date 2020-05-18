from django import forms

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
        fields = ['site_code', 'site_ext','site_desc','district','site_type','branch_manager','comments','entry_date']
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'person_type','type','nid','email','phone','address','hasbankinfo']
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['type', 'desc','status','area','city','district','division','person']
class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ['agrm_id','agrm_create_date', 'tenure_year','tenure_month','eff_date','exp_date','notice_date','notice_period','file','file_no','contact_person']

class RentlineForm(forms.ModelForm):
    class Meta:
        model = Rentline
        fields = ['rent_line_id','from_line_date','to_line_date','total_line_amount','agreement_ref']
class SecuritylineForm(forms.ModelForm):
    class Meta:
        model = Securityline
        fields = ['security_line_id','from_line_date','to_line_date','total_line_amount','agreement_ref']
class AdvancePaymentlineForm(forms.ModelForm):
    class Meta:
        model = AdvancePaymentline
        fields = ['advance_payment_line_id','from_line_date','to_line_date','total_line_amount','agreement_ref']
