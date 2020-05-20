import io
from django.http import FileResponse, HttpResponse
from django.views.generic import View, TemplateView

from reportlab.pdfgen import canvas


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PdfDownloadView(View):
    def get(self, request, *args, **kwargs):

        # Create file to recieve data and create the PDF
        buffer = io.BytesIO()

        # Create the file PDF
        pdf = canvas.Canvas(buffer)

        # Inserting in PDF where this 2 first arguments are axis X and Y respectvely
        pdf.drawString(50, 800, "Some Title")

        pdf.showPage()
        pdf.save()

        # Retrieving the file to start
        buffer.seek(0)

        # as_attachment=True to make file as an attachment to download
        return FileResponse(buffer, as_attachment=True, filename='report.pdf')


class PdfRenderView(View):
    def get(self, request, *args, **kwargs):

        # Create file to recieve data and create the PDF
        buffer = io.BytesIO()

        # Create the file PDF
        pdf = canvas.Canvas(buffer)

        # Inserting in PDF where this 2 first arguments are axis X and Y respectvely
        pdf.drawString(50, 800, "Some Title")

        pdf.showPage()
        pdf.save()

        # Retrieving the file to start
        buffer.seek(0)

        # By default, as_attachment=False
        return FileResponse(buffer, filename='report.pdf')
