from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages



def book(request):
    if not 'userid' in request.session:
        return redirect('/')
    book = books.get_books()
    list = []
    for i in book:
        last_comment = reviews.objects.filter(review_book=i.id).last()
        list.append(last_comment)
    context = {
        'books': books.get_books(),
        'last_comment': list,
        'Allbooks': books.all_books()
    }
    return render(request, 'books.html', context=context)


def add_books(request):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        errors = User.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        author_from_database = request.POST['author_from_database']
        author_from_user = request.POST['author_from_user']
        if len(author_from_user) > 0:
            author = author_from_user
            author_id = authors.add_author(author)
        else:
            author = author_from_database
            author_id = authors.objects.filter(author_name=author)[0].id

        book_id = books.add_book(request, author_id)
        user_id = int(request.session['userid'])
        reviews.add_reviews(book_id, user_id, request)

        return redirect(f'books/{book_id}')
    else:
        context = {
            'authors': authors.get_authors()
        }
        return render(request, 'add_books.html', context=context)


def Book_det(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        book_id = id
        user_id = int(request.session['userid'])
        reviews.add_reviews(book_id, user_id, request)
        return redirect(f'books/{id}')
    else:
        context = {
            'book': books.objects.get(id=id)
        }
        return render(request, 'book_det.html', context=context)


def destroy(request):
    del request.session['userid']
    return redirect('/')


def display_user_info(request, id):
    context = {
        'info_user': get_user_info(id),
        'total_reviews': reviews.total_reviews(id),
        'reviwed_by_user': reviews.objects.filter(review_user=id)
    }
    return render(request, 'display_user_info.html', context=context)


def delete(request, id):
    reviews.deleteReview(id)
    return redirect('/books')
