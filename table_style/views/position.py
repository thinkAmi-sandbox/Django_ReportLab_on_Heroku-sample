from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from .base import BaseView


class CellBase(BaseView):
    filename = 'cell_position.pdf'
    title = 'cell_position: '
    data = [
        ['(0, 0)', '(1, 0)', '(2, 0)', '(3, 0)', '(4, 0)'],     # 1行目
        ['(0, 1)', '(1, 1)', '(2, 1)', '(3, 1)', '(4, 1)'],     # 2行目
        ['(0, 2)', '(1, 2)', '(2, 2)', '(3, 2)', '(4, 2)'],     # 3行目
        ['(0, 3)', '(1, 3)', '(2, 3)', '(3, 3)', '(4, 3)'],     # 4行目
        ['(0, 4)', '(1, 4)', '(2, 4)', '(3, 4)', '(4, 4)'],     # 5行目
    ]
    # セルを指定する場合は、(列, 行)で指定
    start_cell = (0, 0)
    end_cell = (4, 4) 

    def _draw(self, doc):
        table = Table(self.data, colWidths=20*mm, rowHeights=10*mm)

        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            # 指定された範囲の背景色を変える
            ('BACKGROUND', self.start_cell, self.end_cell, colors.lightpink),
        ]))

        table.wrapOn(doc, 50*mm, 10*mm)
        table.drawOn(doc, 50*mm, 10*mm)
        doc.save()


class LeftCellOnly(CellBase):
    start_cell = (0, 0)
    end_cell = (0, 4)

class LeftCellOnlyWithMinus(CellBase):
    start_cell = (0, 0)
    # Pythonと同じように、マイナスindexも指定できる
    # http://www.pythonweb.jp/tutorial/string/index11.html
    end_cell = (0, -1)


class CenterCell(CellBase):
    start_cell = (1, 0)
    end_cell = (3, 4)

class CenterCellWithMinus(CellBase):
    start_cell = (1, 0)
    end_cell = (-2, -1)