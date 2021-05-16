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


def show_dialog():
    dlg = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dlg)
    dlg.setWindowModality(QtCore.Qt.ApplicationModal)
    dlg.show()
    dlg.exec_()


    def methods(self):
        import settings, about, logics
        
        def show_success_msg():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(".\\design\\../img/logo_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setWindowTitle("Info")
            msg.setText("Export successfully!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        def get_report():
            try:
                logics.main("now-30d", "now")
                show_success_msg()
            except:
                pass
            
        self.actionSettings_2.triggered.connect(settings.show_dialog)
        self.actionAbout.triggered.connect(about.show_dialog)
        self.pushButton.clicked.connect(get_report)
