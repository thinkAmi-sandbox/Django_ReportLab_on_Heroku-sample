from django.views import View
from django.http import HttpResponse

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas

class PdfView(View):
    def get(self, request, *args, **kwargs):
        # pdf用のContent-TypeやContent-Dispositionをセット
        response = HttpResponse(status=200, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="example.pdf"'
        # 即ダウンロードしたい時は、attachmentをつける
        # response['Content-Disposition'] = 'attachment; filename="example.pdf"'

        self._create_pdf(response)
        return response

    def _create_pdf(self, response):
        # 日本語が使えるゴシック体のフォントを設定する
        font_name = 'HeiseiKakuGo-W5'
        pdfmetrics.registerFont(UnicodeCIDFont(font_name))

        # A4縦書きのpdfを作る
        size = portrait(A4)

        # pdfを描く場所を作成：位置を決める原点は左上にする(bottomup)
        doc = canvas.Canvas(response, pagesize=size, bottomup=False)

        # フォントサイズをセットして字を表示
        doc.setFont(font_name, 9)
        doc.drawString(20*mm, 18*mm, 'はろーわーるど')

        # pdfの書き出し
        doc.save()
