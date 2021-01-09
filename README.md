# QT-ImageWidget

You can use this widget to display pixmap with keeping aspect ratio. It is mutch faster and mutch better than `QPixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)`

## Exapmle

```
self.viewer_1 = ImageWidget(self.layout_main)  # create the widget
self.viewer_1.setScaleDownOnly(True)  # prevent image upscaling
self.viewer_1.setObjectName("viewer_1")  # set object name
```
