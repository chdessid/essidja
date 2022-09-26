from django.shortcuts import render
from django.views import generic
from .models import *
import os

class PostList(generic.ListView):
    post_list = os.path.join("front_pages","blog.html")
    queryset = Post.objects.all()
    template_name = post_list

class ProductList(generic.ListView):
    product_list = os.path.join("front_pages","products.html")
    queryset = Product.objects.all()
    template_name = product_list

class ServiceList(generic.ListView):
    service_list = os.path.join("front_pages","services.html")
    queryset = Service.objects.all()
    template_name = service_list




class Draft_PostList(generic.ListView):
    draft_post_list = os.path.join("admin_pages","draft_posts_list.html")
    queryset = DraftPost.objects.all()
    template_name = draft_post_list



class PostDetail(generic.DetailView):
    _path = os.path.join("front_pages","index.html")
    model = Post
    template_name = _path

## STATIC PAGES ROUTES
class HomePageView(generic.TemplateView):
    _home_page = os.path.join("front_pages","index.html")
    template_name = _home_page

class AboutPageView(generic.TemplateView):  # new
    _about_page = os.path.join("front_pages","about.html")
    template_name = _about_page

class ContactPageView(generic.TemplateView):  # new
    _contact_page = os.path.join("front_pages","contact.html")
    template_name = _contact_page

class BlogPageView(generic.TemplateView):  # new
    _blog_page = os.path.join("front_pages","blog.html")
    template_name = _blog_page

class PrivacyPageView(generic.TemplateView):  # new
    _privacy_page = os.path.join("front_pages","privacy.html")
    template_name = _privacy_page

class ServicesPageView(generic.TemplateView):  # new
    _services_page = os.path.join("front_pages","services.html")
    template_name = _services_page

class ProductsPageView(generic.TemplateView):  # new
    _products_page = os.path.join("front_pages","products.html")
    template_name = _products_page

class PartnersPageView(generic.TemplateView):  # new
    _partners_page = os.path.join("front_pages","partners.html")
    template_name = _partners_page

class PortfolioPageView(generic.TemplateView):  # new
    _portfolio_page = os.path.join("front_pages","portfolio.html")
    template_name = _portfolio_page

## END STATIC PAGES ROUTES


## START ADMIN PAGES ROUTES
class AdminPageView(generic.TemplateView):  # new
    _admin_page = os.path.join("admin_pages","index.html")
    template_name = _admin_page

## END ADMIN PAGES ROUTES
