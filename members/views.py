from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Member
from .forms import SurveyForm

def master_html(request):
    master = "master.html"
    if (request.user.username[:4] == "v2-1"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v2-2"):
        master = 'master_v2_2.html'
    elif (request.user.username[:4] == "v3-1"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v3-2"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v4-1"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v4-2"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v5-1"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v5-2"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v6-1"):
        master = 'master_v6_1.html'
    elif (request.user.username[:4] == "v6-2"):
        master = 'master_v6_2.html'
    elif (request.user.username[:4] == "v7-1"):
        master = 'master_v7_1.html'
    elif (request.user.username[:4] == "v7-2"):
        master = 'master_v7_2.html'
    elif (request.user.username[:4] == "v8-1"):
        master = 'master_v8_1.html'
    elif (request.user.username[:4] == "v8-2"):
        master = 'master_v8_2.html'
    elif (request.user.username[:4] == "v9-1"):
        master = 'master_v2_1.html'
    elif (request.user.username[:4] == "v9-2"):
        master = 'master_v2_1.html'
    return master;

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'remind.html', {'form': form})
    else:
        form = SurveyForm()

    return render(request, 'survey_view.html', {'form': form})

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



def remind_v1_2(request):
    print ('remind_v1_2 is called')
    template = loader.get_template('remind_v1_2.html')
    return HttpResponse(template.render())



def main(request):
    print ('main is called')

    master = master_html(request)

    context = {'master': master}
    template = 'main.html'
    return render(request, template, context)



def testing(request):
    template = loader.get_template('template.html')
    context = {
      'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))