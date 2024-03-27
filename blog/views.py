from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from blog.models import  Author, Post
from django.urls import reverse
from blog.forms import CommentForm
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import get_object_or_404



class Blog(ListView):
    template_name = 'blog.html'