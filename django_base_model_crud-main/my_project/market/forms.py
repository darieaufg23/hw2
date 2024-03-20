from django.forms import ModelForm
# from django.forms.fields import 
from . models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = []
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['submit'] = False