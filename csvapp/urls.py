"""[Author: Chanh Duong. Student number: 040-681-356]
    """
from django.urls import path, include
from . import views
"""[Create url paths to the specify function
    start with http://127.0.0.1:8000/csvapp/]
    """
urlpatterns = [
    path('list/', views.record_list, name='record_list'),
    path('form/', views.record_form, name='record_insert'),
    path('form/<int:id>/', views.record_form, name='record_update'),
    path('delete/<int:id>/', views.record_delete, name='record_delete'),
    path('download-csv/', views.record_download, name='record_download'),
    path('delete_all/', views.record_delete_all, name='record_delete_all'),
    path('sort_pruid_Ascending/', views.sort_recordId_Ascending, name='record_sortId_ascending'),
    path('sort_pruid_Descending/', views.sort_recordId_Descending, name='record_sortId_descending'),
    path('sort_prname_Ascending/', views.sort_recordName_Ascending, name='record_sortName_ascending'),
    path('sort_prname_Descending/', views.sort_recordName_Descending, name='record_sortName_descending'),
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    path('horizontal_bar_chart/', views.horizontal_bar_chart, name='horizontal_bar_chart'),
]
