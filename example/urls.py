from django.urls import include
from django.urls import path

urlpatterns = [
    path("books/", include("example.urls_books")),
    # path("engravings/", include("example.urls_engravings")),
]
