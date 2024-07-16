from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:#F0E9D2;\n"
"font: 9pt \"Segoe UI\";")
        
        icon = QtGui.QIcon(r"C:\Users\snehs\Downloads\1322164.png")
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"text-align:right;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #28a745;\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"    border-style:outset;\n"
"    color: rgb(0, 0, 0);\n"
"cursor: pointer;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 51, 41))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ico/icons/filogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 40, 421, 61))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset;     /* Outset border style */\n"
"    font-size: 20px;          /* Font size */\n"
"    font-family: \"MS Shell Dlg 2\"; /* Font family */\n"
"    color: white\n"
"}\n"
"")
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.selection = QtWidgets.QWidget(self.centralwidget)
        self.selection.setGeometry(QtCore.QRect(50, 130, 651, 331))
        self.selection.setStyleSheet("#selection {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.selection.setObjectName("selection")
        self.TelemetryData_2 = QtWidgets.QLineEdit(self.selection)
        self.TelemetryData_2.setEnabled(False)
        self.TelemetryData_2.setGeometry(QtCore.QRect(170, 20, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TelemetryData_2.sizePolicy().hasHeightForWidth())
        self.TelemetryData_2.setSizePolicy(sizePolicy)
        self.TelemetryData_2.setStyleSheet("border-style:outset;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(30, 144, 255);\n"
"color: rgb(0, 0, 0);")
        self.TelemetryData_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TelemetryData_2.setReadOnly(True)
        self.TelemetryData_2.setObjectName("TelemetryData_2")
        self.BaudRate_2 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_2.setEnabled(False)
        self.BaudRate_2.setGeometry(QtCore.QRect(160, 90, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_2.sizePolicy().hasHeightForWidth())
        self.BaudRate_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BaudRate_2.setFont(font)
        self.BaudRate_2.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: #ffffff;\n"
"font-weight: bold;")
        self.BaudRate_2.setFrame(False)
        self.BaudRate_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_2.setReadOnly(True)
        self.BaudRate_2.setObjectName("BaudRate_2")
        self.BaudRate_3 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_3.setEnabled(False)
        self.BaudRate_3.setGeometry(QtCore.QRect(10, 140, 111, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_3.sizePolicy().hasHeightForWidth())
        self.BaudRate_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BaudRate_3.setFont(font)
        self.BaudRate_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.BaudRate_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_3.setReadOnly(True)
        self.BaudRate_3.setObjectName("BaudRate_3")
        self.BaudRate_5 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_5.setEnabled(False)
        self.BaudRate_5.setGeometry(QtCore.QRect(410, 90, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_5.sizePolicy().hasHeightForWidth())
        self.BaudRate_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BaudRate_5.setFont(font)
        self.BaudRate_5.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: #ffffff;\n"
"font-weight: bold;")
        self.BaudRate_5.setFrame(False)
        self.BaudRate_5.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_5.setReadOnly(True)
        self.BaudRate_5.setObjectName("BaudRate_5")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.selection)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_2.setStyleSheet("QDateEdit{\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px; /* Width of the dropdown button */\n"
"    border-left: solid #1E90FF; /* Border for the dropdown button */\n"
"    /* background-color: rgb(255, 255, 255); */\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QCalendarWidget styles */\n"
"QCalendarWidget {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QCalendarWidget navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #1E90FF; /* Background color of the navigation bar */\n"
"}\n"
"\n"
"/* QCalendarWidget header row */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar QToolButton {\n"
"    color: white; /* Text color of the navigation bar buttons */\n"
"    background-color: #1E90FF; /* Background color of the navigation bar buttons */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth, \n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* QCalendarWidget header row - month and year */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"    color: white; /* Text color for month and year */\n"
"    background-color: black; /* Background color for month and year */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"/* Ensure the text color is white when these buttons are focused, active, or selected */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:checked, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:checked {\n"
"    color: white; /* Text color for month and year when focused, pressed, or checked */\n"
"}\n"
"\n"
"/* QMenu (dropdown list) styling for the month list */\n"
"QMenu {\n"
"    background-color: #1E90FF; /* Background color of the dropdown menu */\n"
"    color: white; /* Text color of the dropdown menu items */\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: black; /* Background color of each item */\n"
"    color: white; /* Text color of each item */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #1E90FF; /* Text color of the selected item */\n"
"}\n"
"\n"
"/* QCalendarWidget selected date */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: blue; /* Text color */\n"
"    selection-background-color: #1E90FF; /* Background color for selected date */\n"
"    selection-color: black; /* Text color for selected date */\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    outline: 0;\n"
"}\n"
"")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.selection)
        self.timeEdit_2.setGeometry(QtCore.QRect(370, 140, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_2.sizePolicy().hasHeightForWidth())
        self.timeEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.timeEdit_2.setAutoFillBackground(False)
        self.timeEdit_2.setStyleSheet("QTimeEdit {\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Style the up and down buttons */\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 20px;\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"/* Style the up arrow */\n"
"QTimeEdit::up-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-bottom: 6px solid white; /* Arrow color */\n"
"}\n"
"\n"
"/* Style the down arrow */\n"
"QTimeEdit::down-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid white; /* Arrow color */\n"
"}\n"
"\n"
"  ")
        self.timeEdit_2.setWrapping(False)
        self.timeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeEdit_2.setAccelerated(False)
        self.timeEdit_2.setProperty("showGroupSeparator", False)
        self.timeEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.Start_3 = QtWidgets.QPushButton(self.selection)
        self.Start_3.setGeometry(QtCore.QRect(270, 230, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_3.sizePolicy().hasHeightForWidth())
        self.Start_3.setSizePolicy(sizePolicy)
        self.Start_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_3.setStyleSheet("QPushButton{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"text-align:right;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 167, 69);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color: #4caf50;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Start_3.setObjectName("Start_3")
        self.label_3 = QtWidgets.QLabel(self.selection)
        self.label_3.setGeometry(QtCore.QRect(290, 240, 31, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/ico/icons/check.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Open File<br/></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        self.TelemetryData_2.setText(_translate("MainWindow", "Date & Time Selection"))
        self.BaudRate_2.setText(_translate("MainWindow", "Date"))
        self.BaudRate_3.setText(_translate("MainWindow", "Start :"))
        self.BaudRate_5.setText(_translate("MainWindow", "Time"))
        self.timeEdit_2.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.Start_3.setText(_translate("MainWindow", "Submit"))
import ico_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
