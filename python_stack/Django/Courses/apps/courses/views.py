from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "courses" : Course.objects.all(),
    }
    return render(request, "courses/index.html", context)

def destroy(request, course_id):
    print('in destroy')
    print('course_id', course_id)
    context = {
        'course' : Course.objects.get(id = course_id)
    }
    return render(request, "courses/verify.html", context)

def add(request):
    print(request.POST)
    name = request.POST['course_name']
    desc = request.POST['course_desc']
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    print(request.POST)
    errors = Description.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        icourse = Course.objects.create(name = name)
        Description.objects.create(desc = desc, course = Course.objects.get(id = icourse.id))
        return redirect('/')

def delete(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect('/')




# works
# def add(request):
#     print(request.POST)
#     name = request.POST['course_name']
#     desc = request.POST['course_desc']
#     errors = Course.objects.basic_validator(request.POST)
#     if len(errors):
#         print("in add error section")
#         for tag, error in errors.items():
#             messages.error(request, error, extra_tags = tag)
#         return redirect('/')
#     else:
#         icourse = Course.objects.create(name = name)
#         Description.objects.create(desc = desc, course = Course.objects.get(id = icourse.id))
#         return redirect('/')