from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg,Max,Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        'books':books,
        "number_of_books":num_books,
        "average":avg_rating
    })

def book_detail(request,slug):
    try:
        book=Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,"author":book.title,"rating":book.rating,"is_bestselling":book.is_bestselling,
    })