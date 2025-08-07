import os

from django.core.mail import message
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,HttpResponseRedirect
# 改数据库名称
from .models import DalyWorkPost
from . import forms
from django.shortcuts import render

AppDataModel = DalyWorkPost
PostListPage = 'DalyWorkPPP:list'
TemplateFileName = 'DalyWorkPost'

# Create your views here.
def post_list(request):
    #     ↓↓↓↓↓↓↓↓↓改↓↓↓↓↓↓↓
    posts = AppDataModel.objects.all().order_by('-date')
    print(posts)
    form = forms.CreateInFormation()
    #                     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 这个相当于 文件路径
    return render(request, f'{TemplateFileName}/posts_list.html', {'posts': posts, 'form':form})

def post_page(request, pk):
    #     ↓↓↓↓↓↓↓↓↓改↓↓↓↓↓↓↓
    post = AppDataModel.objects.get(id=pk)
    #save_delete(request, post)
    #                                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return render(request, f'{TemplateFileName}/post_page.html', {'post':post})


def delete_item(request, pk):
    print(pk)
    #                     ↓↓↓↓↓↓↓↓↓改↓↓↓↓↓↓↓
    item = get_object_or_404(AppDataModel, id=pk)
    item.delete()
    #              ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return redirect(PostListPage)

def submit_view(request,pk):
    print(pk)
    if request.method == "POST":
        text = request.POST.get('input_text')
        #     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        post = AppDataModel.objects.get(id=pk)
        full_text = post.workduty + "\n" + text
        post.workduty = full_text
        post.save()
        #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    return redirect(PostListPage)

def cutInformation(request):
    if request.method == "POST" and request.POST.get('input_text')!= '':

        text = request.POST.get('input_text')

        print("textttt-----")
        print(text)
        print(type(text))
        #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        temp_posts = AppDataModel.objects.all().order_by('-date')
        posts = []
        print("type of posts", type(temp_posts))
        for post in temp_posts:
            if text in post.client:
                posts.append(post)

        print("_______",posts)
    else:
            #   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        posts = AppDataModel.objects.all().order_by('-date')
        print(posts)

    #                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 这个相当于 文件路径
    return render(request, f'{TemplateFileName}/posts_list.html', {'posts': posts})

def post_new(request):
    if request.method =='POST':
        form = forms.CreateInFormation(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        return redirect(PostListPage)
    else:
        form = forms.CreateInFormation()
            #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        return redirect(PostListPage)

