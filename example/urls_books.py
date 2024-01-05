from django.urls import path
from django.urls import register_converter

from example import views


class YearConverter:
    regex = r"[0-9]{1,4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%d" % value


register_converter(YearConverter, "year")


urlpatterns = [
    path("<year:year>/", views.books_year_archive),
]
