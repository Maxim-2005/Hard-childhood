# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userfpSvKd.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_user(object):
    def setupUi(self, user):
        if not user.objectName():
            user.setObjectName(u"user")
        user.resize(206, 91)
        self.verticalLayout_2 = QVBoxLayout(user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.userID = QGroupBox(user)
        self.userID.setObjectName(u"userID")
        self.userID.setMaximumSize(QSize(16777215, 64))
        self.verticalLayout = QVBoxLayout(self.userID)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.avator = QGraphicsView(self.userID)
        self.avator.setObjectName(u"avator")
        self.avator.setMinimumSize(QSize(32, 32))
        self.avator.setMaximumSize(QSize(32, 32))
        self.avator.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.avator)

        self.nameLabel = QLabel(self.userID)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.nameLabel)

        self.horizontalSpacer = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.statusLabel = QLabel(self.userID)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy1)
        self.statusLabel.setMinimumSize(QSize(16, 0))
        self.statusLabel.setMaximumSize(QSize(16, 16777215))

        self.horizontalLayout.addWidget(self.statusLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.userID)


        self.retranslateUi(user)

        QMetaObject.connectSlotsByName(user)
    # setupUi

    def retranslateUi(self, user):
        user.setWindowTitle(QCoreApplication.translate("user", u"Form", None))
        self.userID.setTitle(QCoreApplication.translate("user", u"\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.nameLabel.setText(QCoreApplication.translate("user", u"User", None))
        self.statusLabel.setText(QCoreApplication.translate("user", u"\u25cf", None))
    # retranslateUi

