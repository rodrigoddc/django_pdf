from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView

from weasyprint import HTML


class PDFRenderView(View):
    def get(self, request, *args, **kwargs):
        text = [
            'Hello',
            'World',
            'Foo',
            'Bar',
        ]

        html_string = render_to_string('core/weasyprint/base_pdf.html', {'text': text})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/report2.pdf')

        # Django built-in
        fs = FileSystemStorage('/tmp/')

        with fs.open('report2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # inline: make file to be open as to print
            response['Content-Disposition'] = 'filename="report2.pdf"'

        return response


class PDFDownloadView(View):
    def get(self, request, *args, **kwargs):
        text = [
            'Hello',
            'World',
            'Foo',
            'Bar',
        ]

        html_string = render_to_string('core/weasyprint/base_pdf.html', {'text': text})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/report2.pdf')

        # Django built-in
        fs = FileSystemStorage('/tmp/')

        with fs.open('report2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # attachment make file content to de downloaded
            response['Content-Disposition'] = 'attachment; filename="report2.pdf"'

        return response


