from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/',BookListCreateAPIView.as_view(),name="book-list-create"),
    path('books/<int:id>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

]
