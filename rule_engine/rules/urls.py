from django.urls import path
from . import views

urlpatterns = [
    path('create_rule/', views.create_rule, name='create_rule'),
    path('evaluate/<int:rule_id>/', views.evaluate_rule, name='evaluate_rule'),
    path('list/', views.rule_list, name='rule_list'),
]


