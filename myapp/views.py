from django.shortcuts import render

def my_info(request):
    return render(request,'my_info.html')
