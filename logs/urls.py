from django.urls import path
from .views import LogList, LogDetail

urlpatterns = [
    path('', LogList.as_view(), name='log-list'),
    path('<int:id_log>/', LogDetail.as_view(), name='log-detail'),
]

