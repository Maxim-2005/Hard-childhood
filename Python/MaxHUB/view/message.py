# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messagegfQlmq.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_message(object):
    def setupUi(self, message):
        if not message.objectName():
            message.setObjectName(u"message")
        message.resize(266, 92)
        self.verticalLayout_2 = QVBoxLayout(message)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 32, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeLabel = QLabel(message)
        self.timeLabel.setObjectName(u"timeLabel")

        self.horizontalLayout_2.addWidget(self.timeLabel)

        self.userLabel = QLabel(message)
        self.userLabel.setObjectName(u"userLabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.userLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.userLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.messageText = QTextBrowser(message)
        self.messageText.setObjectName(u"messageText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageText.sizePolicy().hasHeightForWidth())
        self.messageText.setSizePolicy(sizePolicy)
        self.messageText.setMinimumSize(QSize(0, 28))

        self.verticalLayout.addWidget(self.messageText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.miniButton_1 = QToolButton(message)
        self.miniButton_1.setObjectName(u"miniButton_1")
        self.miniButton_1.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.miniButton_1)

        self.miniButton_2 = QToolButton(message)
        self.miniButton_2.setObjectName(u"miniButton_2")
        self.miniButton_2.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.miniButton_2)

        self.miniButton_3 = QToolButton(message)
        self.miniButton_3.setObjectName(u"miniButton_3")
        self.miniButton_3.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.miniButton_3)

        self.miniButton_4 = QToolButton(message)
        self.miniButton_4.setObjectName(u"miniButton_4")
        self.miniButton_4.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.miniButton_4)

        self.miniButton_5 = QToolButton(message)
        self.miniButton_5.setObjectName(u"miniButton_5")
        self.miniButton_5.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.miniButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(message)

        QMetaObject.connectSlotsByName(message)
    # setupUi

    def retranslateUi(self, message):
        message.setWindowTitle(QCoreApplication.translate("message", u"Form", None))
        self.timeLabel.setText(QCoreApplication.translate("message", u"2024.04.15 01:23:45", None))
        self.userLabel.setText(QCoreApplication.translate("message", u"User", None))
        self.miniButton_1.setText(QCoreApplication.translate("message", u"\u043b", None))
        self.miniButton_2.setText(QCoreApplication.translate("message", u"\u0430", None))
        self.miniButton_3.setText(QCoreApplication.translate("message", u"\u0439", None))
        self.miniButton_4.setText(QCoreApplication.translate("message", u"\u043a", None))
        self.miniButton_5.setText(QCoreApplication.translate("message", u"\u0438", None))
    # retranslateUi

