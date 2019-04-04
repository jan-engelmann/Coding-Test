from django import forms

class AmountForm(forms.Form):
    EURO = 'EUR'
    USDOLLAR = 'USD'
    YEN = 'YPY'
    CURRENCY_CHOICES = (
        (EURO, 'Euro'),
        (USDOLLAR, 'US-Dollar'),
        (YEN, 'Japanese-Yen'),
    )
    amount = forms.FloatField()
    from_curr = forms.ChoiceField(choices=CURRENCY_CHOICES)
    to_curr = forms.ChoiceField(choices=CURRENCY_CHOICES)