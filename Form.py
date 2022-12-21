# -*- coding: utf-8 -*-
from PyQt6.QtWidgets import QButtonGroup
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QCheckBox, QGroupBox, QPushButton,
                             QRadioButton)


class Ui_launcher(object):
    def setupUi(self, launcher):
        if not launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.resize(505, 377)
        self.radioButton_3 = QRadioButton(launcher)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(40, 150, 201, 31))
        font = QFont()
        font.setPointSize(15)
        self.radioButton_3.setFont(font)
        self.radioButton_2 = QRadioButton(launcher)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(40, 90, 201, 41))
        self.radioButton_2.setFont(font)
        self.pushButton = QPushButton(launcher)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 240, 221, 91))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.radioButton = QRadioButton(launcher)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 40, 181, 41))
        self.radioButton.setFont(font)
        self.groupBox = QGroupBox(launcher)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(250, 40, 241, 151))
        font2 = QFont()
        font2.setPointSize(12)
        self.groupBox.setFont(font2)
        self.xformer = QCheckBox(self.groupBox)
        self.xformer.setObjectName(u"xformer")
        self.xformer.setGeometry(QRect(10, 30, 141, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.xformer.setFont(font3)
        self.deepdanbooru = QCheckBox(self.groupBox)
        self.deepdanbooru.setObjectName(u"deepdanbooru")
        self.deepdanbooru.setGeometry(QRect(10, 60, 201, 21))
        self.deepdanbooru.setFont(font3)
        self.autolaunch = QCheckBox(self.groupBox)
        self.autolaunch.setObjectName(u"autolaunch")
        self.autolaunch.setGeometry(QRect(10, 90, 121, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.autolaunch.setFont(font4)
        self.administrator = QCheckBox(self.groupBox)
        self.administrator.setObjectName(u"administrator")
        self.administrator.setGeometry(QRect(10, 120, 121, 20))
        self.administrator.setFont(font3)
        self.groupBox.raise_()
        self.radioButton_3.raise_()
        self.radioButton_2.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()

        self.levels = QButtonGroup()
        self.levels.addButton(self.radioButton, 1)
        self.levels.addButton(self.radioButton_2, 2)
        self.levels.addButton(self.radioButton_3, 3)

        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)

    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"launcher", None))
        self.radioButton_3.setText(
            QCoreApplication.translate("launcher", u"\u4f4e\u663e\u5b58\uff084G\u53ca\u4ee5\u4e0b\uff09", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("launcher", u"\u4e2d\u663e\u5b58\uff086G\u53ca\u4ee5\u4e0a\uff09", None))
        self.pushButton.setText(QCoreApplication.translate("launcher", u"\u542f\u52a8", None))
        self.radioButton.setText(
            QCoreApplication.translate("launcher", u"\u9ad8\u663e\u5b58\uff088G\u4ee5\u4e0a\uff09", None))
        self.groupBox.setTitle(QCoreApplication.translate("launcher", u"\u53c2\u6570\u5217\u8868", None))
        self.xformer.setText(QCoreApplication.translate("launcher", u"xformer", None))
        self.deepdanbooru.setText(QCoreApplication.translate("launcher", u"deepdanbooru", None))
        self.autolaunch.setText(QCoreApplication.translate("launcher", u"autolaunch", None))
        self.administrator.setText(QCoreApplication.translate("launcher", u"administrator", None))
    # retranslateUi
