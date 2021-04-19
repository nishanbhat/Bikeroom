from django.shortcuts import render, redirect
from .auth import admin_only
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import Bikes
from .forms import AddBikes


@login_required
@admin_only
def admin_dashboard(request):
    # student = Student.objects.all()
    # student_count = student.count()
    # files = FileUpload.objects.all()
    # files_count = files.count()
    users = User.objects.all()
    user_count = users.count()
    bike_count = Bikes.objects.all().count()
    # admin_count = users.filter(is_staff=1).count()
    context = {
        # 'student': student_count,
        # 'file': files_count,
        'user_count': user_count,
        # 'admin': admin_count
        'bike_count': bike_count
    }
    return render(request, 'admins/AdminDashboard.html', context)


@admin_only
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    return redirect('/admins-dashboard/users')


@admin_only
def show_users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'admins/showUsers.html', context)


@admin_only
def update_admin_to_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = False
    user.save()
    return redirect('/admins-dashboard/users')


@admin_only
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/admins-dashboard/users')


@admin_only
def show_bikes(request):
    bikes = Bikes.objects.all()
    context = {
        "bikes": bikes,
    }
    return render(request, 'admins/showbikes.html', context)


@admin_only
def update_bike(request, id):
    bike = Bikes.objects.get(id=id)
    if request.method == 'POST':
        form = AddBikes(request.POST, instance=bike)
        if form.is_valid():
            form.save()

            return redirect('/admins-dashboard/bikes')
    context = {
        'form': AddBikes(instance=bike)
    }
    return render(request, 'admins/bikeUpdate.html', context)


@admin_only
def delete_bike(request, id):
    bike = Bikes.objects.get(id=id)
    bike.delete()
    return redirect('/admins-dashboard/bikes')


@admin_only
def addBike(request):
    if request.method == "POST":
        form = AddBikes(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Bike added Successfully')
            return redirect('/admin-dashboard/bikes')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please provide correct details')
            return render(request, 'admins/bikeAdd.html', {'form': form})

    context = {
        'form': AddBikes
    }
    return render(request, 'admins/bikeAdd.html', context)
