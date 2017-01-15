from django.http import HttpResponse
from django.views import View

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


# ドキュメントはこちら
# http://www.reportlab.com/documentation/
# ユーザガイドのp77あたりにTableStyleについての記載がある
# https://www.reportlab.com/docs/reportlab-userguide.pdf
class BaseView(View):
    filename = 'example.pdf'
    title = 'title: example'
    font_name = 'HeiseiKakuGo-W5'
    is_bottomup = False

    def get(self, request, *args, **kwargs):
        # pdf用のContent-TypeやContent-Dispositionをセット
        response = HttpResponse(status=200, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{}"'.format(self.filename)
        # 即ダウンロードしたい時は、attachmentをつける
        # response['Content-Disposition'] = 'attachment; filename="{}"'.format(self.filename)

        # 日本語が使えるゴシック体のフォントを設定する
        pdfmetrics.registerFont(UnicodeCIDFont(self.font_name))

        # A4縦書きのpdfを作る
        size = portrait(A4)

        # pdfを描く場所を作成：位置を決める原点は左上にする(bottomup)
        # デフォルトの原点は左下
        doc = canvas.Canvas(response, pagesize=size, bottomup=self.is_bottomup)

        # pdfのタイトルを設定
        doc.setTitle(self.title)

        # pdf上にも、タイトルとして使用したクラス名を表示する
        doc.drawString(10*mm, 10*mm, self.__class__.__name__)

        self._draw(doc)

        return response


    def _draw(self, doc):
        pass
        