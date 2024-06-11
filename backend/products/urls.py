from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.product_alt_view),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),#change
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),#change
    path('', views.product_alt_view)
]