from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/index.html')


def terms(request):
    return redirect('//lyceum.urfu.ru/fileadmin/user_upload/zamUchRab/uPlan/curr2022-general.pdf')
