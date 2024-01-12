# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matching_plugin_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MatchingPluginDialogBase(object):
    def setupUi(self, MatchingPluginDialogBase):
        MatchingPluginDialogBase.setObjectName("MatchingPluginDialogBase")
        MatchingPluginDialogBase.resize(954, 742)
        self.verticalLayout = QtWidgets.QVBoxLayout(MatchingPluginDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(MatchingPluginDialogBase)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(9, 9, 66, 17))
        self.label.setObjectName("label")
        self.mMapLayerComboBoxCoucheAncienne = gui.QgsMapLayerComboBox(self.tab)
        self.mMapLayerComboBoxCoucheAncienne.setGeometry(QtCore.QRect(113, 9, 501, 25))
        self.mMapLayerComboBoxCoucheAncienne.setShowCrs(True)
        self.mMapLayerComboBoxCoucheAncienne.setObjectName("mMapLayerComboBoxCoucheAncienne")
        self.RunButton = QtWidgets.QPushButton(self.tab)
        self.RunButton.setGeometry(QtCore.QRect(590, 510, 80, 25))
        self.RunButton.setObjectName("RunButton")
        self.mMapLayerComboBoxCoucheRecente = gui.QgsMapLayerComboBox(self.tab)
        self.mMapLayerComboBoxCoucheRecente.setGeometry(QtCore.QRect(113, 40, 501, 25))
        self.mMapLayerComboBoxCoucheRecente.setShowCrs(True)
        self.mMapLayerComboBoxCoucheRecente.setObjectName("mMapLayerComboBoxCoucheRecente")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(9, 40, 89, 17))
        self.label_2.setObjectName("label_2")
        self.QgsFileWidget = gui.QgsFileWidget(self.tab)
        self.QgsFileWidget.setGeometry(QtCore.QRect(130, 310, 501, 21))
        self.QgsFileWidget.setObjectName("QgsFileWidget")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 101, 20))
        self.label_5.setObjectName("label_5")
        self.CloseButton = QtWidgets.QPushButton(self.tab)
        self.CloseButton.setGeometry(QtCore.QRect(490, 510, 81, 25))
        self.CloseButton.setObjectName("CloseButton")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(110, 450, 471, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(110, 420, 201, 17))
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(120, 360, 471, 23))
        self.checkBox.setObjectName("checkBox")
        self.mQgsProjectionSelectionWidget = gui.QgsProjectionSelectionWidget(self.tab)
        self.mQgsProjectionSelectionWidget.setGeometry(QtCore.QRect(200, 120, 411, 27))
        self.mQgsProjectionSelectionWidget.setObjectName("mQgsProjectionSelectionWidget")
        self.HelpButton = QtWidgets.QPushButton(self.tab)
        self.HelpButton.setGeometry(QtCore.QRect(10, 510, 89, 25))
        self.HelpButton.setObjectName("HelpButton")
        self.CancelButton = QtWidgets.QPushButton(self.tab)
        self.CancelButton.setGeometry(QtCore.QRect(590, 450, 81, 25))
        self.CancelButton.setObjectName("CancelButton")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 181, 20))
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(60, 180, 581, 92))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        icon = QtGui.QIcon.fromTheme("Parameters")
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(70, 20, 551, 501))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(80, 10, 691, 571))
        self.textEdit.setObjectName("textEdit")
        self.toolBtnSaveLog = QtWidgets.QToolButton(self.tab_2)
        self.toolBtnSaveLog.setGeometry(QtCore.QRect(710, 660, 26, 24))
        self.toolBtnSaveLog.setText("")
        self.toolBtnSaveLog.setObjectName("toolBtnSaveLog")
        self.toolBtnCopyLog = QtWidgets.QToolButton(self.tab_2)
        self.toolBtnCopyLog.setGeometry(QtCore.QRect(760, 660, 26, 24))
        self.toolBtnCopyLog.setText("")
        self.toolBtnCopyLog.setObjectName("toolBtnCopyLog")
        self.toolBtnClearLog = QtWidgets.QToolButton(self.tab_2)
        self.toolBtnClearLog.setGeometry(QtCore.QRect(830, 660, 26, 24))
        self.toolBtnClearLog.setText("")
        self.toolBtnClearLog.setObjectName("toolBtnClearLog")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, -30, 936, 724))
        self.tabWidget_2.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 66, 17))
        self.label_4.setObjectName("label_4")
        self.mMapLayerComboBoxCoucheAncienne_2 = gui.QgsMapLayerComboBox(self.tab_4)
        self.mMapLayerComboBoxCoucheAncienne_2.setGeometry(QtCore.QRect(113, 9, 501, 25))
        self.mMapLayerComboBoxCoucheAncienne_2.setShowCrs(True)
        self.mMapLayerComboBoxCoucheAncienne_2.setObjectName("mMapLayerComboBoxCoucheAncienne_2")
        self.RunButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.RunButton_2.setGeometry(QtCore.QRect(590, 510, 80, 25))
        self.RunButton_2.setObjectName("RunButton_2")
        self.mMapLayerComboBoxCoucheRecente_2 = gui.QgsMapLayerComboBox(self.tab_4)
        self.mMapLayerComboBoxCoucheRecente_2.setGeometry(QtCore.QRect(113, 40, 501, 25))
        self.mMapLayerComboBoxCoucheRecente_2.setShowCrs(True)
        self.mMapLayerComboBoxCoucheRecente_2.setObjectName("mMapLayerComboBoxCoucheRecente_2")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(9, 40, 89, 17))
        self.label_8.setObjectName("label_8")
        self.QgsFileWidget_2 = gui.QgsFileWidget(self.tab_4)
        self.QgsFileWidget_2.setGeometry(QtCore.QRect(130, 310, 501, 21))
        self.QgsFileWidget_2.setObjectName("QgsFileWidget_2")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 101, 20))
        self.label_9.setObjectName("label_9")
        self.CloseButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.CloseButton_2.setGeometry(QtCore.QRect(490, 510, 81, 25))
        self.CloseButton_2.setObjectName("CloseButton_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 450, 471, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(110, 420, 201, 17))
        self.label_10.setObjectName("label_10")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 360, 471, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.mQgsProjectionSelectionWidget_2 = gui.QgsProjectionSelectionWidget(self.tab_4)
        self.mQgsProjectionSelectionWidget_2.setGeometry(QtCore.QRect(200, 120, 411, 27))
        self.mQgsProjectionSelectionWidget_2.setObjectName("mQgsProjectionSelectionWidget_2")
        self.HelpButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.HelpButton_2.setGeometry(QtCore.QRect(10, 510, 89, 25))
        self.HelpButton_2.setObjectName("HelpButton_2")
        self.CancelButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.CancelButton_2.setGeometry(QtCore.QRect(590, 450, 81, 25))
        self.CancelButton_2.setObjectName("CancelButton_2")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 181, 20))
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 180, 581, 92))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        icon = QtGui.QIcon.fromTheme("Parameters")
        self.tabWidget_2.addTab(self.tab_4, icon, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget_2 = QtWidgets.QWidget(self.tab_5)
        self.widget_2.setGeometry(QtCore.QRect(70, 20, 551, 501))
        self.widget_2.setObjectName("widget_2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 70, 551, 511))
        self.textEdit_2.setObjectName("textEdit_2")
        self.toolBtnSaveLog_2 = QtWidgets.QToolButton(self.tab_6)
        self.toolBtnSaveLog_2.setGeometry(QtCore.QRect(500, 630, 26, 24))
        self.toolBtnSaveLog_2.setText("")
        self.toolBtnSaveLog_2.setObjectName("toolBtnSaveLog_2")
        self.toolBtnCopyLog_2 = QtWidgets.QToolButton(self.tab_6)
        self.toolBtnCopyLog_2.setGeometry(QtCore.QRect(540, 630, 26, 24))
        self.toolBtnCopyLog_2.setText("")
        self.toolBtnCopyLog_2.setObjectName("toolBtnCopyLog_2")
        self.toolBtnClearLog_2 = QtWidgets.QToolButton(self.tab_6)
        self.toolBtnClearLog_2.setGeometry(QtCore.QRect(580, 630, 26, 24))
        self.toolBtnClearLog_2.setText("")
        self.toolBtnClearLog_2.setObjectName("toolBtnClearLog_2")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(MatchingPluginDialogBase)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MatchingPluginDialogBase)

    def retranslateUi(self, MatchingPluginDialogBase):
        _translate = QtCore.QCoreApplication.translate
        MatchingPluginDialogBase.setWindowTitle(_translate("MatchingPluginDialogBase", "Matching Plugin"))
        self.label.setText(_translate("MatchingPluginDialogBase", "Old Layer:"))
        self.RunButton.setText(_translate("MatchingPluginDialogBase", "Run"))
        self.label_2.setText(_translate("MatchingPluginDialogBase", "Recent Layer"))
        self.QgsFileWidget.setToolTip(_translate("MatchingPluginDialogBase", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MatchingPluginDialogBase", "Matching links"))
        self.CloseButton.setText(_translate("MatchingPluginDialogBase", "Close"))
        self.label_6.setText(_translate("MatchingPluginDialogBase", "Waiting for you to click \'Run\'"))
        self.checkBox.setText(_translate("MatchingPluginDialogBase", "Open the output file after running the algorithm"))
        self.HelpButton.setText(_translate("MatchingPluginDialogBase", "Help"))
        self.CancelButton.setText(_translate("MatchingPluginDialogBase", "Cancel"))
        self.label_7.setText(_translate("MatchingPluginDialogBase", "Select the right projection"))
        self.groupBox.setTitle(_translate("MatchingPluginDialogBase", "Advanced parameters"))
        self.label_3.setText(_translate("MatchingPluginDialogBase", "Comparison method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MatchingPluginDialogBase", "Run processes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MatchingPluginDialogBase", "Data"))
        self.label_4.setText(_translate("MatchingPluginDialogBase", "Old Layer:"))
        self.RunButton_2.setText(_translate("MatchingPluginDialogBase", "Run"))
        self.label_8.setText(_translate("MatchingPluginDialogBase", "Recent Layer"))
        self.QgsFileWidget_2.setToolTip(_translate("MatchingPluginDialogBase", "<html><head/><body><p><br/></p></body></html>"))
        self.label_9.setText(_translate("MatchingPluginDialogBase", "Matching links"))
        self.CloseButton_2.setText(_translate("MatchingPluginDialogBase", "Close"))
        self.label_10.setText(_translate("MatchingPluginDialogBase", "Waiting for you to click \'Run\'"))
        self.checkBox_2.setText(_translate("MatchingPluginDialogBase", "Open the output file after running the algorithm"))
        self.HelpButton_2.setText(_translate("MatchingPluginDialogBase", "Help"))
        self.CancelButton_2.setText(_translate("MatchingPluginDialogBase", "Cancel"))
        self.label_11.setText(_translate("MatchingPluginDialogBase", "Select the right projection"))
        self.groupBox_2.setTitle(_translate("MatchingPluginDialogBase", "Advanced parameters"))
        self.label_12.setText(_translate("MatchingPluginDialogBase", "Comparison method"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MatchingPluginDialogBase", "Run processes"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MatchingPluginDialogBase", "Data"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MatchingPluginDialogBase", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MatchingPluginDialogBase", "Log"))
from qgis import gui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MatchingPluginDialogBase = QtWidgets.QDialog()
    ui = Ui_MatchingPluginDialogBase()
    ui.setupUi(MatchingPluginDialogBase)
    MatchingPluginDialogBase.show()
    sys.exit(app.exec_())
