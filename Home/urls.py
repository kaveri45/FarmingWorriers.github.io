from django.urls import path,include
from . import views
urlpatterns = [
     path('',views.home,name="Home"),
    path('admin_login',views.admin_login,name='admin_login'),
    path('register',views.register,name="register"),
     path('Add_Worker_Data',views.Add_Worker_Data,name="Add_Woker_Data"),
      path('view_Worker_Data',views.view_Worker_Data,name="view_Worker_Data"),
      path('delete_Worker/<int:id>',views.delete_Worker,name="delete_Worker"),
       path('worker_Login',views.worker_Login,name="worker_Login"),
        path('worker_Logout',views.worker_Logout,name="worker_Logout"),
         path('admin_Logout',views.admin_Logout,name="admin_Logout"),
        path('search',views.search,name='search'),
        path('edit/<int:id>', views.edit,name='edit'),
]
