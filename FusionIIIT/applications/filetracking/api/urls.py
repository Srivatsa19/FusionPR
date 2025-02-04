from django.conf.urls import url
from .views import (
    CreateFileView,
    ViewFileView,
    DeleteFileView,
    ViewInboxView,
    ViewOutboxView,
    ViewHistoryView,
    ForwardFileView,
    GetDesignationsView,
)

urlpatterns = [
    url(r'^file/$', CreateFileView.as_view(), name='create_file'),
    url(r'^file/(?P<file_id>\d+)/$', ViewFileView.as_view(), name='view_file'),
    url(r'^file/(?P<file_id>\d+)/$', DeleteFileView.as_view(), name='delete_file'),
    url(r'^inbox/$', ViewInboxView.as_view(), name='view_inbox'),
    url(r'^outbox/$', ViewOutboxView.as_view(), name='view_outbox'),
    url(r'^history/(?P<file_id>\d+)/$', ViewHistoryView.as_view(), name='view_history'),
    url(r'^file/(?P<file_id>\d+)/$', ForwardFileView.as_view(), name='forward_file'),
    url(r'^designations/(?P<username>\w+)/$', GetDesignationsView.as_view(), name='get_designations'),
]
