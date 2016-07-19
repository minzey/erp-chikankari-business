"""internship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from AnIndianStory import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': 'login'}, name='logout'),
    url(r'^homepage/$',login_required(views.homepage), name='home'),
    url(r'^karigars_all/$', login_required(views.karigars_all), name='karigars_all'),
    url(r'^products_all/$', login_required(views.products_all), name='products_all'),
    url(r'^new_karigar/$',login_required(views.new_karigar), name='new_karigar'),
    url(r'^new_product/$',login_required(views.new_product), name='new_product'),
    url(r'^overview_dates/$', login_required(views.overview_dates), name='overview_dates'),
    url(r'^overview_karigars/$', login_required(views.overview_karigars), name='overview_karigars'),
    url(r'^overview_products/$', login_required(views.overview_products), name='overview_products'),
    url(r'^overview_challans/$', login_required(views.overview_challans), name='overview_challans'),
    url(r'(?P<name_pk>[\w\ -]+)/edit_karigar/$',login_required(views.edit_karigar), name='edit_karigar'),
    url(r'delete_karigar/(?P<name_pk>[\w\ -]+)/$',login_required(views.delete_karigar), name='delete_karigar'),
    url(r'(?P<id_pk>[\w\ -]+)/edit_product/$',login_required(views.edit_product), name='edit_product'),
    url(r'delete_product/(?P<id_pk>[\w\ -]+)/$',login_required(views.delete_product), name='delete_product'),
    url(r'(?P<name_pk>[\w\ -]+)/new_assignment/$',login_required(views.assign_product), name='new_product_assign'),
    url(r'^overview_karigars/get_table_karigar/$', login_required(views.getTableKarigar), name='get_table_karigar'),
    url(r'^overview_products/get_table_product/$', login_required(views.getTableProduct), name='get_table_product'),
    url(r'^overview_challans/get_table_challan/$', login_required(views.getTableChallan), name='get_table_challan'),
    url(r'^overview_dates/get_report/$', login_required(views.getTableDate_ActiveProducts), name='get_report'),
    url(r'^overview_dates/get_report_table/$', login_required(views.getTableData_Process), name='get_report_table'),
    url(r'^overview_challans/delete_assignment/$', login_required(views.deleteAssignment), name='delete_assignment'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
