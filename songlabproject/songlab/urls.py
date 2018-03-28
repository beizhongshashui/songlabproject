from  django.conf.urls import url
from songlab import views

urlpatterns = [
    url(r'^$',views.index,name='index'),#首页
    url(r'^services/$',views.services,name='services'),#科研成果
    url(r'^contact/$',views.contact,name='contact'),#其他
    url(r'^about/$',views.about,name='about'),#团队成员

]