from django.urls import path
from rest_framework.authtoken import views as auth_views

from library import views

app_name = 'library'

urlpatterns = [
    path('token-auth/', auth_views.obtain_auth_token),
    path('student/create/', views.CreateStudentView.as_view()),
    path('student/list/', views.ListStudentView.as_view()),
    path('student/<int:pk>/', views.SingleStudentView.as_view()),
    path('student/update/<int:pk>/', views.UpdateStudentView.as_view()),
    path('student/delete/<int:pk>/', views.DeleteUserView.as_view()),

    path('book/create/', views.CreateBookView.as_view()),
    path('book/list/', views.ListBookView.as_view()),
    path('book/<int:pk>/', views.SingleBookView.as_view()),
    path('book/update/<int:pk>/', views.UpdateBookView.as_view()),
    path('book/delete/<int:pk>/', views.DeleteBookView.as_view()),

    path('checkout/create/', views.CreateCheckoutView.as_view()),
    path('checkout/list/', views.ListCheckoutView.as_view()),
    path('checkout/<int:pk>/', views.SingleCheckoutView.as_view()),
    path('checkout/update/<int:pk>/', views.UpdateCheckoutView.as_view()),
    path('checkout/delete/<int:pk>/', views.DeleteCheckoutView.as_view()),


]