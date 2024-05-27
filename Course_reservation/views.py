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
from django.db.models import Q  # 引入 Q 對象，用於複合查詢

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

# 預約結果頁面
def Course_reservation_result(request):
        template = loader.get_template('Reservation.html')
        
        # 篩選有完成預約的人
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")

        context = {
            "Course": reservationData,
        }
        return HttpResponse(template.render(context))

# 預約課程
def CourseReservation(request):
    template = loader.get_template('Course_reservation_result.html')
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

        # 篩選課程資料表裡有對到的第一筆資料
        CourseData = Course_reservation.objects.filter(Course_code=code).first()

        # # 判斷如果目前的人數大於預約人數的話
        # if  (CourseData.Current_number_applicants >= CourseData.Full_number_applicants) and  cancel != "True"  :
        #     reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")
        #     context = {
        #         "Course": reservationData,
        #     }
        #     # print(context["msg"])
        #     return HttpResponse(template.render(context))

        # 篩選歷史資料表裡的資料，用於確認有沒有預約過
        haveReservation = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).exists()

        # 檢查是否有衝堂
        conflicts = Course_reservation_history.objects.filter(
            week=CourseData.week,  # 先比對星期
            State='Appointment Confirmed',  # 並且狀態為CCC
            class_time_start__lt=CourseData.class_time_end,
            class_time_end__gt= CourseData.class_time_start
        ).exclude(
            # Q(Course_code=CourseData.Course_code) & Q(State='Cancelled')  # 複合查詢，排除課程代碼為DD且狀態為cancel的紀錄
            Course_code=CourseData.Course_code
        ).exists()

        if conflicts:
            print("課程時間衝突，請選擇其他時間。")
            context = {
                "msg" : "預約失敗，因課程時間衝突"
            }
            return HttpResponse(template.render(context))
        else:
            print("課程時間不衝突，成功預約")

            # 如果沒有被預約過
            if not haveReservation:
                # 加入新的資料到表裡面
                new_reservation = Course_reservation_history(
                    Period=f"{CourseData.Period}_{CourseData.Category}",
                    Course_code=CourseData.Course_code,
                    Coach_name=CourseData.Coach_name,
                    Student_id=request.user,
                    State = "Appointment Confirmed",
                    class_time_start = CourseData.class_time_start,
                    class_time_end = CourseData.class_time_end,
                    week= CourseData.week
                )
                # 儲存
                new_reservation.save()
                # msg = "Appointment Confirmed"

            # 如果被預約過，改狀態為預約
            else:
                historyData = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).first()
                # 如果目前為預約的話，就甚麼都不做，如果不是的話，把狀態改成預約
                if historyData.State == "Cancelled":
                    historyData.State = "Appointment Confirmed"
                    historyData.save()
                    # 課程人數+1
                    CourseData.Current_number_applicants = CourseData.Current_number_applicants + 1
                    CourseData.save()
                    # msg = "Appointment Confirmed"

        # 篩選有完成預約的人
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")

        # 篩選完放到context裡面
        context = {
            "Course": reservationData,
            "msg" : "預約成功"
            # "msg": msg
        }
        return HttpResponse(template.render(context))

    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")
        context = {
            "Course": reservationData,
            # "msg": msg
        }
        return HttpResponse(template.render(context))

# 取消預約課程
def Cancel_Course(request):
    template = loader.get_template('Reservation.html')
    data = {}
    # msg = ""
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
        if (CourseData.Current_number_applicants >= CourseData.Full_number_applicants) and cancel != "True":
            reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
                                                                        State="Appointment Confirmed")
            context = {
                "Course": reservationData,
                # "msg" : "Appointment Limit Reached"
            }
            # print(context["msg"])
            return HttpResponse(template.render(context))
        # 篩選歷史資料表裡的資料，用於確認有沒有預約過
        haveReservation = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).exists()

        historyData = Course_reservation_history.objects.filter(Student_id=request.user, Course_code=code).first()

        # 如果沒有被預約過
        if historyData.State == "Appointment Confirmed":
            historyData.State = "Cancelled"
            historyData.save()
            # 課程人數-1
            CourseData.Current_number_applicants = CourseData.Current_number_applicants - 1
            CourseData.save()
            # msg = "Cancelled"

        # 篩選有完成預約的人
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
                                                                    State="Appointment Confirmed")

        # 篩選完放到context裡面
        context = {
            "Course": reservationData,
            # "msg": msg
        }
        return HttpResponse(template.render(context))

    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
                                                                    State="Appointment Confirmed")
        context = {
            "Course": reservationData,
            # "msg": msg
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


# 取消預約確認頁面
def Course_Clear_check(request):
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")
        context = {
            "Course": reservationData,
        }
        return render(request, 'Course_Clear_check.html', context)



#
# def Course_Clear(request):
#     if request.method == 'POST':
#         # 更新所有狀態為 "Appointment Confirmed" 的預約記錄為 "Cancelled"
#         Course_reservation_history.objects.filter(State="Appointment Confirmed").update(State="Cancelled")
#
#         # 更新對應課程的人數
#         confirmed_reservations = Course_reservation_history.objects.filter(State="Cancelled")
#         for reservation in confirmed_reservations:
#             course = Course_reservation.objects.filter(Course_code=reservation.Course_code).first()
#             if course:
#                 course.Current_number_applicants = course.Current_number_applicants - 1
#                 course.save()
#         # 篩選有完成預約的人
#         reservationData = Course_reservation_history.objects.filter(Student_id=request.user,State="Appointment Confirmed")
#         # 篩選完放到context裡面
#         context = {
#             "Course": reservationData,
#             # "msg": msg
#         }
#         # 重定向回 index 頁面
#         return redirect('index')
#
#     # 加載 Course_reservation.html 頁面
#     return render(request, 'Course_reservation.html')

def Course_Clear(request):
    if request.method == 'POST':

        # 更新對應課程的人數
        confirmed_reservations = Course_reservation_history.objects.filter(State="Appointment Confirmed")

        for reservation in confirmed_reservations:
            course = Course_reservation.objects.filter(Course_code=reservation.Course_code).first()
            if course:
                course.Current_number_applicants = course.Current_number_applicants - 1
                course.save()

        # 更新所有狀態為 "Appointment Confirmed" 的預約記錄為 "Cancelled"
        Course_reservation_history.objects.filter(State="Appointment Confirmed").update(State="Cancelled")

        # 重定向回 index 頁面
        return redirect('index')

    else:
        # 顯示確認頁面
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
                                                                    State="Appointment Confirmed")
        context = {
            "Course": reservationData,
        }
        return render(request, 'Course_cancel.html', context)