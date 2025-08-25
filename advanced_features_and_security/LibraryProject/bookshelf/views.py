from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book
from .forms import BookForm, SearchForm

@require_http_methods(["GET"])
def book_list(request):
    form = SearchForm(request.GET or None)
    qs = Book.objects.all().order_by("-id")

    if form.is_valid():
        q = form.cleaned_data.get("q") or ""
        if q:
            # Safe: ORM builds a parameterized query (no SQL injection).
            qs = qs.filter(title__icontains=q) | qs.filter(author__icontains=q)

    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "bookshelf/book_list.html", {"page_obj": page_obj, "form": form})

@login_required
@permission_required("bookshelf.add_book", raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data["title"],
                author=form.cleaned_data["author"],
                published_date=form.cleaned_data.get("published_date"),
            )
            messages.success(request, "Book created.")
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
