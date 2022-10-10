# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:17:13 2022

@author: hankr
"""

from django.urls import path
from giwpage import views

urlpatterns = [
    path( 'home', views.render_index, name = 'render_index' ),
    
    ]