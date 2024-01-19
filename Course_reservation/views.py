from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course_reservation
from .filters import Course_reservation_Filter
from django.contrib import messages


def index(request):
    template = loader.get_template('test.html')
    Course_reservation_list = Course_reservation.objects.all()
    # 使用 distinct() 方法查询所有不重复的商品名称
    Period_list = Course_reservation.objects.values_list('Period', flat=True).distinct()
    Course_code_list = Course_reservation.objects.values_list('Course_code', flat=True).distinct()
    Category_list = Course_reservation.objects.values_list('Category', flat=True).distinct()

    # 過濾用
    course_reservation_Filter = Course_reservation_Filter(queryset=Course_reservation_list)

    if request.method == "POST":
        course_reservation_Filter = Course_reservation_Filter(request.POST, queryset=Course_reservation_list)

    context = {
        'Course_reservation_list': Course_reservation_list,
        'course_reservation_Filter': course_reservation_Filter,
        'Period_list': Period_list,
        'Course_code_list': Course_code_list,
        'Category_list': Category_list,
    }

    return HttpResponse(template.render(context, request))


def test_2(request):
    template = loader.get_template('test-2.html')
    return HttpResponse(template.render())


def Course_content(request):
    template = loader.get_template('Course_content.html')
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None
    return HttpResponse(template.render())

def first_stage(request):
    template = loader.get_template('first_stage.html')
    return HttpResponse(template.render())
def second_stage(request):
    template = loader.get_template('second_stage.html')
    return HttpResponse(template.render())
def third_stage(request):
    template = loader.get_template('third_stage.html')
    return HttpResponse(template.render())