from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from accounts.permissions import login_user
from .models import Blog
from .forms import BlogForm
# Create your views here.
def get_blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog/list.html',{'blogs':blogs})

@login_user
def create_blog(request):
    # user=request.user
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect("list")
        # if form.is_valid():
        #     form.owner = request.user.id
        #     form.save()
        #     # blog.owner=user.id
        #     return redirect("list")
    else:
        form=BlogForm()
    return render(request,"blog/create.html",{'form':form})




# blog (yoki tegishli app) ichidagi views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog # modelingiz nomi nima bo'lsa shuni yozing

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'accounts/detail.html', {'blog': blog})