from import_export import resources
from .models import LocalArea
from .models import SingerArea

class LocalAreaResource(resources.ModelResource):
    class Meta:
        model = LocalArea

class SingerAreaResource(resources.ModelResource):
    class Meta:
        model = SingerArea
