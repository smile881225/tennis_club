from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course_reservation , Course_reservation_history
from .filters import Course_reservation_Filter
from django.contrib import messages
from django.shortcuts import redirect

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
    data = {}
    print(request.GET.get('code'))
    if not  request.user.is_authenticated:
        print(request.user)
        return redirect('/login/')
    try:
        # urid = request.GET['user_id']
        # urpass = request.GET['user_pass']
        code = request.GET.get('code')
        print(code)
        data = Course_reservation.objects.filter(Course_code=code)
        for i in data :
            print(i)
        context = {
        "Course" : data
            }
        return HttpResponse(template.render(context))
    except:
        urid = None
        context = {
        "Course" : data
            }
        return HttpResponse(template.render(context))

def first_stage(request):
    template = loader.get_template('first_stage.html')
    return HttpResponse(template.render())
def second_stage(request):
    template = loader.get_template('second_stage.html')
    return HttpResponse(template.render())
def third_stage(request):
    template = loader.get_template('third_stage.html')
    return HttpResponse(template.render())


def CourseReservation(request):
    template = loader.get_template('Reservation.html')
    data = {}
    try:
        code = request.GET.get('code')
        data = Course_reservation.objects.filter(Course_code=code).first()
        haveReservation = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).exists()

        if not haveReservation:
            new_reservation = Course_reservation_history(
                Period=f"{data.Period}_{data.Category}",
                Course_code=data.Course_code,
                Student_id=request.user
            )
            new_reservation.save()
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user)
        context = {
            "Course": reservationData
        }
        return HttpResponse(template.render(context))
    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user)
        context = {
            "Course": reservationData
        }
        return HttpResponse(template.render(context))