from django.urls import path
from .views import DashboardView, AddFeedbackView, ListFeedbackView, DetailsFeedbackView, EditFeedbackView, DeleteFeedbackView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('feedback/add', AddFeedbackView.as_view(), name='add-feedback'),
    path('feedback/list', ListFeedbackView.as_view(), name='list-feedback'),
    path('feedback/<int:pk>/details', DetailsFeedbackView.as_view(), name='details-feedback'),
    path('feedback/<int:pk>/edit', EditFeedbackView.as_view(), name='edit-feedback'),
    path('feedback/<int:pk>/delete', DeleteFeedbackView.as_view(), name='delete-feedback'),
]
