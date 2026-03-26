from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('logo', 'Logo'),
        ('poster', 'Poster'),
        ('icon', 'Icon'),
    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta:
        model = Order
        fields = ['type', 'size', 'description', 'design_file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'design_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
