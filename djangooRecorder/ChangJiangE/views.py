import os

from django.core.mail import message
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,HttpResponseRedirect
# 改数据库名称
from .models import ChangJiangEPost
from . import forms
from django.shortcuts import render
from imagekit.models import ProcessedImageField
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

AppDataModel = ChangJiangEPost
PostListPage = 'ChangJiangEPPP:list'
TemplateFileName = 'ChangJiangEDoc'


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
            getPhotoForm = form.save(commit=False)
            if 'AA' in request.FILES:
                getPhotoForm.AA = resize_image(request.FILES['AA'])
            if 'BB' in request.FILES:
                getPhotoForm.BB = resize_image(request.FILES['BB'])
            if 'CC' in request.FILES:
                getPhotoForm.CC = resize_image(request.FILES['CC'])
            if 'DD' in request.FILES:
                getPhotoForm.DD = resize_image(request.FILES['DD'])
            if 'EE' in request.FILES:
                getPhotoForm.EE = resize_image(request.FILES['EE'])
            if 'FF' in request.FILES:
                getPhotoForm.FF = resize_image(request.FILES['FF'])

            getPhotoForm.save()

            #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        return redirect(PostListPage)
    else:
        form = forms.CreateInFormation()
            #          ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        return redirect(PostListPage)

def resize_image(image_field, width=800, height=1200):
    img = Image.open(image_field)

    if img.mode == 'RGBA':
        img = img.convert('RGB')


    img.thumbnail((width,height))

    output = BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)

    return InMemoryUploadedFile(
        output, 'banner', f"{image_field.name.split('.')[0]}.jpg",
        'image/jpeg', output.getbuffer().nbytes, None
    )

