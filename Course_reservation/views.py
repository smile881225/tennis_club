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

# 課程總攬頁面
def index(request):
    master = master_html(request)
    if (request.user.username[:4] == "v2-1"):
        template = loader.get_template('Course_reservation_v2_1.html')
    elif (request.user.username[:4] == "v2-2"):
        template = loader.get_template('Course_reservation_v2_2.html')
    elif (request.user.username[:4] == "v3-1"):
        template = loader.get_template('Course_reservation_v2_2.html')
    elif (request.user.username[:4] == "v8-2"):
        template = loader.get_template('Course_reservation_v8_2.html')
    elif (request.user.username[:4] == "v9-1"):
        template = loader.get_template('Course_reservation_v2_1.html')
    elif (request.user.username[:4] == "v9-2"):
        template = loader.get_template('Course_reservation_v2_1.html')
    # elif (request.user.username[:4] == "v2-2"):
    #     template = loader.get_template('Course_content_v2_2.html')
    else:
        template = loader.get_template('Course_reservation_v2_2.html')
    Course_reservation_list = Course_reservation.objects.all()
    # 使用 distinct() 方法查询所有不重复的商品名称
    Period_list = Course_reservation.objects.values_list('Period', flat=True).distinct()
    Course_code_list = Course_reservation.objects.values_list('Course_code', flat=True).distinct()
    Category_list = Course_reservation.objects.values_list('Category', flat=True).distinct()

    reserved_course_codes = Course_reservation_history.objects.filter(Student_id=request.user.username, State="Appointment Confirmed").values_list('Course_code', flat=True)

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
        'master': master,
        'have_Reservation': 'color: crimson',
        'reserved_course_codes': reserved_course_codes,
    }

    return HttpResponse(template.render(context, request))


def test_2(request):
    template = loader.get_template('test-2.html')
    return HttpResponse(template.render())



def Course_content(request):
    master = master_html(request)
    if (request.user.username[:4] == "v3-2"):
        template = loader.get_template('Course_content_v3_2.html')
    elif (request.user.username[:4] == "v4-2"):
        template = loader.get_template('Course_content_v4_2.html')
    elif (request.user.username[:4] == "v5-2"):
        template = loader.get_template('Course_content_v5_2.html')
    elif (request.user.username[:4] == "v6-1"):
        template = loader.get_template('Course_content_v7_1.html')
    elif (request.user.username[:4] == "v6-2"):
        template = loader.get_template('Course_content_v7_1.html')
    elif (request.user.username[:4] == "v7-1"):
        template = loader.get_template('Course_content_v7_1.html')
    elif (request.user.username[:4] == "v7-2"):
        template = loader.get_template('Course_content_v7_1.html')
    else:
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
        print("code:"+code)
        data = Course_reservation.objects.filter(Course_code=code)
        for i in data:
            print(i)
        context = {
            "Course": data,
            'master': master
        }
        return HttpResponse(template.render(context))
    except:
        urid = None
        context = {
            "Course": data,
            'master': master
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
        master = master_html(request)
        if (request.user.username[:4] == "v2-1"):
            template = loader.get_template('Reservation_v2.html')
        elif (request.user.username[:4] == "v2-2"):
            template = loader.get_template('Reservation_v2.html')
        elif (request.user.username[:4] == "v8-2"):
            template = loader.get_template('Course_reservation_v8_2.html')
            return redirect('/Course_reservation/')
        elif (request.user.username[:4] == "v9-2"):
            template = loader.get_template('Reservation_v9_2.html')
        else:
            template = loader.get_template('Reservation.html')

        master=master_html(request)
        # 篩選有完成預約的人
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")

        context = {
            "Course": reservationData,
            'master': master
        }
        return HttpResponse(template.render(context))

# 預約課程
def CourseReservation(request):
    template = loader.get_template('Course_reservation_result.html')
    master = master_html(request)

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
            Student_id=request.user, # 自己的id
            week=CourseData.week,  # 先比對星期
            State='Appointment Confirmed',  # 並且狀態為 Appointment Confirmed
            class_time_start__lt=CourseData.class_time_end,
            class_time_end__gt= CourseData.class_time_start
        ).exclude(
            # Q(Course_code=CourseData.Course_code) & Q(State='Cancelled')  # 複合查詢，排除課程代碼為DD且狀態為cancel的紀錄
            Course_code=CourseData.Course_code
        )

        if conflicts.exists():
            print("課程時間衝突，請選擇其他時間。")
            print("我想預約的課程是：" + CourseData.Course_code + " 星期： "+str(CourseData.week)+"，時間:" + str(CourseData.class_time_start) + " - " + str(CourseData.class_time_end))
            for conflict in conflicts:
                print(f"衝突課程: {conflict.Course_code}，星期： {conflict.week} 時間: {conflict.class_time_start} - {conflict.class_time_end}")
            context = {
                "msg" : "Appointment failed, course time conflict",
                "master":master
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
            "msg" : "Appointment successful",
            "master": master
            # "msg": msg
        }
        return HttpResponse(template.render(context))

    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")
        context = {
            "Course": reservationData,
            "master": master
            # "msg": msg
        }
        return HttpResponse(template.render(context))

# 取消預約課程
def Cancel_Course(request):
    if (request.user.username[:4] == "v9-2"):
        template = loader.get_template('Reservation_v9_2.html')
    else:
        template = loader.get_template('Reservation.html')
    master = master_html(request)

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
                'master': master
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
            'master': master
            # "msg": msg
        }
        return HttpResponse(template.render(context))

    except:
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
                                                                    State="Appointment Confirmed")
        context = {
            "Course": reservationData,
            'master': master
            # "msg": msg
        }
        return HttpResponse(template.render(context))


def Course_search(request):
    master = master_html(request)
    cls = 'd-none'
    if (request.user.username[:4] == "v7-1"):
        template = loader.get_template('Course_search_v7_1.html')
    elif (request.user.username[:4] == "v7-2"):
        template = loader.get_template('Course_search_v7_2.html')
    else:
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
        cls = ''
    context = {
        'Course_reservation_list': Course_reservation_list,
        'course_reservation_Filter': course_reservation_Filter,
        'Period_list': Period_list,
        'Course_code_list': Course_code_list,
        'Category_list': Category_list,
        'master': master,
        'cls':cls
    }

    return HttpResponse(template.render(context, request))


# 取消預約確認頁面
def Course_Clear_check(request):
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user, State="Appointment Confirmed")
        master = master_html(request)
        context = {
            "Course": reservationData,
            'master': master
        }
        return render(request, 'Course_Clear_check.html', context)

def Course_Clear(request):
    if (request.user.username[:4] == "v8-2"):
        template = loader.get_template('Course_reservation_v8_2.html')
    elif (request.user.username[:4] == "v9-2"):
        template = loader.get_template('Reservation_v9_2.html')
    else :
        template = loader.get_template('Reservation.html')
    master = master_html(request)
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

        # 顯示確認頁面
        reservationData = Course_reservation_history.objects.filter(Student_id=request.user,State="Appointment Confirmed")

        context = {
                "Course": reservationData,
                'master': master
            }
        if (request.user.username[:4] == "v8-2"):
            return redirect('/Course_reservation/')
        else:
            return HttpResponse(template.render(context))
        # 重定向回 index 頁面
        # return render(request, 'Course_cancel.html', context)

    # else:
    #     # 顯示確認頁面
    #     reservationData = Course_reservation_history.objects.filter(Student_id=request.user,
    #                                                                 State="Appointment Confirmed")
    #     context = {
    #         "Course": reservationData,
    #         'master': master
    #     }
    #     return render(request, 'Course_cancel.html', context)