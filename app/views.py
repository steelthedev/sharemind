from django.shortcuts import redirect, render , get_object_or_404
from .models import *
from django.contrib import messages

# Create your views here.

def Home(request):
    Category = Categories.objects.all()
    context = {
        'category':Category
    }
    if request.method == "POST":
        title=request.POST["title"]
        post = request.POST["post"]
        category = request.POST["category"]
        e = Experience.objects.create(title = title , post = post , category = category)
        e.save()

        messages.success(request, "Experience Successfully Shared")
        return redirect('feed')
    return render(request , 'app/index.html' , context)

def PostDetails(request, slug ):
    Post = Experience.objects.get(slug=slug)
    comments = Comment.objects.filter(post=Post ,active=True)
    context = {
        'post':Post,
        'comments':comments
    }

    if request.method == "POST":
        comment = request.POST["comment"]
        new_comment = Comment.objects.create(text=comment , active=True , post = Post)
        new_comment.save()
        
    
    return render(request , "app/postdetails.html" , context)

def Feed(request):
    e = Experience.objects.all().order_by("date")
    context = {
        'experience':e
    }
    return render(request, "app/feed.html" , context)
