from typing import List, Optional

from PyQt5 import QtWidgets
from src.models.hymn import Hymn

from .hymn_widget import HymnWidget


class HymnListWidget(QtWidgets.QWidget):
    __hymns: List[Hymn] = []
    __hymn_widgets: List[HymnWidget] = []
    list_widget: QtWidgets.QListWidget

    def __init__(self, parent=None, *, list_widget: QtWidgets.QListWidget):
        super(HymnListWidget, self).__init__(parent)

        self.list_widget = list_widget

    @property
    def hymns(self) -> List[Hymn]:
        return self.__hymns

    @hymns.setter
    def hymns(self, hymns: List[Hymn]):
        self.__hymns = hymns
        self.render()

    def current_hymn(self) -> Hymn:
        current_row = self.list_widget.currentRow()
        return self.__hymns[current_row]

    def first_hymn(self) -> Optional[Hymn]:
        if len(self.__hymns) > 0:
            return self.__hymns[0]
        return None

    def render(self):
        self.list_widget.clear()
        self.__hymn_widgets = []

        for hymn in self.__hymns:
            list_widget_item = QtWidgets.QListWidgetItem(self.list_widget)
            hymn_widget = HymnWidget(self, hymn=hymn)
            self.__hymn_widgets.append(hymn_widget)
            list_widget_item.setSizeHint(hymn_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(list_widget_item, hymn_widget)
