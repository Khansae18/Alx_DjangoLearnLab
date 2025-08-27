from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.http import HttpResponse

def book_list(request):
    return HttpResponse("This is the book list page")

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # change to your list view
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

