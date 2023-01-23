from django.urls import path
from . import views


app_name = 'DojoReadsApp'

urlpatterns = [
    path('', views.book, name='books'),
    path('add', views.add_books, name='add_books'),
    path('books/<int:id>', views.Book_det, name='Book_det'),
    path('books/books/<int:id>', views.Book_det),
    path('destroy', views.destroy, name='destroy'),
    path('users/<int:id>', views.display_user_info, name='users'),
    path('delete/<int:id>', views.delete, name='delete'),
]
