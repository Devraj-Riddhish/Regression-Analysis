"""ra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views  # Ensure 'index' is your app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # Add this line for the root URL
    path('index', views.index),
    path('login', views.login),
    path('about', views.about),
    path('upload', views.upload),
    path('show', views.show),
    path('login_check', views.login_check),
    path('logout', views.logout),
    path('boston_housing', views.boston_housing),
    path('black_friday_catb1', views.black_friday_catb1),
    path('black_friday_train', views.black_friday_train),
    path('black_friday_test', views.black_friday_test),
    path('walmart_sales_features', views.walmart_sales_features),
    path('walmart_sales_store', views.walmart_sales_store),
    path('walmart_sales_train', views.walmart_sales_train),
    path('walmart_sales_test', views.walmart_sales_test),
    path('analysis/Walmart_sales', views.Walmart_sales_analysis),
    path('analysis/redwine', views.redwine_analysis),
    path('analysis/black_friday_sales', views.black_friday_analysis),
    path('analysis/boston_housing', views.boston_housing_data_analysis),
    path('registration', views.registration),
]
