from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course_reservation  # 導入您的模型
from .models import Course_reservation_history  # 導入您的模型

admin.site.register(Course_reservation)  # 註冊模型
admin.site.register(Course_reservation_history)  # 註冊模型
