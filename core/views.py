from django.shortcuts import render
from .forms import ContactModelForm

# Create your views here.


def home(request):
    form = ContactModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
    	obj = form.save(commit=False)
    	obj.save()
    	return redirect('/')


    context = {'form': form}
    template_name = 'core/home.html'
    return render(request, template_name, context)
