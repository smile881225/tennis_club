from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib import auth
from django.shortcuts import render

from web.forms import LoginForm
# from web.forms import signinForm

def login(request):
    ''' 登入 '''
    login_page = loader.get_template('login.html')
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'user': request.user,
            'login_form': login_form,
        }
        return render(request, 'login.html', context)

    elif request.method == "POST":

        login_form = LoginForm(request.POST)
        err_login_msg = ""
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            if not username or not password:
                err_login_msg = 'Please enter both username and password.'
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    main_page = loader.get_template('main.html')
                    context = {'user': request.user,
                               'message': 'login ok'}
                    if username[:4] == "v1-1":
                        return render(request, 'login_result-v-1.html', context)
                    # if username[:4] == "v1-2": 用另一個網址
                    #     return render(request, 'login_result-v-1.html',context)
                    elif username[:4] == "v2-1":
                        print("v2-1")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v2-2":
                        print("v2-2")
                        return render(request, 'main_v2_2.html', context)
                    elif username[:4] == "v3-1":
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v3-2":
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v4-1":
                        print("v4-1")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v4-2":
                        print("v4-2")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v5-1":
                        print("v5-1")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v5-2":
                        print("v5-2")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v6-1":
                        print("v6-1")
                        return render(request, 'main_v6_1.html', context)
                    elif username[:4] == "v6-2":
                        print("v6-2")
                        return render(request, 'main_v6_2.html', context)
                    elif username[:4] == "v7-1":
                        print("v7-1")
                        return render(request, 'main_v7_1.html', context)
                    elif username[:4] == "v7-2":
                        print("v7-2")
                        return render(request, 'main_v7_2.html', context)
                    elif username[:4] == "v8-1":
                        print("v8-2")
                        return render(request, 'main_v8_1.html', context)
                    elif username[:4] == "v8-2":
                        print("v8-2")
                        return render(request, 'main_v8_2.html', context)
                    elif username[:4] == "v9-1":
                        print("v9-1")
                        return render(request, 'main_v2_1.html', context)
                    elif username[:4] == "v9-2":
                        print("v9-2")
                        return render(request, 'main_v2_2.html', context)
                else:
                    err_login_msg = 'Login failed (user id/passworld not correct)'
        else:
            err_login_msg = 'Login error (login form is not valid)'

        # login fail
        context = {'login_form': login_form,
                   'err_login_msg': err_login_msg}
        return render(request, 'login.html', context)

    else:
        print ('Error on request (not GET/POST)')
def login_v1_2(request):
    ''' 登入 '''
    login_page = loader.get_template('login.html')
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'user': request.user,
            'login_form': login_form,
        }
        return render(request, 'login.html', context)

    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                main_page = loader.get_template('main.html')
                context = {'user': request.user,
                           'message': 'login ok'}
                # if username[:4] == "v1-1":
                #     return render(request, 'login_result-v-1.html', context)
                if username[:4] == "v1-2":
                    return render(request, 'login_result-v-1.html',context)
                if username[:4] == "v2-1":
                    return render(request, 'main.html',context)
                if username[:4] == "v2-2":
                    return render(request, 'main.html',context)
            # login fail
            context = {'login_form': login_form,
                       'err_login_msg': ''}
        return render(request, 'login.html', context)
        # return redirect('login_v1_2')  # 重定向





def logout(request):
    ''' 登出 '''
    auth.logout(request)
    main_html = loader.get_template('remind.html')
    context = {'user': request.user}
    return HttpResponse(main_html.render(context, request))

# def signin(request):
# 註冊，沒有寫完
#     login_page = loader.get_template('signin.html')
#     if request.method == 'POST':
#         login_form = signinForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 main_page = loader.get_template('main.html')
#                 context = {'user': request.user,
#                            'message': 'login ok'}
#                 return render(request, 'main.html', context)
#     data = {}
#
#     username = request.GET.get('username')
#     password = request.GET.get('password')
#
#     context = {}
#     return HttpResponse(login_page.render(context, request))

