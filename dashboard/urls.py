from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import DashboardView
from .views import BookingListView
from .views import BookingDetailsView
from .views import BookingDeleteView
from .views import AddFeedbackView
from .views import ListFeedbackView
from .views import DetailsFeedbackView
from .views import EditFeedbackView
from .views import DeleteFeedbackView
from .views import EditProfileView
from .views import ProfileCarView
from .views import ProfileCarListView
from .views import ProfileCarDeleteView
from .views import PasswordChangeProfileView
from .views import PasswordSuccess


urlpatterns = [
    path(
        '', DashboardView.as_view(), name='dashboard'),
    path(
        '', include('django.contrib.auth.urls')),
    ###########################################
    #             Feedback Paths              #
    ###########################################
    path(
        'feedback/add',
        AddFeedbackView.as_view(),
        name='add-feedback'
        ),
    path(
        'feedback/list',
        ListFeedbackView.as_view(),
        name='list-feedback'
        ),
    path(
        'feedback/<int:pk>/details',
        DetailsFeedbackView.as_view(),
        name='details-feedback'
        ),
    path(
        'feedback/<int:pk>/edit',
        EditFeedbackView.as_view(),
        name='edit-feedback'
        ),
    path(
        'feedback/<int:pk>/delete',
        DeleteFeedbackView.as_view(),
        name='delete-feedback'
        ),
    ###########################################
    #             Profile Paths               #
    ###########################################
    path(
        'profile/edit',
        EditProfileView.as_view(),
        name='edit-profile'
        ),
    path(
        'profile/car',
        ProfileCarView.as_view(),
        name='profile-car'
        ),
    path(
        'profile/car/list',
        ProfileCarListView.as_view(),
        name='profile-car-list'
        ),
    path(
        'profile/<int:pk>/delete',
        ProfileCarDeleteView.as_view(),
        name='profile-car-delete'
        ),
    path(
        'password/',
        PasswordChangeProfileView.as_view(
            template_name='dashboard/change-password.html'),
        name='password'
        ),
    path(
        'password-success',
        PasswordSuccess,
        name='password-success'
        ),
    ###########################################
    #             Booking Paths               #
    ###########################################
    path(
        'booking/list',
        BookingListView.as_view(),
        name='booking-list'
        ),
    path(
        'booking/<int:pk>/details',
        BookingDetailsView.as_view(),
        name='booking-details'
        ),
    path(
        'booking/<int:pk>/delete',
        BookingDeleteView.as_view(),
        name='booking-delete'
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
