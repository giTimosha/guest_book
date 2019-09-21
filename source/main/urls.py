from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_view, update_view, delete_view, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('record/add', create_view, name='record_add'),
    path('record/<int:pk>/edit/', update_view, name='record_update'),
    path('record/<int:pk>/delete/', delete_view, name='record_delete'),
    path('record/search/', search_view, name='search_view')
]
