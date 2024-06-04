指令
> venv\Scripts\activate.bat
> py manage.py runserver
> python manage.py makemigrations
> python manage.py migrate
# version bind_user
> cd /home/selab/tennis_club
> source venv/bin/activate
> sudo systemctl restart apache2
> sudo tail -f /var/log/apache2/error.log
> deactivate
前一版本：img

[/members/models.py](/members/models.py)
* 加上 `user` 的外鍵
```python
user = models.OneToOneField(User, on_delete=models.CASCADE, default= None, blank=True, null=True)
```
* 因為一個 `user` 對應一個 `member`, 所以採用 `OneToOneField` 來建立 `user`。

asgiref==3.7.2
Django==4.2.10
django-filter==23.5
Imagegrab==0.0.3
MouseInfo==0.1.3
packaging==23.2
Pillow==10.1.0
playsound==1.3.0
PyAutoGUI==0.9.54
pygame==2.5.2
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyperclip==1.8.2
PyRect==0.2.0
PyScreeze==0.1.30
pytesseract==0.3.10
pytweening==1.0.7
screeninfo==0.8.1
sqlparse==0.4.4
typing_extensions==4.9.0
tzdata==2023.3


