from django.contrib import admin
from django.urls import path, include
import contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("contact.urls"))
]
