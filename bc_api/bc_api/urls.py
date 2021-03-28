from django.contrib import admin
from django.urls import path
from apps.book.views import BookListView
from apps.review.views import ReviewListView
from apps.user.views import BCUserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view()),
    path('reviews/', ReviewListView.as_view()),
    path('users/', BCUserListView.as_view()),
]
