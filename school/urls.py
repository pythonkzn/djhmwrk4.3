from django.urls import include, path

from school.views import students_list
import website

urlpatterns = [
    path('', students_list, name='students'),
]

if  website.settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns