from django.urls import path
from .views import DashboardView, AddFeedbackView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('add-feedback/', AddFeedbackView.as_view(), name='add-feedback'),
]
