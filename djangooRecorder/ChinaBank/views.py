import os

from django.core.mail import message
from django.shortcuts import render
from .models import ChinaBankPost
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,HttpResponseRedirect


# Create your views here.
def post_list(request):
    posts = ChinaBankPost.objects.all().order_by('-date')
    print(posts)
    return render(request, 'NChinaBankPosts/posts_list.html', {'posts': posts})

def post_page(request, pk):
    post = ChinaBankPost.objects.get(id=pk)
    #save_delete(request, post)

    return render(request, 'NChinaBankPosts/post_page.html', {'post':post})


def delete_item(request, pk):
    print(pk)
    item = get_object_or_404(ChinaBankPost, id=pk)
    item.delete()
    return redirect('NChinaBankPosts:list')

def submit_view(request,pk):
    print(pk)
    if request.method == "POST":
        text = request.POST.get('input_text')
        post = ChinaBankPost.objects.get(id=pk)
        full_text = post.workduty + "\n" + text
        post.workduty = full_text
        post.save()
    return redirect('NChinaBankPosts:list')
