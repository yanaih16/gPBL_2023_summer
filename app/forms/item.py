from django import forms

class ItemAdd(forms.Form):
    name = forms.CharField(max_length=255, help_text='商品名')
    text = forms.CharField(help_text='商品説明', widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))
    value = forms.IntegerField( help_text='価格')
    image = forms.FileField(help_text="商品画像")