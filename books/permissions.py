# books/permissions.py
from rest_framework import permissions

class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기는 모두 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # 수정/삭제는 작성자만 허용
        return obj.user == request.user
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    작성자만 수정/삭제 가능하고, 나머지는 읽기 전용 권한
    """
    def has_object_permission(self, request, view, obj):
        # 읽기 요청(GET, HEAD, OPTIONS)은 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # 그 외(PUT, PATCH, DELETE)는 작성자만 허용
        return obj.user == request.user