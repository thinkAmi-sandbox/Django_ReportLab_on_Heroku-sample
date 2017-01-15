from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from .base import BaseView


class LineBase(BaseView):
    filename = 'line.pdf'
    title = 'line: '
    data = [
        ['(0, 0)', '(1, 0)', '(2, 0)', '(3, 0)', '(4, 0)'],     # 1行目
        ['(0, 1)', '(1, 1)', '(2, 1)', '(3, 1)', '(4, 1)'],     # 2行目
        ['(0, 2)', '(1, 2)', '(2, 2)', '(3, 2)', '(4, 2)'],     # 3行目
        ['(0, 3)', '(1, 3)', '(2, 3)', '(3, 3)', '(4, 3)'],     # 4行目
        ['(0, 4)', '(1, 4)', '(2, 4)', '(3, 4)', '(4, 4)'],     # 5行目
    ]
    # 罫線の種類
    line_type = None
    # 罫線の開始・終了位置(基本は一列目のみ罫線対応)
    start_cell = (0, 0)
    end_cell = (0, 4)

    def _draw(self, doc):
        table = Table(self.data, colWidths=20*mm, rowHeights=10*mm)

        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            # 決められた範囲で、太さや色を指定して、罫線を引く
            (self.line_type, self.start_cell, self.end_cell, 0.25, colors.black),
        ]))

        table.wrapOn(doc, 50*mm, 20*mm)
        table.drawOn(doc, 50*mm, 20*mm)
        doc.save()


class LineBefore(LineBase):
    # セルの左側に線を描く
    line_type = 'LINEBEFORE'

class LineAfter(LineBase):
    # セルの右側に線を描く
    line_type = 'LINEAFTER'


class LineAbove(LineBase):
    # セルの上側に線を描く(今回はセルの下側)
    # 今回はbottomup=Falseなので、AboveとBelowが入れ替わってることに注意
    line_type = 'LINEABOVE'

class LineBelow(LineBase):
    # セルの下側に線を描く(今回はセルの上側)
    # 今回はbottomup=Falseなので、AboveとBelowが入れ替わってることに注意
    line_type = 'LINEBELOW'


class LineBox(LineBase):
    # セルの範囲の外枠を描く
    line_type = 'BOX'

class LineOutline(LineBase):
    # BOXと同等で、セルの範囲の外枠を描く
    line_type = 'OUTLINE'


class LineInnerGrid(LineBase):
    # 範囲の内側に格子線を描く
    line_type = 'INNERGRID'
    # 一列だけだと分かりづらいので、中央のセルを選択する
    start_cell = (1, 1)
    end_cell = (3, 3)


class LineGrid(LineBase):
    # BOXとINNERGRIDを組み合わせたもの
    line_type = 'GRID'
    # 一列だけだと分かりづらいので、中央のセルを選択する
    start_cell = (1, 1)
    end_cell = (3, 3)

