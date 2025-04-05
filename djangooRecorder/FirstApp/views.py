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





'''
def delete_item(request, item_id):
    item = get_object_or_404(MyModel, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('success_url_name')  # 删除后重定向

    # 如果是GET请求，可以显示确认页面
    return render(request, 'confirm_delete.html', {'item': item})
'''