from django.db import models
from LoginAndRegAPP.models import *


class authors(models.Model):
    author_name = models.CharField(max_length=45, null=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def add_author(name):
        author = authors.objects.create(author_name=name)
        return author.id

    def get_authors():
        return authors.objects.all()


class books(models.Model):
    book_title = models.CharField(max_length=45, null=True)
    author = models.ForeignKey(authors, related_name='author_book', null=True, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    objects=usersManger()

    def add_book(request, author_id):
        author_id = authors.objects.get(id=author_id)
        book_title = request.POST['book_title']
        book = books.objects.create(book_title=book_title, author=author_id)
        return book.id

    def get_books():
        return books.objects.all().order_by('-id')[:3]

    def all_books():
        return books.objects.all()


class reviews(models.Model):
    review_book = models.ForeignKey(
        books, related_name='reviewBook', on_delete=models.CASCADE)
    review_user = models.ForeignKey(
        User, related_name='reviewUser', on_delete=models.CASCADE)
    review = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(null=True)
    create_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def add_reviews(book_id, user_id, request):
        book_id = books.objects.get(id=book_id)
        user_id = User.objects.get(id=user_id)
        review = request.POST['review']
        rating = request.POST['rating']
        reviews.objects.create(
            review_book=book_id, review_user=user_id, review=review, rating=rating)

    def total_reviews(id):
        return reviews.objects.filter(review_user=id).count()

    def deleteReview(id):
        return reviews.objects.get(id=id).delete()


def get_user_info(id):
    return User.objects.get(id=id)
