from django.contrib import admin
from django.urls import path ,include
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "welcome to the API"})),
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('api/', include('books.urls')),
    path('api/', include('authors.urls')),
    path('api/', include('reviews.urls')),
    path('api/users/', include('users.urls')),   
]
