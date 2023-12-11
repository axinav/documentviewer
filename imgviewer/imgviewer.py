
from PySide6.QtWidgets import (QDialog, QFileDialog, QGraphicsItem, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView,
                               QPlainTextEdit)
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QKeySequence, QPixmap
from PySide6.QtCore import QDir, QFile, QFileInfo, QTextStream, Qt, Slot

from abstractviewer import AbstractViewer
from imgviewer.QCImageViewer import QCImageViewer


class ImgViewer(AbstractViewer):
    def __init__(self):
        super().__init__()
        self.uiInitialized.connect(self.setupImgUi)

    def init(self,file, parent, mainWindow):
        self._imgView = QCImageViewer(parent)
        # self._imgView = QGraphicsView(parent)
        super().init(file, self._imgView, mainWindow)
        self._scene = QGraphicsScene()

    def viewerName(self):
        return "ImgViewer"

    def supportedMimeTypes(self):
        return ["image/jpeg", "image/png"]
    
    def setupImgUi(self):
        self.openFile()


    def openFile(self):
        fullName = QFileInfo(self._file)
        pixmap = QPixmap(fullName.filePath())
        item = QGraphicsPixmapItem(pixmap)
        self._imgView.load_single_image(fullName.filePath())
        # self._scene.addItem(item)
        # self._imgView.setScene(self._scene)
        # self._imgView.fitInView(pixmap.rect())
