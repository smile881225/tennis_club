
from django.db import models

class Course_reservation(models.Model):
    Period = models.CharField(max_length=255,null=True,help_text="期別")
    Course_code = models.CharField(max_length=255,null=True,help_text="課程代碼")
    Time_start = models.DateField(null=True,help_text="開始日期")
    Time_end = models.DateField(null=True,help_text="結束日期")
    week_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    week=models.CharField(max_length=10, choices=week_choices, default='')
    # def week(self):
    #     self = self.weekday() + 1
    #     chinese_numbers = {
    #         1: '星期一',
    #         2: '星期二',
    #         3: '星期三',
    #         4: '星期四',
    #         5: '星期五',
    #         6: '星期六',
    #         7: '星期七',
    #     }
    #     return chinese_numbers[self]
    # week_day=models.CharField(max_length=10, editable = False, default='')
    # week_day.week()
    class_time_start=models.TimeField(null=True)
    class_time_end=models.TimeField(null=True)
    Classroom = models.CharField(max_length=255,null=True,help_text="教室")
    Category_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Master', 'Master'),
    ]
    Category = models.CharField(max_length=255,choices=Category_choices,null=True,help_text="課程等級")
    Coach_name = models.CharField(max_length=255,null=True,help_text="教練名子")
    Full_number_applicants = models.IntegerField(default=26,null=True,help_text="總共可報名的人數")
    Current_number_applicants = models.IntegerField(default=0,null=True,help_text="目前報名人數")
    Class_status_choices = [
        ('Registration Open', 'Registration Open'),#報名中
        (' Registration Closed', ' Registration Closed'),#報名已滿
        ('Cancelled ', 'Cancelled '),#停開
        ('On-site Registration Only', 'On-site Registration Only'),#僅現場報名
    ]

    Class_status = models.CharField(max_length=255,choices=Class_status_choices,null=True,help_text="班級狀態，報名中、報名已滿、停開、僅現場報名")

    # 如果單純呼叫，就會回傳下面資料，django格式
    def __str__(self):
        return f"{self.Period} {self.Course_code}"
    
    
    
class Course_reservation_history(models.Model):
    Period = models.CharField(max_length=255,null=True,help_text="期別")
    Course_code = models.CharField(max_length=255,null=True,help_text="課程代碼")
    Coach_name= models.CharField(max_length=255,null=True,help_text="教練名子")
    Student_id = models.CharField(max_length=255,null=True,help_text="學生帳號")
    Create_time = models.DateTimeField(auto_now_add=True,help_text="建立時間")
    class_time_start=models.TimeField(null=True)
    class_time_end=models.TimeField(null=True)
    week_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),

    ]
    week = models.CharField(max_length=10, choices=week_choices, default='')
    State =models.CharField(max_length=255,null=True,help_text="預約狀態，完成預約、已取消")


