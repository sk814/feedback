from django.forms import ModelForm
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['company', 'Product', 'Service','Employee', 'Value', 'Recommendable', 'review']
        exclude = ['company', 'Product', 'Service','Employee', 'Value', 'Recommendable', 'review']

