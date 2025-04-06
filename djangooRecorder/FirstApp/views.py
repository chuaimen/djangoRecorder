import os

from django.core.mail import message
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,HttpResponseRedirect


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    #save_delete(request, post)

    return render(request, 'posts/post_page.html', {'post':post})


def delete_item(request, pk):
    print(pk)
    item = get_object_or_404(Post, id=pk)
    item.delete()
    return redirect('posts:list')

def submit_view(request,pk):
    print(pk)
    if request.method == "POST":
        text = request.POST.get('input_text')
        post = Post.objects.get(id=pk)
        full_text = post.workduty + "\n" + text
        post.workduty = full_text
        post.save()
    return redirect('posts:list')
