"""Определяет схемы URL для Personal_diarys"""
from django.urls import path
from . import views


app_name = 'Personal_diarys'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    
    path('topics/', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Страница добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Удаление темы
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),

    # Удаление записи
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]