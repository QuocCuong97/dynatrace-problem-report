# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 383)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\design\\../img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(False)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 521, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(220, 30, 291, 31))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 161, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 80, 291, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 521, 171))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 30, 291, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 80, 291, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 130, 291, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.label_5.setObjectName("label_5")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.clicked['QAbstractButton*'].connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.groupBox.setTitle(_translate("Dialog", "Dynatrace"))
        self.label.setText(_translate("Dialog", "Dynatrace Environment URL"))
        self.label_2.setText(_translate("Dialog", "Token API"))
        self.groupBox_2.setTitle(_translate("Dialog", "Output File"))
        self.label_3.setText(_translate("Dialog", "Title"))
        self.label_4.setText(_translate("Dialog", "Output Folder"))
        self.label_5.setText(_translate("Dialog", "File name prefix"))
        self.pushButton.setText(_translate("Dialog", "Save"))


def show_dialog():
    from tool import load_from_json, export_to_json
    dlg = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dlg)
    dlg.setWindowModality(QtCore.Qt.ApplicationModal)
    settings = load_from_json("settings.json")
    if settings["dynatrace"]["url"]:
        ui.lineEdit.setText(settings["dynatrace"]["url"])
    if settings["dynatrace"]["api-token"]:
        ui.lineEdit_2.setText(settings["dynatrace"]["api-token"])
    if settings["output_file"]["title"]:
        ui.lineEdit_3.setText(settings["output_file"]["title"])
    if settings["output_file"]["output_folder"]:
        ui.lineEdit_4.setText(settings["output_file"]["output_folder"])
    if settings["output_file"]["file_name_prefix"]:
        ui.lineEdit_5.setText(settings["output_file"]["file_name_prefix"])
    dlg.show()
    def save():
        new_settings = {
            "dynatrace": {
                "url": ui.lineEdit.text(),
                "api-token": ui.lineEdit_2.text()
            },
            "output_file": {
                "title": ui.lineEdit_3.text(),
                "output_folder": ui.lineEdit_4.text(),
                "file_name_prefix": ui.lineEdit_5.text()
            }
        }
        export_to_json(new_settings, "settings.json")
        dlg.close()
    ui.pushButton.clicked.connect(save)
    dlg.exec_()
