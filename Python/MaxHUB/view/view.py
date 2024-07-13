# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewIokMJG.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.nameLayout = QHBoxLayout()
        self.nameLayout.setObjectName(u"nameLayout")
        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.nameEdit.setFont(font)

        self.nameLayout.addWidget(self.nameEdit)

        self.nameButton = QToolButton(self.centralwidget)
        self.nameButton.setObjectName(u"nameButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameButton.sizePolicy().hasHeightForWidth())
        self.nameButton.setSizePolicy(sizePolicy)
        self.nameButton.setMaximumSize(QSize(45, 16777215))

        self.nameLayout.addWidget(self.nameButton)


        self.verticalLayout_left.addLayout(self.nameLayout)

        self.line_left_up = QFrame(self.centralwidget)
        self.line_left_up.setObjectName(u"line_left_up")
        self.line_left_up.setMaximumSize(QSize(200, 16777215))
        self.line_left_up.setFrameShape(QFrame.HLine)
        self.line_left_up.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_left.addWidget(self.line_left_up)

        self.scrollListUser = QScrollArea(self.centralwidget)
        self.scrollListUser.setObjectName(u"scrollListUser")
        self.scrollListUser.setMaximumSize(QSize(200, 16777215))
        self.scrollListUser.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 476))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listUser = QVBoxLayout()
        self.listUser.setSpacing(0)
        self.listUser.setObjectName(u"listUser")
        self.listUser.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_2.addLayout(self.listUser)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollListUser.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_left.addWidget(self.scrollListUser)

        self.line_left_down = QFrame(self.centralwidget)
        self.line_left_down.setObjectName(u"line_left_down")
        self.line_left_down.setMaximumSize(QSize(200, 16777215))
        self.line_left_down.setFrameShape(QFrame.HLine)
        self.line_left_down.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_left.addWidget(self.line_left_down)

        self.horizontalLayout_panel = QHBoxLayout()
        self.horizontalLayout_panel.setObjectName(u"horizontalLayout_panel")
        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.btn_1 = QToolButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(22, 0))

        self.horizontalLayout_buttons.addWidget(self.btn_1)

        self.btn_2 = QToolButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(22, 0))

        self.horizontalLayout_buttons.addWidget(self.btn_2)

        self.btn_3 = QToolButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(22, 0))

        self.horizontalLayout_buttons.addWidget(self.btn_3)

        self.btn_4 = QToolButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(22, 0))

        self.horizontalLayout_buttons.addWidget(self.btn_4)


        self.horizontalLayout_panel.addLayout(self.horizontalLayout_buttons)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_panel.addItem(self.horizontalSpacer)

        self.sendButton = QToolButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")

        self.horizontalLayout_panel.addWidget(self.sendButton)


        self.verticalLayout_left.addLayout(self.horizontalLayout_panel)


        self.horizontalLayout_4.addLayout(self.verticalLayout_left)

        self.line_vertical = QFrame(self.centralwidget)
        self.line_vertical.setObjectName(u"line_vertical")
        self.line_vertical.setFrameShape(QFrame.VLine)
        self.line_vertical.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_vertical)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.scrollListMessages = QScrollArea(self.centralwidget)
        self.scrollListMessages.setObjectName(u"scrollListMessages")
        self.scrollListMessages.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 254, 494))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listMessage = QVBoxLayout()
        self.listMessage.setSpacing(0)
        self.listMessage.setObjectName(u"listMessage")

        self.verticalLayout.addLayout(self.listMessage)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollListMessages.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_right.addWidget(self.scrollListMessages)

        self.line_right = QFrame(self.centralwidget)
        self.line_right.setObjectName(u"line_right")
        self.line_right.setFrameShape(QFrame.HLine)
        self.line_right.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_right.addWidget(self.line_right)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 48))
        self.textEdit.setFont(font)

        self.verticalLayout_right.addWidget(self.textEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HUB messager", None))
        self.nameButton.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"send", None))
    # retranslateUi

