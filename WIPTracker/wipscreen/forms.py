from django.forms import ModelForm
from .models import Order,ReelEntry

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class EntryForm(ModelForm):
    class Meta:
        model = ReelEntry
        fields = '__all__'