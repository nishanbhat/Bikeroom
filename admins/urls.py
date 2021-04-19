from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.admin_dashboard),
    # path('show-user', views.get_user),
    # path('update-user-to-admin/<int:user_id>', views.update_user_to_admin),
    # path('admin_register_user', views.admin_register_user),
    path('users', views.show_users),
    path('update-user-to-admin/<int:user_id>', views.update_user_to_admin),
    path('update-admin-to-user/<int:user_id>', views.update_admin_to_user),
    path('delete-user/<int:user_id>', views.delete_user),
    path('bikes', views.show_bikes),
    path('bikes/<int:id>/update', views.update_bike),
    path('bikes/<int:id>/delete', views.delete_bike),
    path('bikes/new', views.addBike),



]
