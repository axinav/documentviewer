# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_copy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.11
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 630)
        icon = QIcon()
        icon.addFile(u":/demos/documentviewer/images/qt-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u"images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        iconThemeName = u"help-about"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/demos/documentviewer/images/help-about.svgz", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionAbout.setIcon(icon2)
        self.actionForward = QAction(MainWindow)
        self.actionForward.setObjectName(u"actionForward")
        icon3 = QIcon()
        icon3.addFile(u"images/go-next.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionBack = QAction(MainWindow)
        self.actionBack.setObjectName(u"actionBack")
        icon4 = QIcon()
        icon4.addFile(u"images/go-previous.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBack.setIcon(icon4)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionPrint.setEnabled(False)
        icon5 = QIcon()
        iconThemeName = u"document-print"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u":/demos/documentviewer/images/print2x.png", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionPrint.setIcon(icon5)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon6 = QIcon()
        icon6.addFile(u":/demos/documentviewer/images/qt-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/demos/documentviewer/images/qt-logo.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionAboutQt.setIcon(icon6)
        self.actionRecent = QAction(MainWindow)
        self.actionRecent.setObjectName(u"actionRecent")
        icon7 = QIcon()
        icon7.addFile(u":/demos/documentviewer/images/document-open-recent.svgz", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRecent.setIcon(icon7)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon8 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionQuit.setIcon(icon8)
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        icon9 = QIcon()
        icon9.addFile(u"images/imagefolder-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenFolder.setIcon(icon9)
        self.actionNewProject = QAction(MainWindow)
        self.actionNewProject.setObjectName(u"actionNewProject")
        icon10 = QIcon()
        icon10.addFile(u"images/newProject-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewProject.setIcon(icon10)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.viewArea = QWidget(self.centralwidget)
        self.viewArea.setObjectName(u"viewArea")
        self.horizontalLayout_3 = QHBoxLayout(self.viewArea)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(self.viewArea)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bySubjectPB = QPushButton(self.frame)
        self.bySubjectPB.setObjectName(u"bySubjectPB")

        self.horizontalLayout.addWidget(self.bySubjectPB)

        self.byObjectPB = QPushButton(self.frame)
        self.byObjectPB.setObjectName(u"byObjectPB")

        self.horizontalLayout.addWidget(self.byObjectPB)

        self.byDocTypePB = QPushButton(self.frame)
        self.byDocTypePB.setObjectName(u"byDocTypePB")

        self.horizontalLayout.addWidget(self.byDocTypePB)


        self.verticalLayout.addWidget(self.frame)

        self.docsTreeView = QTreeView(self.widget)
        self.docsTreeView.setObjectName(u"docsTreeView")

        self.verticalLayout.addWidget(self.docsTreeView)


        self.horizontalLayout_3.addWidget(self.widget)

        self.scrollArea = QScrollArea(self.viewArea)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 398, 513))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.widget_2 = QWidget(self.viewArea)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 470))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.subjectCB = QComboBox(self.groupBox)
        self.subjectCB.setObjectName(u"subjectCB")
        self.subjectCB.setEditable(False)

        self.gridLayout.addWidget(self.subjectCB, 0, 0, 1, 1)

        self.newSubjectPB = QPushButton(self.groupBox)
        self.newSubjectPB.setObjectName(u"newSubjectPB")
        self.newSubjectPB.setMaximumSize(QSize(51, 16777215))

        self.gridLayout.addWidget(self.newSubjectPB, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.objectCB = QComboBox(self.groupBox_2)
        self.objectCB.setObjectName(u"objectCB")
        self.objectCB.setEditable(False)

        self.horizontalLayout_2.addWidget(self.objectCB)

        self.newObjectPB = QPushButton(self.groupBox_2)
        self.newObjectPB.setObjectName(u"newObjectPB")
        self.newObjectPB.setMaximumSize(QSize(51, 16777215))

        self.horizontalLayout_2.addWidget(self.newObjectPB)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(291, 0))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 20, 291, 261))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.docNumberLE = QLineEdit(self.gridLayoutWidget_2)
        self.docNumberLE.setObjectName(u"docNumberLE")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.docNumberLE.sizePolicy().hasHeightForWidth())
        self.docNumberLE.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.docNumberLE, 2, 0, 1, 1)

        self.docNameLE = QLineEdit(self.gridLayoutWidget_2)
        self.docNameLE.setObjectName(u"docNameLE")

        self.gridLayout_3.addWidget(self.docNameLE, 1, 0, 1, 2)

        self.docAuthorLE = QLineEdit(self.gridLayoutWidget_2)
        self.docAuthorLE.setObjectName(u"docAuthorLE")

        self.gridLayout_3.addWidget(self.docAuthorLE, 3, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.docTypeCB = QComboBox(self.groupBox_5)
        self.docTypeCB.setObjectName(u"docTypeCB")
        self.docTypeCB.setGeometry(QRect(5, 21, 132, 22))

        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.docDataDE = QDateEdit(self.gridLayoutWidget_2)
        self.docDataDE.setObjectName(u"docDataDE")
        self.docDataDE.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.docDataDE, 2, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayoutWidget = QWidget(self.groupBox_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 20, 271, 61))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.firstPageLE = QLineEdit(self.gridLayoutWidget)
        self.firstPageLE.setObjectName(u"firstPageLE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.firstPageLE.sizePolicy().hasHeightForWidth())
        self.firstPageLE.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.firstPageLE, 1, 0, 1, 1)

        self.lastPageLE = QLineEdit(self.gridLayoutWidget)
        self.lastPageLE.setObjectName(u"lastPageLE")
        sizePolicy4.setHeightForWidth(self.lastPageLE.sizePolicy().hasHeightForWidth())
        self.lastPageLE.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.lastPageLE, 1, 1, 1, 1)

        self.getNextPagePB = QPushButton(self.gridLayoutWidget)
        self.getNextPagePB.setObjectName(u"getNextPagePB")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.getNextPagePB.sizePolicy().hasHeightForWidth())
        self.getNextPagePB.setSizePolicy(sizePolicy5)
        self.getNextPagePB.setMinimumSize(QSize(51, 0))

        self.gridLayout_2.addWidget(self.getNextPagePB, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 4, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy6)
        self.groupBox_6.setMinimumSize(QSize(0, 50))
        self.docSubTypeCB = QComboBox(self.groupBox_6)
        self.docSubTypeCB.setObjectName(u"docSubTypeCB")
        self.docSubTypeCB.setGeometry(QRect(5, 21, 131, 22))

        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.addDocBB = QDialogButtonBox(self.gridLayoutWidget_2)
        self.addDocBB.setObjectName(u"addDocBB")
        self.addDocBB.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.addDocBB, 5, 0, 1, 2)

        self.gridLayout_3.setRowStretch(0, 2)

        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalLayout_2.setStretch(2, 3)

        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.viewArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 18))
        self.qtFileMenu = QMenu(self.menubar)
        self.qtFileMenu.setObjectName(u"qtFileMenu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)

        self.menubar.addAction(self.qtFileMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.qtFileMenu.addAction(self.actionNewProject)
        self.qtFileMenu.addAction(self.actionOpen)
        self.qtFileMenu.addAction(self.actionOpenFolder)
        self.qtFileMenu.addAction(self.actionRecent)
        self.qtFileMenu.addAction(self.actionPrint)
        self.qtFileMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionRecent)
        self.mainToolBar.addAction(self.actionPrint)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionBack)
        self.mainToolBar.addAction(self.actionForward)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Document Viewer Demo", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"about documentviewer", None))
#if QT_CONFIG(tooltip)
        self.actionAbout.setToolTip(QCoreApplication.translate("MainWindow", u"Show information about the Document Viewer deomo.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionForward.setText(QCoreApplication.translate("MainWindow", u"actionForward", None))
#if QT_CONFIG(tooltip)
        self.actionForward.setToolTip(QCoreApplication.translate("MainWindow", u"One step forward", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionForward.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionBack.setText(QCoreApplication.translate("MainWindow", u"actionBack", None))
#if QT_CONFIG(tooltip)
        self.actionBack.setToolTip(QCoreApplication.translate("MainWindow", u"One step back", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionBack.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(tooltip)
        self.actionPrint.setToolTip(QCoreApplication.translate("MainWindow", u"Print current file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
#if QT_CONFIG(tooltip)
        self.actionAboutQt.setToolTip(QCoreApplication.translate("MainWindow", u"Show Qt license information", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAboutQt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecent.setText(QCoreApplication.translate("MainWindow", u"Recently opened...", None))
#if QT_CONFIG(shortcut)
        self.actionRecent.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Quit the application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionNewProject.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.bySubjectPB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0421\u0443\u0431\u044a\u0435\u043a\u0442\u0443", None))
        self.byObjectPB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u0443", None))
        self.byDocTypePB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0442\u0438\u043f\u0443 \u0434\u043e\u043a.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0431\u044a\u0435\u043a\u0442/\u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0434\u0435\u043b\u0430", None))
        self.subjectCB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0421\u0443\u0431\u044a\u0435\u043a\u0442", None))
        self.newSubjectPB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
#if QT_CONFIG(tooltip)
        self.objectCB.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.newObjectPB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.docNumberLE.setText("")
        self.docNumberLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.docNameLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.docAuthorLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e \u043f\u0440\u0438\u043d\u044f\u043b", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.docDataDE.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/M/yyyy", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b/\u0424\u0430\u0439\u043b\u044b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442", None))
        self.getNextPagePB.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0438\u043f", None))
        self.qtFileMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

