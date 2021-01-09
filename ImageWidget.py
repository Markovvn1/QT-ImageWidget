from PyQt5 import QtCore, QtWidgets


class ImageWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__scale_down_only = False
        self.__canvas = QtWidgets.QLabel(self)

        self.__canvas.setText("")
        self.__canvas.setScaledContents(True)

    def setObjectName(self, name):
        super().setObjectName(name)
        self.__canvas.setObjectName(name + "_canvas")

    def resizeEvent(self, event):
        pixmap = self.__canvas.pixmap()
        
        if pixmap is not None:
            size = pixmap.size()
            vp = event.size()

            size.scale(vp, QtCore.Qt.KeepAspectRatio)
            w, h = size.width(), size.height()
            if self.__scale_down_only:
                w, h = min(w, pixmap.width()), min(h, pixmap.height())

            dx = vp.width() - w
            dy = vp.height() - h

            self.__canvas.setGeometry(dx // 2, dy // 2, w, h)
        super().resizeEvent(event)

    def setPixmap(self, image):
        self.__canvas.setPixmap(image)

    def setScaleDownOnly(self, value):
        self.__scale_down_only = value