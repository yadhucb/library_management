from django.contrib import admin
from library.models import User, Book, CheckOut

admin.site.register(User)
admin.site.register(Book)
admin.site.register(CheckOut)

