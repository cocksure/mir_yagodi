from django import forms
from .models import Orders, Categories, Berries


class OrderBerryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    berry = forms.ModelChoiceField(queryset=Berries.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.all()
        self.fields['berry'].queryset = Berries.objects.all()

    class Meta:
        model = Orders
        fields = ('category', 'berry', 'amount', 'address', 'comment')


