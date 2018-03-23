from django import forms

from .models import Friend
from core.utils import (get_available_worksheets)

class FriendCreateForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        WORKSHEET_CHOICE = kwargs.pop('choices', None)
        super(FriendCreateForm, self).__init__(*args, **kwargs)
        # WORKSHEET_CHOICE = get_available_worksheets()
        self.fields['worksheet_title']=forms.CharField(label="Which Worksheet? ",widget= forms.Select(
            choices = WORKSHEET_CHOICE), required = False)

class FriendListForm(forms.Form):

    def __init__(self, *args, **kwargs):
        WORKSHEET_CHOICE = kwargs.pop('choices', None)
        super(FriendListForm, self).__init__(*args, **kwargs)
        # WORKSHEET_CHOICE = get_available_worksheets()
        self.fields['worksheet_title']=forms.CharField(label="Which Worksheet? ",widget= forms.Select(
            choices = WORKSHEET_CHOICE), required = False)
