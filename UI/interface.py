# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
from UI import res_etinspector_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 461)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/C:/Users/Philipp/Downloads/dna.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.projectNameLabel = QLabel(Form)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.projectNameLabel.sizePolicy().hasHeightForWidth())
        self.projectNameLabel.setSizePolicy(sizePolicy1)
        self.projectNameLabel.setMinimumSize(QSize(0, 30))
        self.projectNameLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.projectNameLabel.setFont(font)
        self.projectNameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.projectNameLabel, 0, 0, 1, 2)

        self.exitButton = QPushButton(Form)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font)

        self.gridLayout.addWidget(self.exitButton, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loadButton = QPushButton(Form)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setFont(font)

        self.horizontalLayout.addWidget(self.loadButton)

        self.clearButton = QPushButton(Form)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setFont(font)

        self.horizontalLayout.addWidget(self.clearButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 378, 337))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.indentLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.indentLabel.setObjectName(u"indentLabel")
        self.indentLabel.setEnabled(False)
        self.indentLabel.setFont(font)
        self.indentLabel.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.indentLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.indentLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.indentLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"ET-Inspector", None))
        self.projectNameLabel.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0435\u043a\u0442 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.exitButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.loadButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.indentLabel.setText("")
    # retranslateUi

