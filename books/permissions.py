# books/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 요청(GET, HEAD, OPTIONS)은 모두 허용
        if request.method in SAFE_METHODS:
            return True
        # 쓰기 요청은 객체 작성자만 허용
        return obj.user == request.user
