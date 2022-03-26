from django.shortcuts import redirect, render
from django.http import HttpResponse
from forms.forms import GumForm
from forms.models import Gum


def form(request):
    rn = GumForm()
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = GumForm(request.POST)
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../1/{slug}/')
        else:
            data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, 'forms/form.html', data)


def result(request, pk):
    try:
        data_copy = Gum.objects.get(slug=pk)
    except:
        return redirect('10gum')
    ALL1 = sum((data_copy.d1, data_copy.d3, data_copy.d5, data_copy.d7, data_copy.d9, data_copy.d11, data_copy.d13, data_copy.d15, data_copy.d17, data_copy.d19, data_copy.d21, data_copy.d23, data_copy.d25, 29))
    ALL2 = sum((data_copy.d2, data_copy.d4, data_copy.d6, data_copy.d8, data_copy.d10, data_copy.d12, data_copy.d14, data_copy.d16, data_copy.d18, data_copy.d20, data_copy.d22, data_copy.d24, data_copy.d26, 28))
    return render(request, 'forms/result.html', {
        "form": data_copy,
        "all1": ALL1,
        "all2": ALL2,
        "all": (ALL1 + ALL2) * 35,
        "vn1": data_copy.d27,
        "vn2": data_copy.d28
    })


def not_ready(request, pk):
    return HttpResponse('В разработке')
