from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import *

urlpatterns = [
    path('postlist/', PostAPIListView.as_view(), name='postlist'),
    path('post/<int:pk>/', PostAPIUpdate.as_view(), name='post'),
    path('postdelete/<int:pk>/', PostAPIDestroy.as_view()),
    path('postrating/<int:pk>/<str:method>', postrating),
    path('auth/', include('djoser.urls'), name='auth'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
