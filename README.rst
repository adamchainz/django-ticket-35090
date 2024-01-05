django-ticket-35090
===================

Reproduction for `Ticket #35090 <https://code.djangoproject.com/ticket/35090>`__.

First, show the successful resolution of a “book archive URL” with a single-digit year:

.. code-block:: text

    $ ./manage.py shell -c 'from django.urls import resolve; print(resolve("/books/1/").func)'
    <function books_year_archive at 0x10550afc0>

This is per the definition in ``example/urls_books.py``.

Then, edit ``example/urls.py`` to uncomment the second ``include()``:

.. code-block:: diff

     from django.urls import include
     from django.urls import path

     urlpatterns = [
         path("books/", include("example.urls_books")),
    -    # path("engravings/", include("example.urls_engravings")),
    +    path("engravings/", include("example.urls_engravings")),
     ]

Now, the test will fail:

.. code-block:: text

    $ ./manage.py shell -c 'from django.urls import resolve; print(resolve("/books/1/").func)'
    Traceback (most recent call last):
      ...
    django.urls.exceptions.Resolver404: {'tried': [[<URLResolver <module 'example.urls_books' from '/.../example/urls_books.py'> (None:None) 'books/'>, <URLPattern '<year:year>/'>], [<URLResolver <module 'example.urls_engravings' from '/.../example/urls_engravings.py'> (None:None) 'engravings/'>]], 'path': 'books/1/'}

The path converter registered in ``example/urls_engravings.py`` clobbered the one from ``example/urls_books.py``, breaking the expected allowed books URL.
