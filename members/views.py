from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Member
from .forms import SurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'remind.html', {'form': form})
    else:
        form = SurveyForm()

    return render(request, 'Questionnaire.html', {'form': form})

# def Questionnaire(request):
#     print ('Questionnaire is called')
#     template = loader.get_template('Questionnaire.html')
#     return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all()
    template = loader.get_template('all_members.html')
    context = {
      'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def remind(request):
    print ('remind is called')
    template = loader.get_template('remind.html')
    return HttpResponse(template.render())

def main(request):
    print ('main is called')
    template = loader.get_template('main.html')
    return HttpResponse(template.render())



def testing(request):
    template = loader.get_template('template.html')
    context = {
      'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))