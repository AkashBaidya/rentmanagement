
from django.contrib import admin
from .models import Site
from .models import Person
from .models import Properties
from .models import Agreement
# from .models import Rent
from .models import Rentline
# from .models import Security
from .models import Securityline
# from .models import AdvancePayment
from .models import AdvancePaymentline
from .models import LocalArea
from .models import SingerArea

from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User
# from django.apps import apps
# models = apps.get_models()

# for model in models:
    # admin.site.register(model)

@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    pass
    # def save_model(self,request,obj,form,change):
    #     if not obj.entry_by:
    #         obj.entry_by=request.user
    #     print("from site admin")
    #
    #     obj.save()

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Properties)
class PropertiesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Agreement)
class AgreementAdmin(ImportExportModelAdmin):
    pass

@admin.register(Rentline)
class RentlineAdmin(ImportExportModelAdmin):
    pass

@admin.register(AdvancePaymentline)
class AdvancePaymentlineAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Site)
# admin.site.register(Person)
# admin.site.register(Properties)
# admin.site.register(Agreement)
# admin.site.register(Rent)
# admin.site.register(Rentline)
@admin.register(LocalArea)
class LocalAreaAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(LocalArea)

@admin.register(SingerArea)
class SingerAreaAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(SingerArea)
# admin.site.register(Security)
admin.site.register(Securityline)
# admin.site.register(AdvancePayment)
# admin.site.register(AdvancePaymentline)
