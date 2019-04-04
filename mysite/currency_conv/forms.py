from django import forms

class AmountForm(forms.Form):
    EURO = 'EUR'
    USDOLLAR = 'USD'
    YEN = 'JPY'
    CURRENCY_CHOICES = (
        (EURO, 'Euro'),
        (USDOLLAR, 'US-Dollar'),
        (YEN, 'Japanese-Yen'),
    )
    START_CURRENCY = forms.ChoiceField(choices=CURRENCY_CHOICES)
    END_CURRENCY = forms.ChoiceField(choices=CURRENCY_CHOICES)
    AMOUNT = forms.FloatField()