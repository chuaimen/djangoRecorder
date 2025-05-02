from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.post_list, name="list"),
    path('<int:pk>',views.post_page,name="page"),
    path('item/<int:pk>/delete/',views.delete_item, name ="delete_item"),
    path('item/<int:pk>/submit/', views.submit_view, name='submit_view')

]
