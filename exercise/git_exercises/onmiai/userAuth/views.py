from django.shortcuts import render, HttpResponse, redirect
from .models import Boy, Girl

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        if gender == "1":
            obj = Boy.objects.filter(username=username, password=password).first()
        else:
            obj = Girl.objects.filter(username=username, password=password).first()

        if not obj:
            return render(request, "userAuth/login.html", context={
                "msg" : "用户或密码错误!",
            })
        else:
            request.session["user_info"] = {
                "user_id" : obj.id,
                "user_name" : obj.username,
                "nick_name" : obj.nickname,
                "gender" : gender,
            }
            return redirect("/")

    return render(request, "userAuth/login.html", context={})

def logout(request):
    userInfo = request.session.get("user_info")
    if userInfo: request.session.clear()
    return render(request, "userAuth/login.html", context={})
