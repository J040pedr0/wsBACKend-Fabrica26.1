from django import forms
from .models import Collection

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),}