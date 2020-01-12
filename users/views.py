from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #check content validity
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        #blank form
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
