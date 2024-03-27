from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from blog.models import  Author, Post, Tags, Comment
from django.urls import reverse
from blog.forms import CommentForm
from typing import Any
from django.db.models.query import QuerySet

