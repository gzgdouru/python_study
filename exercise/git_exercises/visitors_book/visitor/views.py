from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import CommentForm
from .models import Comment

# Create your views here.
def index(request):
    form = CommentForm()
    commentList = Comment.objects.all().order_by("-create_time")
    return render(request, "index.html", context={
        "form": form,
        "comment_list" : commentList,
    })

class IndexView(ListView):
    model = Comment
    template_name = "index.html"
    context_object_name = "comment_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        form = CommentForm()
        context.update({
            "form" : form,
        })
        return context

def post_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/")

