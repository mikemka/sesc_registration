from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest as Request
from forms.forms import GumForm, SgumForm, SocEkForm, MatInfForm
from forms.models import Gum, Sgum, SocEk, MatInf


def form(request: Request):
    rn = GumForm()
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = GumForm(request.POST)
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../1/{slug}/')
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, 'forms/form.html', data)


def form2(request: Request):
    rn = SgumForm()
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = SgumForm(request.POST)
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../2/{slug}/')
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, 'forms/form2.html', data)


def form3(request: Request):
    rn = SocEkForm()
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = SocEkForm(request.POST)
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../3/{slug}/')
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, 'forms/form3.html', data)


def form4(request: Request):
    rn = MatInfForm()  #!
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = MatInfForm(request.POST)  #!
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../4/{slug}/')  #!
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, 'forms/form4.html', data)  #!


def result(request: Request, pk):
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
        "all": (ALL1 * 2) * 35 + 1995,
    })


def result2(request: Request, pk):
    try:
        data_copy = Sgum.objects.get(slug=pk)
    except:
        return redirect('10sgum')
    dt = {
        "name": data_copy.name,
        "slug": data_copy.slug,
        "d1": int(data_copy.d1),
        "d2": int(data_copy.d2),
        "d3": int(data_copy.d3),
        "d4": int(data_copy.d4),
        "d5": int(data_copy.d5) * 3,
        "d6": int(data_copy.d6) * 2,
        "d7": int(data_copy.d7),
        "d8": int(data_copy.d8),
        "d9": int(data_copy.d9) * 2,
        "d10": int(data_copy.d10) * 2,
        "d11": int(data_copy.d11) * 2
    }
    ALL1 = sum((dt['d1'], dt['d2'], dt['d3'], dt['d4'], dt['d5'], dt['d6'], dt['d7'], dt['d8'], dt['d9'], dt['d10'], dt['d11'], 3))
    return render(request, 'forms/result2.html', {
        "form": dt,
        "all1": ALL1 + 28,
        "all": (ALL1 * 2) * 35 + 1855,
    })


def result3(request: Request, pk):
    try:
        data_copy = SocEk.objects.get(slug=pk)
    except:
        return redirect('10socek')
    dt = {
        "name": data_copy.name,
        "slug": data_copy.slug,
        "d1": int(data_copy.d1),
        "d2": int(data_copy.d2),
        "d3": int(data_copy.d3),
        "d4": int(data_copy.d4),
        "d5": int(data_copy.d5) * 3,
        "d6": int(data_copy.d6),
        "d7": int(data_copy.d7) * 2,
        "d8": int(data_copy.d8) * 2,
    }
    ALL1 = sum((dt['d1'], dt['d2'], dt['d3'], dt['d4'], dt['d5'], dt['d6'], dt['d7'], dt['d8'], 2))
    return render(request, 'forms/result3.html', {
        "form": dt,
        "all1": ALL1 + 30,
        "all": ALL1 * 2 * 35 + 1995,
    })  


def result4(request: Request, pk):
    try:
        data_copy = MatInf.objects.get(slug=pk)  #!
    except:
        return redirect('10matinf')  #!
    dt = {
        "name": data_copy.name,
        "slug": data_copy.slug,
        "d1": int(data_copy.d1) * 2,
        "d2": int(data_copy.d2),
        "d3": int(data_copy.d3),
        "d4": int(data_copy.d4),
        "d5": int(data_copy.d5),
        "d6": int(data_copy.d6) * 2,
        "d7": int(data_copy.d7) * 2,
        "d8": int(data_copy.d8) * 2,
    }
    ALL1 = sum((dt['d1'], dt['d2'], dt['d3'], dt['d4'], dt['d5'], dt['d6'], dt['d7'], dt['d8'], 5))
    return render(request, 'forms/result4.html', {  #!
        "form": dt,
        "all1": ALL1 + 28,
        "all": ALL1 * 2 * 35 + 1855,
    })  
