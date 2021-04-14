from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='plans'),
    path('add', views.add_plan, name='add_plan'),
    path('view_plan/<str:pk>', views.view_plan, name='view_plan'),
    path('make_active/<str:pk>', views.make_active, name='make_active'),

    path('add_workout/<str:pk>', views.add_workout, name='add_workout'),

    path('add_sets/<str:pk>', views.add_sets, name='add_sets'),

    path('play_workout/<str:pk>', views.play_workout, name='play_workout'),
]