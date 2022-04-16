from django import forms


from django import forms

class Info(forms.Form):
    altura = forms.FloatField(max_value=3, help_text='Use . para separar', widget=forms.NumberInput(attrs={"class":"altura", "placeholder":"Digite sua altura.", "step": "0.01"}))
    peso = forms.FloatField( widget=forms.NumberInput(attrs={"class":"peso", "placeholder":"Digite seu peso."}))
