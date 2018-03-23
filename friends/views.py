import json

from django.shortcuts import render
# from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Friend
from .forms import FriendCreateForm, FriendListForm
from core.utils import (
    get_credential,
    open_sheet,
    save_data_to_worksheet,
    get_data_after_row,
    get_available_worksheets,
)
# Create your views here.

sheet_url = "https://docs.google.com/spreadsheets/d/\
1pFdoDO1PPTLphVz_dBLY4lwR0RLL2wQOXjIZDIC4ZrY/edit?usp=sharing"
class FriendCreateView(View):
    def get(self, request, *args, **kwargs):
        WORKSHEET_CHOICE = get_available_worksheets()
        form = FriendCreateForm(choices = WORKSHEET_CHOICE)
        context = {
            'form': form,
        }
        return render(request, 'friends/create.html', context)

    def post(self, request, *args, **kwargs):

        # update the data to sheet
        WORKSHEET_CHOICE = get_available_worksheets()
        form = FriendCreateForm(request.POST, choices = WORKSHEET_CHOICE)
        # print(form.data)
        if form.is_valid():
            row_data=[]
            form_data = (form.cleaned_data)
            # print(form_data)
            form_data['date_of_birth'] = form.cleaned_data['date_of_birth']\
                .strftime('%x')
            title = form_data.pop('worksheet_title')

            for data in form_data.values():
                row_data.append(data)
            save_data_to_worksheet(row_data,
                worksheet_title = title)
            return HttpResponseRedirect(reverse('friends:list'))
        else:
            form = FriendCreateForm()
            context = {
                'form': form,
                'error_message':"Some error occured!"
            }
            return render(request, 'friends/create.html', context)



class FriendListView(View):

    def get(self, request, *args, **kwargs):
        #  get data from sheet
        WORKSHEET_CHOICE = get_available_worksheets()
        form = FriendListForm(choices= WORKSHEET_CHOICE)
        context = {
            'form':form,
        }
        return render(request, 'friends/list.html',context)

    def post(self, request, *args, **kwargs):

        form_data = request.POST
        title = form_data['worksheet_title']
        row_number = form_data['row_number'] or 1
        if row_number:
            row_number = int(row_number)
        friends_data = get_data_after_row(row = row_number,
            worksheet_title = title)
        context = {
            'friends_data':json.loads(friends_data),
        }
        return render(request, 'friends/list.html',context)
        # return HttpResponse("Some error-occured")

# class FriendCreateView(CreateView):
#     model = Friend
#     fields = '__all__'
#     template_name = 'friends/create.html'
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             print(form.data)
#
#         return None
