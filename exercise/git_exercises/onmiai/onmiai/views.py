from django.shortcuts import render, redirect
from userAuth.models import Boy, Girl, B2G

def index(request):
    user_info = request.session.get("user_info")
    if not user_info:
        return redirect("login/")
    else:
        gender = user_info.get("gender")
        if gender == "1":
            userList = Girl.objects.all()
        else:
            userList = Boy.object.all()
        return render(request, "index.html", context={
            "user_list" : userList,
        })

def others(request):
    user_info = request.session.get("user_info")
    userId = user_info.get("user_id")
    gender = user_info.get("gender")
    if gender == "1":
        userList = B2G.objects.filter(b_id=userId).values("g__nickname")
    else:
        userList = B2G.objetcs.filter(g_id=userId).values("b__nickname")
    return render(request, "others.html", context={
        "user_list" : userList,
    })