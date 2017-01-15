from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^multi-rows$', BasicMultiRows.as_view(), name='multi-basic'),
    url(r'^multi-rows-bottomup$', BasicMultiRowsBottomup.as_view(), name='multi-bottomup'),
    url(r'^multi-rows-with-height-length$', MultiRowsWithHeightLength.as_view(), name='multi-with-height-length'),
    url(r'^position-left-cell-only$', LeftCellOnly.as_view(), name='pos-left-cell-only' ),
    url(r'^position-left-cell-only-minus$', LeftCellOnlyWithMinus.as_view(), name='pos-left-cell-only-minus' ),
    url(r'^position-center-cell$', CenterCell.as_view(), name='pos-center-cell' ),
    url(r'^position-center-cell-minus$', CenterCellWithMinus.as_view(), name='pos-center-cell-minus' ),
    url(r'^line-before$', LineBefore.as_view(), name='line-before'),
    url(r'^line-after$', LineAfter.as_view(), name='line-after'),
    url(r'^line-above$', LineAbove.as_view(), name='line-above'),
    url(r'^line-below$', LineBelow.as_view(), name='line-below'),
    url(r'^line-box$', LineBox.as_view(), name='line-box'),
    url(r'^line-outline$', LineOutline.as_view(), name='line-outline'),
    url(r'^line-inner-grid$', LineInnerGrid.as_view(), name='line-inner-grid'),
    url(r'^line-grid$', LineGrid.as_view(), name='line-grid'),
    url(r'^span$', Span.as_view(), name='span'),
]
