from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest as Request
from forms.forms import GumForm, SgumForm, SocEkForm, MatInfForm, FizMatForm, FizTechForm, HimForm



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
    return render(request, 'forms/form/form.html', data)


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
    return render(request, 'forms/form/form2.html', data)


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
    return render(request, 'forms/form/form3.html', data)


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
    return render(request, 'forms/form/form4.html', data)  #!


def form5(request: Request):
    rn = FizMatForm()  #!
    template_name = 'forms/form/form5.html'  #!
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = FizMatForm(request.POST)  #!
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../5/{slug}/')  #!
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, template_name, data)


def form6(request: Request):
    rn = FizTechForm()  #!
    template_name = 'forms/form/form6.html'  #!
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = FizTechForm(request.POST)  #!
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../6/{slug}/')  #!
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, template_name, data)


def form7(request: Request):
    rn = HimForm()  #!
    template_name = 'forms/form/form7.html'  #!
    data = {'form': rn, 'error': ''}
    if request.method == 'POST':
        frm = HimForm(request.POST)  #!
        if frm.is_valid():
            slug = frm.cleaned_data['slug']
            frm.save()
            return redirect(f'../7/{slug}/')  #!
        data['error'] = 'Ошибка! Проверьте правильность введенных данных!'
    return render(request, template_name, data)
