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
    dt = {
        "name": data_copy.name,
        "slug": data_copy.slug,
        "d1": int(data_copy.d1) * 2,
        "d2": int(data_copy.d2),
        "d3": int(data_copy.d3) * 3,
        "d4": int(data_copy.d4),
        "d5": int(data_copy.d5),
        "d6": int(data_copy.d6) * 3,
        "d7": int(data_copy.d7),
        "d8": int(data_copy.d8),
        "d9": int(data_copy.d9),
        "d10": int(data_copy.d10) * 2,
        "d11": int(data_copy.d11) * 2
    }
    ALL1 = sum((dt['d1'], dt['d2'], dt['d3'], dt['d4'], dt['d5'], dt['d6'], 2, dt['d7'], dt['d8'], dt['d9'], 2, dt['d10'], dt['d11']))
    return render(request, 'forms/result.html', {
        "form": dt,
        "all1": ALL1 + 29,
        "all": (ALL1 * 2 - 1) * 35 + 1995,
    })


def not_ready(request, pk):
    return HttpResponse('В разработке')