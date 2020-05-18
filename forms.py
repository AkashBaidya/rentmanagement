from django import forms

from .models import Site
from .models import Person
from .models import Properties
from .models import Agreement

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
        fields = ['agrm_create_date', 'tenure_year','tenure_month','eff_date','exp_date','notice_date','notice_period','file','file_no','contact_person']
