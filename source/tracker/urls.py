from django.urls import path
from tracker.views.base import IndexView, IndexRedirectView
from tracker.views.issues import AddView, DetailView, UpdateView, DeleteView

from tracker.views.projects import ProjectDetail

from tracker.views.projects import ProjectCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issues_redirect'),
    path('issue/add/', AddView.as_view(), name='issue_add'),
    path('issue/<int:pk>', DetailView.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update/', UpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', DeleteView.as_view(), name='issue_delete'),
    path('issue/<int:pk>/confirm_delete/', DeleteView.as_view(), name='confirm_delete'),
    path('project/add/', ProjectCreate.as_view(), name='project_add'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_detail')
]
