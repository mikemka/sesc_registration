from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest as Request
from forms.models import Gum, Sgum, SocEk, MatInf, FizMat


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
    return render(request, 'forms/result/result.html', {
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
    return render(request, 'forms/result/result2.html', {
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
    return render(request, 'forms/result/result3.html', {
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
    return render(request, 'forms/result/result4.html', {  #!
        "form": dt,
        "all1": ALL1 + 28,
        "all": ALL1 * 2 * 35 + 1855,
    })  


def result5(request: Request, pk):
    try:
        data_copy = FizMat.objects.get(slug=pk)  #!
    except:
        return redirect('10fizmat')  #!
    dt = {
        "name": data_copy.name,
        "slug": data_copy.slug,
        "d1": int(data_copy.d1) * 2,
        "d2": int(data_copy.d2),
        "d3": int(data_copy.d3),
        "d4": int(data_copy.d4),
        "d5": int(data_copy.d5),
        "d6": int(data_copy.d6) * 2,
        "d7": int(data_copy.d7) * 0.5,
        "d8": int(data_copy.d8) * 2,
    }
    ALL1 = sum((dt['d1'], dt['d2'], dt['d3'], dt['d4'], dt['d5'], dt['d6'], dt['d7'], dt['d8'], 4))
    return render(request, 'forms/result/result5.html', {  #!
        "form": dt,
        "all1": ALL1 + 30,
        "all": ALL1 * 2 * 35 + 1995,
    })  
