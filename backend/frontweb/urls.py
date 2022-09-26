from . import views
from django.urls import path
from .views import *
 
urlpatterns = [
    ### START STATIC PAGES ROUTES FRONTEND 
    path('', views.HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about"),  
    path("contact/", ContactPageView.as_view(), name="contact"), 
    
    path('blog/', views.PostList.as_view(), name='blog'),
    path("products/", views.ProductList.as_view(), name="products"), 
    path("services/", views.ServiceList.as_view(), name="services"), 

    path('admin_draft_post/', views.Draft_PostList.as_view(), name='draft_post_list'),
    path("privacy/", PrivacyPageView.as_view(), name="privacy"), 
    path("portfolio/", PortfolioPageView.as_view(), name="portfolio"), 
    path("partners/", PartnersPageView.as_view(), name="partners"), 
    ### END STATIC PAGES ROUTES FRONTEND 

    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("int/", AdminPageView.as_view(), name="home"), 



    ### START STATIC PAGES ROUTES FRONTEND 

]