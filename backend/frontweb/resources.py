from import_export import resources
from .models import Companie

class CompanieResource(resources.ModelResource):
    class Meta:
        model = Companie
        