from django.shortcuts import render, redirect
from elections24.models import Constituency, Postcode
from .forms import PostcodeForm


def index(request):
    args = {'page': 'Home', 'form': PostcodeForm}
    return render(request, 'elections24/index.html', args)


def constituency(request, constituency):
    try:
        c = Constituency.objects.get(three_code=constituency.upper())
    except Constituency.DoesNotExist:
        return redirect('index')
    args = {'page': 'Constituency', 'constituency': c}
    return render(request, 'elections24/constituency.html', args)


def postcode(request):
    if request.method == "POST":
        form = PostcodeForm(request.POST)
        args = {'page': 'Home', 'form': form}
        if form.is_valid():
            postcode = form.cleaned_data['postcode']
            try:
                p = Postcode.objects.get(postcode=postcode)
            except Postcode.DoesNotExist:
                return render(request, 'elections24/index.html', args)
            c = p.constituency_fk
            return redirect('constituency', c.three_code)
        else:
            return render(request, 'elections24/index.html', args)
    else:
        return redirect('index')
