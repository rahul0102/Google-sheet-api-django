from django import forms
# from django.contrib.admin.widgets import AdminDateWidget

from .models import Friend
from core.utils import (get_available_worksheets)

class FriendCreateForm(forms.ModelForm):
    date_of_birth = forms.DateField(help_text = "DD/MM/YY", input_formats = ['%d/%m/%y'])
    class Meta:
        model = Friend
        fields = ['firstname', 'lastname', 'date_of_birth','mobile_no', 'address', 'occupation']

    def __init__(self, *args, **kwargs):
        WORKSHEET_CHOICE = kwargs.pop('choices', None)
        super(FriendCreateForm, self).__init__(*args, **kwargs)
        # WORKSHEET_CHOICE = get_available_worksheets()
        self.fields['worksheet_title']=forms.CharField(label="Which Worksheet? ",widget= forms.Select(
            choices = WORKSHEET_CHOICE), required = False)
        # self.fields['date_of_birth'] = forms.DateField(help_text = "DD/MM/YYYY",input_formats = '%d/%m/%y')

class FriendListForm(forms.Form):

    def __init__(self, *args, **kwargs):
        WORKSHEET_CHOICE = kwargs.pop('choices', None)
        super(FriendListForm, self).__init__(*args, **kwargs)
        # WORKSHEET_CHOICE = get_available_worksheets()
        self.fields['worksheet_title']=forms.CharField(label="Which Worksheet? ",widget= forms.Select(
            choices = WORKSHEET_CHOICE), required = False)
