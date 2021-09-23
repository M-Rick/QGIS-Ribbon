import os
import re

from PyQt5.QtCore import Qt
from qgis.PyQt.QtGui import (
    QIcon, QPixmap
)
from qgis.PyQt.QtWidgets import (
    QWidget, QMessageBox, QGridLayout, QLabel, QDialogButtonBox, QScrollArea)


def normalize_path(path):
    return os.path.normpath(os.sep.join(re.split(r'\\|/', path)))


class CustomMessageBox(QMessageBox):
    

    def __init__(self, parent=None, text='', image=''):
        super(CustomMessageBox, self).__init__(parent)
        self.text = text

        self.rebuild_layout(text, image)

    def rebuild_layout(self, text, image):

        scrll = QScrollArea(self)
        scrll.setWidgetResizable(False)
        self.qwdt = QWidget()
        self.qwdt.setLayout(QGridLayout(self))
        grd = self.findChild(QGridLayout)
        if text:
            lbl = QLabel(text, self)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setWordWrap(False)
            lbl.setTextInteractionFlags(
                Qt.TextSelectableByMouse)
            self.qwdt.layout().addWidget(lbl, 1, 0)
        if image:
            px_lbl = QLabel(self)
            img_path = normalize_path(image)
            pixmap = QPixmap(img_path)
            px_lbl.setPixmap(pixmap)
            px_lbl.setMinimumSize(pixmap.width(), pixmap.height())
            px_lbl.setAlignment(Qt.AlignCenter)
            px_lbl.setWordWrap(False)
            self.qwdt.layout().addWidget(px_lbl, 0, 0)

        scrll.setWidget(self.qwdt)
        scrll.setContentsMargins(15, 5, 15, 10)
        grd.addWidget(scrll, 0, 1)
        self.layout().removeItem(self.layout().itemAt(0))
        self.layout().removeItem(self.layout().itemAt(0))
        self.setWindowTitle('QGIS Ribbon')

    def button_ok(self):
        self.setStandardButtons(QMessageBox.Ok)
        self.setDefaultButton(QMessageBox.Ok)
        self.set_proper_size()
        QMessageBox.exec_(self)

    def button_yes_no(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        self.set_proper_size()
        return QMessageBox.exec_(self)

    def button_yes_no_open(self):
        self.setStandardButtons(
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Open)
        self.setDefaultButton(QMessageBox.No)
        self.set_proper_size()
        return QMessageBox.exec_(self)

    def button_ok_open(self):
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Open)
        self.setDefaultButton(QMessageBox.Open)
        self.set_proper_size()
        return QMessageBox.exec_(self)

    def button_editr_close(self):
        self.setStandardButtons(
            QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard)
        self.setDefaultButton(QMessageBox.Discard)
        self.set_proper_size()
        return QMessageBox.exec_(self)

    def set_proper_size(self):
        scrll = self.findChild(QScrollArea)
        new_size = self.qwdt.sizeHint()
        if self.qwdt.sizeHint().height() > 600:
            new_size.setHeight(600)
        else:
            new_size.setHeight(self.qwdt.sizeHint().height())
        if self.qwdt.sizeHint().width() > 800:
            new_size.setWidth(800)
            new_size.setHeight(new_size.height() + 20)
        else:
            btn_box_width = self.findChild(QDialogButtonBox).sizeHint().width()
            if self.qwdt.sizeHint().width() > btn_box_width:
                new_size.setWidth(self.qwdt.sizeHint().width())
            else:
                new_size.setWidth(btn_box_width)
        scrll.setFixedSize(new_size)
        scrll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scrll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.show()
        scrll.horizontalScrollBar().setValue(
            int(scrll.horizontalScrollBar().maximum() / 2))
