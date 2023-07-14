from django import forms
from .models import CustomUser, Categories, Berries, Orders2


class OrderBerryForm2(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    berry = forms.ModelChoiceField(queryset=Berries.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.all()
        self.fields['berry'].queryset = Berries.objects.all()

    class Meta:
        model = Orders2
        fields = ('category', 'berry', 'amount', 'address', 'phone_number', 'comment')


class OrderBerryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Имя'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Почта'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Адрес'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': 'Телефон номер'})
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Скажите что-то'})
    )

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'address', 'phone_number', 'comment')

