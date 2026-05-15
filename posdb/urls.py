# posdb/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ១. ផ្លូវទៅកាន់ផ្ទាំងគ្រប់គ្រង Admin (គួរដាក់នៅខាងលើគេដើម្បីឱ្យ Django រកឃើញមុន)
    path('admin/', admin.site.urls),
    
    # ២. ផ្លូវទៅកាន់ App ផ្នែកលក់ (Sales App)
    path('sales/', include('sales.urls')),
    
    # ៣. ផ្លូវទៅកាន់ប្រព័ន្ធ Login/Logout
    path('accounts/', include('django.contrib.auth.urls')),

    # ៤. ទំព័រដើម (បើកមកឱ្យលោតទៅទំព័រ Login ភ្លាម)
    path('', RedirectView.as_view(url='/accounts/login/'), name='home'),
]

# ៥. ការកំណត់សម្រាប់បង្ហាញរូបភាព (Media Files)
# ត្រូវប្រាកដថាវាស្ថិតនៅក្រៅ urlpatterns មេ និងនៅខាងក្រោមបង្អស់
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # បន្ថែម static files ក្នុងករណីខ្លះវាមិនទាន់ស្គាល់ CSS របស់ Admin
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)