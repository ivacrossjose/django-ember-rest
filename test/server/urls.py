from django_ember_rest import patterns, include, url
import apis

urlpatterns = patterns('',
    url(r'^', include(apis.urls, namespace='apis')),
)