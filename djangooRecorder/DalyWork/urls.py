from django.urls import path
from . import views

#修改 app 的名称
app_name = 'DalyWorkPPP'


urlpatterns = [
    path('', views.post_list, name="list"),
    path('<int:pk>',views.post_page,name="page"),
    path('item/<int:pk>/delete/',views.delete_item, name ="delete_item"),
    path('item/<int:pk>/submit/', views.submit_view, name='submit_view'),
    path('item/cutInformation/', views.cutInformation, name='cutInformation_view')

]
