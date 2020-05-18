
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
# from django.apps import apps
# models = apps.get_models()

# for model in models:
    # admin.site.register(model)
admin.site.register(Site)
admin.site.register(Person)
admin.site.register(Properties)
admin.site.register(Agreement)
# admin.site.register(Rent)
admin.site.register(Rentline)
# admin.site.register(Security)
admin.site.register(Securityline)
# admin.site.register(AdvancePayment)
admin.site.register(AdvancePaymentline)
