import os

from django.core.mail import message
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,HttpResponseRedirect
# 改数据库名称
from .models import DalyWorkPost

# Create your views here.
def post_list(request):
    posts = DalyWorkPost.objects.all().order_by('-date')
    print(posts)
    #                                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 这个相当于 文件路径
    return render(request, 'DalyWorkPost/posts_list.html', {'posts': posts})

def post_page(request, pk):
    post = DalyWorkPost.objects.get(id=pk)
    #save_delete(request, post)
    #                                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return render(request, 'DalyWorkPost/post_page.html', {'post':post})


def delete_item(request, pk):
    print(pk)
    item = get_object_or_404(DalyWorkPost, id=pk)
    item.delete()
    #              ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return redirect('DalyWorkPPP:list')

def submit_view(request,pk):
    print(pk)
    if request.method == "POST":
        text = request.POST.get('input_text')
        post = DalyWorkPost.objects.get(id=pk)
        full_text = post.workduty + "\n" + text
        post.workduty = full_text
        post.save()
        #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return redirect('DalyWorkPPP:list')
from django.shortcuts import render

# Create your views here.
