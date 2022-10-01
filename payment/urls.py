from django.urls import path
from payment.views import purchase_view

urlpatterns = [
    # purchase
    path('purchase/', purchase_view.PurchaseCreateListView.as_view()),
    path('purchase/<pk>/', purchase_view.PurchaseUpdateAPIView.as_view()),
    path('purchase/detail/<pk>/', purchase_view.PurchaseDetailsView.as_view()),
]
