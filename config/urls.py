from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, ReviewViewSet, AuthorViewSet, AuthorDashboardAPIView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'authors', AuthorViewSet, basename='author')

schema_view = get_schema_view(
    openapi.Info(
        title="BookReview API",
        default_version='v1',
        description="도서 및 리뷰 API 명세",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/authors/', AuthorDashboardAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]