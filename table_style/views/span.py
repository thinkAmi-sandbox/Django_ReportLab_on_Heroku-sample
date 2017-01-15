from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from .base import BaseView


class Span(BaseView):
    filename = 'span.pdf'
    title = 'span: '
    data = [
        ['(0, 0)', '(1, 0)', '(2, 0)', '(3, 0)', '(4, 0)'],     # 1行目
        ['(0, 1)', '(1, 1)', '(2, 1)', '(3, 1)', '(4, 1)'],     # 2行目
        ['(0, 2)', '(1, 2)', '(2, 2)', '(3, 2)', '(4, 2)'],     # 3行目
        ['(0, 3)', '(1, 3)', '(2, 3)', '(3, 3)', '(4, 3)'],     # 4行目
        ['(0, 4)', '(1, 4)', '(2, 4)', '(3, 4)', '(4, 4)'],     # 5行目
    ]

    def _draw(self, doc):
        table = Table(self.data, colWidths=20*mm, rowHeights=10*mm)

        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            # わかりやすくするため、全範囲をグリッドにしておく
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            # 指定した範囲のセルを結合して、背景色を入れる
            # ただし、結合した部分のデータは最初のセルを除いて削除されることに注意
            ('SPAN', (1, 1), (3, 3)),
            ('BACKGROUND', (1, 1), (2, 2), colors.lightpink),
        ]))

        table.wrapOn(doc, 50*mm, 20*mm)
        table.drawOn(doc, 50*mm, 20*mm)
        doc.save()
