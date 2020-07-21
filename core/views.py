from django.shortcuts import render, redirect
from .forms import ContactModelForm

# Create your views here.


def home(request):
    form = ContactModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
    	obj = form.save(commit=False)
    	obj.save()
    	return redirect('/')


    context = {'form': form}
    template_name = 'core/index.html'
    return render(request, template_name, context)


def next(request):
	template_name ='core/single.html'
	context = {}
	return render(request, template_name, context)
