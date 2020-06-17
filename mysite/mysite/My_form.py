from django.forms import Form
from django.forms import widgets
from django.forms import fields
 
class MyForm(Form):
    user = fields.CharField(
        widget=widgets.TextInput(attrs={'id': 'i1', 'class': 'c1'})
    )
 
    gender = fields.ChoiceField(
        choices=((1, '男'), (2, '女'),),
        initial=2,
        widget=widgets.RadioSelect
    )
 
    city = fields.CharField(
        initial=2,
        widget=widgets.Select(choices=((1,'上海'),(2,'北京'),))
    )
 
    pwd = fields.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True)
    )