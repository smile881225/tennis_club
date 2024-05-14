from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course_reservation, Course_reservation_history
from .filters import Course_reservation_Filter
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def index(request):
    template = loader.get_template('Course_reservation.html')
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
    if not request.user.is_authenticated:
        print(request.user)
        return redirect('/login/')
    try:
        # urid = request.GET['user_id']
        # urpass = request.GET['user_pass']
        code = request.GET.get('code')
        print(code)
        data = Course_reservation.objects.filter(Course_code=code)
        for i in data:
            print(i)
        context = {
            "Course": data
        }
        return HttpResponse(template.render(context))
    except:
        urid = None
        context = {
            "Course": data
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
    msg = ""
    cancel = False
    try:
        # 從 A 標籤的url拿到 code
        code = request.GET.get('code')
        try:
            cancel = request.GET.get('cancel')
        except:
            pass
        print(cancel)
        # 篩選課程資料表裡的第一筆資料
        CourseData = Course_reservation.objects.filter(Course_code=code).first()
        if  (CourseData.Current_number_applicants >= CourseData.Full_number_applicants) and  cancel != "True"  :
            reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="完成預約")
            context = {
                "Course": reservationData,
                "msg" : "預約已達上限"
            }
            print(context["msg"])
            return HttpResponse(template.render(context))
        # 篩選歷史資料表裡的資料，用於確認有沒有預約過
        haveReservation = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).exists()

        # 如果沒有被預約過
        if not haveReservation:
            # 加入新的資料到表裡面
            new_reservation = Course_reservation_history(
                Period=f"{CourseData.Period}_{CourseData.Category}",
                Course_code=CourseData.Course_code,
                Coach_name=CourseData.Coach_name,
                Student_id=request.user
            )
            # 儲存
            new_reservation.save()
            msg = "預約完成"
        else:
            historyData = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).first()

            if historyData.State == "完成預約":
                historyData.State = "已取消"
                historyData.save()
                # 課程人數-1
                CourseData.Current_number_applicants = CourseData.Current_number_applicants - 1
                CourseData.save()
                msg = "取消預約完成"
            else :
                historyData.State = "完成預約"
                historyData.save()
                # 課程人數+1
                CourseData.Current_number_applicants = CourseData.Current_number_applicants + 1
                CourseData.save()
                msg = "預約完成"


        # 篩選有完成預約的人
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="完成預約")

        # 篩選完放到context裡面
        context = {
            "Course": reservationData,
            "msg": msg
        }
        return HttpResponse(template.render(context))

    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="完成預約")
        context = {
            "Course": reservationData,
            "msg": msg
        }
        return HttpResponse(template.render(context))

def Course_search(request):
    template = loader.get_template('Course_search.html')
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
    return HttpResponse(template.render())
