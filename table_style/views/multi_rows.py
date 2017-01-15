from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from .base import BaseView

class BasicMultiRows(BaseView):
    filename = 'basic_multi_rows.pdf'
    title = 'basic_multi_rows: '

    def _draw(self, doc):
        # 複数行の表を用意したい場合、二次元配列でデータを用意する
        data = [
            ['行1-列1', '行1-列2-*********', '行1-列3-*********-*********'],
            ['行2-列1', '行2-列2-*********', '行2-列3-*********-*********'],
            ['行3-列1', '行3-列2-*********', '行3-列3-*********-*********'],
        ]

        table = Table(data)

        table.setStyle(TableStyle([
            # 表で使うフォントとそのサイズを設定
            ('FONT', (0, 0), (-1, -1), self.font_name, 9),
            # 四角に罫線を引いて、0.5の太さで、色は黒
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            # 四角の内側に格子状の罫線を引いて、0.25の太さで、色は赤
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.red),
            # セルの縦文字位置を、TOPにする
            # 他にMIDDLEやBOTTOMを指定できるのでお好みで
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        # tableを描き出す位置を指定
        table.wrapOn(doc, 50*mm, 10*mm)
        table.drawOn(doc, 50*mm, 10*mm)

        # pdfを保存
        doc.save()


class BasicMultiRowsBottomup(BasicMultiRows):
    filename = 'basic_multi_rows_bottomup.pdf'
    title = 'basic_multi_rows_bottomup: '
    is_bottomup = True


class MultiRowsWithHeightLength(BaseView):
    filename = 'multi_rows_with_height_length.pdf'
    title = 'basic_multi_rows_with_height_length: '

    def _draw(self, doc):
        data = [
            ['行1-列1', '行1-列2-*********', '行1-列3-*********-*********'],
            ['行2-列1', '行2-列2-*********', '行2-列3-*********-*********'],
            ['行3-列1', '行3-列2-*********', '行3-列3-*********-*********'],
        ]

        # 列・行ごとに幅や高さを指定したい場合、データと同じ順で指定する
        # 全て一律にしたい場合は、単一値を指定する
        table = Table(data, colWidths=(20*mm, 40*mm, 60*mm,), rowHeights=10*mm)

        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), self.font_name, 9),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.red),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        table.wrapOn(doc, 50*mm, 10*mm)
        table.drawOn(doc, 50*mm, 10*mm)
        doc.save()

