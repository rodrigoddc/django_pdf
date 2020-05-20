from django.urls import path

from apps.core.views.view_reportlab import IndexView, PdfRenderView, PdfDownloadView
from apps.core.views.view_weasyprint import PDFRenderView, PDFDownloadView

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('reportlab-download/', PdfDownloadView.as_view(), name='reportlab_download'),
    path('reportlab-render/', PdfRenderView.as_view(), name='reportlab_render'),

    path('weasyprint-render/', PDFRenderView.as_view(), name='weasyprint_render'),
    path('weasyprint-download/', PDFDownloadView.as_view(), name='weasyprint_download'),
]
