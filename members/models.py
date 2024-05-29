from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default= None, blank=True, null=True)

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    age = models.IntegerField(default=20)

    # 如果單純呼叫，就會回傳下面資料，django格式
    def __str__(self):
      return f"{self.firstname} {self.lastname}"

class Survey(models.Model):
    student_id = models.CharField(max_length=20, verbose_name='學號')
    choice_labels = [('1', '非常不同意'), ('2', '不同意'), ('3', '中等'), ('4', '同意'), ('5', '非常同意')]
    question_1 = models.CharField(max_length=1, choices=choice_labels, verbose_name='在任何時候，我很清楚系統目前的狀態如何？')
    question_2 = models.CharField(max_length=1, choices=choice_labels, verbose_name='在操作的過程中，網頁是否都有在合理的時間內做出回應？')
    question_3 = models.CharField(max_length=1, choices=choice_labels, verbose_name='可以從每個頁面返回主頁嗎？')
    question_4 = models.CharField(max_length=1, choices=choice_labels, verbose_name='是否能夠隨時取消和重做任何操作？')
    question_5 = models.CharField(max_length=1, choices=choice_labels, verbose_name='對於系統的錯誤訊息是否都清楚明瞭？')
    question_6 = models.CharField(max_length=1, choices=choice_labels, verbose_name='是否有清楚易懂的錯誤訊息？')
    question_7 = models.CharField(max_length=1, choices=choice_labels, verbose_name='對於任何介面，使用一致的配色？')
    question_8 = models.CharField(max_length=1, choices=choice_labels, verbose_name='對於任何介面，使用一致的排版？')
    question_9 = models.CharField(max_length=1, choices=choice_labels, verbose_name='網頁的排版設計遵循一般的網站標準嗎？')
    question_10 = models.CharField(max_length=1, choices=choice_labels, verbose_name='我在使用這個系統時，不需要記憶太多東西，就可以完成任務？')
    question_11 = models.CharField(max_length=1, choices=choice_labels, verbose_name='系統的顯示方式符合現實世界的習慣？')
    fill_in_1 = models.TextField(null=True,verbose_name='你認為此系統的 UX 有哪裡好的地方嗎？')
    fill_in_2 = models.TextField(null=True,verbose_name='你認為此系統的 UX 有哪裡不好的地方嗎？')
    fill_in_3 = models.TextField(null=True,verbose_name='給予系統的任何建議')
    def __str__(self):
        return self.student_id