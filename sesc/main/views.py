from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/index.html', {
        'forms': (
            ('10gum', 'Гуманитарный'),
            ('10sgum', 'Социально-гуманитарный'),
            ('10socek', 'Социально-экономический'),
            ('10matinf', 'Математико-информационный'),
            ('10fizmat', 'Физико-математический'),
            ('10fiztech', 'Физико-технический'),
            ('10him', 'Химический'),
            ('10bio', 'Биологический'),
        ),
    })


def terms(request):
    return redirect('//lyceum.urfu.ru/fileadmin/user_upload/zamUchRab/uPlan/curr2022-general.pdf')
