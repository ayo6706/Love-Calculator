import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NameForm
def index(request):

    male = ''
    female = ''
    love = {}
    url = 'https://love-calculator.p.rapidapi.com/getPercentage'

    header = {
        "x-rapidapi-key": "your key",
        "x-rapidapi-host": "love-calculator.p.rapidapi.com"
    }

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            male = form.cleaned_data['male']
            female = form.cleaned_data['female']
            # ...
            # redirect to a new URL:

        query = {
            'fname': [],
            'sname': []
        }
        query['fname'].append(male)
        query['sname'].append(female)

        
        response = requests.get(url, headers=header, params=query).json()
        #
        # print(response)
        # print(male)
        # print(female)

        love = {
            'male': response['fname'],
            'female': response['sname'],
            'percentage': response['percentage'],
            'result': response['result'],
        }
        context = {'love': love, 'form': form}
        return render(request, 'main/result.html', context)



    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    context = {'love': love, 'form': form}
    return render(request, 'main/index.html', context)
