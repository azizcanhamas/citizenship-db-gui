# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

#import SQLite library.
import sqlite3 as sql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 525))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1920, 518))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.useridLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.useridLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.useridLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.useridLabel.setObjectName("useridLabel")
        self.gridLayout.addWidget(self.useridLabel, 0, 0, 1, 1)
        self.gender = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gender.setMinimumSize(QtCore.QSize(118, 35))
        self.gender.setMaximumSize(QtCore.QSize(118, 35))
        self.gender.setObjectName("gender")
        self.gridLayout.addWidget(self.gender, 6, 0, 1, 1)
        
        self.resTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.resTable.setMinimumSize(QtCore.QSize(1200, 500))
        self.resTable.setMaximumSize(QtCore.QSize(1200, 500))
        self.resTable.setObjectName("resTable")
        #=== Configure table.
        #create 12 column.
        self.resTable.setColumnCount(12)
        #define column names.
        self.resTable.setHorizontalHeaderLabels(["user_id","nat_identifier","first_name","last_name","mother_name","father_name","gender","birth_city","date_of_birth","reg_city","reg_district","reg_address"])
        self.resTable.setDisabled(False)
        #make rows uneditable.
        self.resTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        #===================        
        
        self.gridLayout.addWidget(self.resTable, 0, 2, 14, 1)
        self.regaddressText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.regaddressText.setMinimumSize(QtCore.QSize(450, 35))
        self.regaddressText.setMaximumSize(QtCore.QSize(450, 35))
        self.regaddressText.setObjectName("regaddressText")
        self.gridLayout.addWidget(self.regaddressText, 11, 1, 1, 1)
        self.firstText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.firstText.setMinimumSize(QtCore.QSize(450, 35))
        self.firstText.setMaximumSize(QtCore.QSize(450, 35))
        self.firstText.setObjectName("firstText")
        self.gridLayout.addWidget(self.firstText, 2, 1, 1, 1)
        self.birthText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.birthText.setMinimumSize(QtCore.QSize(450, 35))
        self.birthText.setMaximumSize(QtCore.QSize(450, 35))
        self.birthText.setObjectName("birthText")
        self.gridLayout.addWidget(self.birthText, 7, 1, 1, 1)
        self.regdistText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.regdistText.setMinimumSize(QtCore.QSize(450, 35))
        self.regdistText.setMaximumSize(QtCore.QSize(450, 35))
        self.regdistText.setObjectName("regdistText")
        self.gridLayout.addWidget(self.regdistText, 10, 1, 1, 1)
        self.dateText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.dateText.setMinimumSize(QtCore.QSize(450, 35))
        self.dateText.setMaximumSize(QtCore.QSize(450, 35))
        self.dateText.setObjectName("dateText")
        self.gridLayout.addWidget(self.dateText, 8, 1, 1, 1)
        self.identifierText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.identifierText.setMinimumSize(QtCore.QSize(450, 35))
        self.identifierText.setMaximumSize(QtCore.QSize(450, 35))
        self.identifierText.setObjectName("identifierText")
        self.gridLayout.addWidget(self.identifierText, 1, 1, 1, 1)
        self.lastText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.lastText.setMinimumSize(QtCore.QSize(450, 35))
        self.lastText.setMaximumSize(QtCore.QSize(450, 35))
        self.lastText.setObjectName("lastText")
        self.gridLayout.addWidget(self.lastText, 3, 1, 1, 1)
        self.useridText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.useridText.setMinimumSize(QtCore.QSize(450, 35))
        self.useridText.setMaximumSize(QtCore.QSize(450, 35))
        self.useridText.setObjectName("useridText")
        self.gridLayout.addWidget(self.useridText, 0, 1, 1, 1)
        self.motherLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.motherLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.motherLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.motherLabel.setObjectName("motherLabel")
        self.gridLayout.addWidget(self.motherLabel, 4, 0, 1, 1)
        self.fatherText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.fatherText.setMinimumSize(QtCore.QSize(450, 35))
        self.fatherText.setMaximumSize(QtCore.QSize(450, 35))
        self.fatherText.setObjectName("fatherText")
        self.gridLayout.addWidget(self.fatherText, 5, 1, 1, 1)
        self.firstLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.firstLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.firstLabel.setObjectName("firstLabel")
        self.gridLayout.addWidget(self.firstLabel, 2, 0, 1, 1)
        self.regaddLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.regaddLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.regaddLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.regaddLabel.setObjectName("regaddLabel")
        self.gridLayout.addWidget(self.regaddLabel, 11, 0, 1, 1)
        self.regcityText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.regcityText.setMinimumSize(QtCore.QSize(450, 35))
        self.regcityText.setMaximumSize(QtCore.QSize(450, 35))
        self.regcityText.setObjectName("regcityText")
        self.gridLayout.addWidget(self.regcityText, 9, 1, 1, 1)
        self.lastLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lastLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.lastLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.lastLabel.setObjectName("lastLabel")
        self.gridLayout.addWidget(self.lastLabel, 3, 0, 1, 1)
        self.genderComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.genderComboBox.setMinimumSize(QtCore.QSize(450, 35))
        self.genderComboBox.setMaximumSize(QtCore.QSize(450, 35))
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.gridLayout.addWidget(self.genderComboBox, 6, 1, 1, 1)
        self.fatherLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fatherLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.fatherLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.fatherLabel.setObjectName("fatherLabel")
        self.gridLayout.addWidget(self.fatherLabel, 5, 0, 1, 1)
        self.motherText = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.motherText.setMinimumSize(QtCore.QSize(450, 35))
        self.motherText.setMaximumSize(QtCore.QSize(450, 35))
        self.motherText.setObjectName("motherText")
        self.gridLayout.addWidget(self.motherText, 4, 1, 1, 1)
        self.identifierLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.identifierLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.identifierLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.identifierLabel.setObjectName("identifierLabel")
        self.gridLayout.addWidget(self.identifierLabel, 1, 0, 1, 1)
        self.regcityLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.regcityLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.regcityLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.regcityLabel.setObjectName("regcityLabel")
        self.gridLayout.addWidget(self.regcityLabel, 9, 0, 1, 1)
        self.dateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dateLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.dateLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 8, 0, 1, 1)
        self.regdistLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.regdistLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.regdistLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.regdistLabel.setObjectName("regdistLabel")
        self.gridLayout.addWidget(self.regdistLabel, 10, 0, 1, 1)
        self.birthLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.birthLabel.setMinimumSize(QtCore.QSize(118, 35))
        self.birthLabel.setMaximumSize(QtCore.QSize(118, 35))
        self.birthLabel.setObjectName("birthLabel")
        self.gridLayout.addWidget(self.birthLabel, 7, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.resetButton.setMinimumSize(QtCore.QSize(450, 35))
        self.resetButton.setMaximumSize(QtCore.QSize(450, 35))
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 13, 1, 1, 1)
        self.queryButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.queryButton.setMinimumSize(QtCore.QSize(450, 35))
        self.queryButton.setMaximumSize(QtCore.QSize(450, 35))
        self.queryButton.setObjectName("queryButton")
        self.gridLayout.addWidget(self.queryButton, 12, 1, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.statusLabel.setMinimumSize(QtCore.QSize(0, 35))
        self.statusLabel.setMaximumSize(QtCore.QSize(16777215, 35))
        self.statusLabel.setObjectName("label")
        self.gridLayout.addWidget(self.statusLabel, 13, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #=== Define button events
        self.queryButton.clicked.connect(self.query_clicked)
        self.resetButton.clicked.connect(self.reset_clicked)
        #================
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Citizenship Database"))
        self.useridLabel.setText(_translate("MainWindow", "User ID"))
        self.gender.setText(_translate("MainWindow", "Gender"))
        self.motherLabel.setText(_translate("MainWindow", "Mother Name"))
        self.firstLabel.setText(_translate("MainWindow", "First Name"))
        self.regaddLabel.setText(_translate("MainWindow", "Registration Address"))
        self.lastLabel.setText(_translate("MainWindow", "Last Name"))
        self.genderComboBox.setItemText(0, _translate("MainWindow", "E"))
        self.genderComboBox.setItemText(1, _translate("MainWindow", "K"))
        self.fatherLabel.setText(_translate("MainWindow", "Father Name"))
        self.identifierLabel.setText(_translate("MainWindow", "National Identifier"))
        self.regcityLabel.setText(_translate("MainWindow", "Registration City"))
        self.dateLabel.setText(_translate("MainWindow", "Date of Birth"))
        self.regdistLabel.setText(_translate("MainWindow", "Registration District"))
        self.birthLabel.setText(_translate("MainWindow", "Birth City/District"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.queryButton.setText(_translate("MainWindow", "Query"))
        self.statusLabel.setText(_translate("MainWindow", "          Status"))

    #Create button events.
    def query_clicked(self):
        self.statusLabel.setText("Applying query...")
        
        #Clear table.
        while self.resTable.rowCount() > 0:
            self.resTable.removeRow(0)
        
        #Connnect database and create cursor for queries.
        db=sql.connect("citizens_db.sqlite")
        cursor=db.cursor()
        
        #Get entered values from textboxes and create query string.
        arr=[self.useridText,self.identifierText,self.firstText,self.lastText,self.motherText,
             self.fatherText,self.birthText,self.dateText,self.regcityText,
             self.regdistText,self.regaddressText] #self.genderComboBox
        sql_str_param=[
                " user_id=(?) AND",
                " national_identifier=(?) AND",
                " first_name=(?) AND",
                " last_name=(?) AND",
                " mother_name=(?) AND",
                " father_name=(?) AND",
                " birth_city=(?) AND",
                " date_of_birth=(?) AND",
                " registration_city=(?) AND",
                " registration_district=(?) AND",
                " registration_address=(?) AND"]
        
        values=[]     
        query_str="SELECT * FROM citizens WHERE "
        
        for i in range(0,len(arr)):
            value=arr[i].toPlainText()
            if not value=="":    
                values.append(value)
                query_str+=sql_str_param[i]
                
        values.append(self.genderComboBox.currentText())
        query_str+=" gender=(?)"
        
        #Fetch results and write rows the table.
        res=cursor.execute(query_str,tuple(values))
        fetched=res.fetchall()
        for i in range(0,len(fetched)):
            self.resTable.insertRow(i)
            for z in range(0,len(fetched[i])):
                self.resTable.setItem(i, z, QtWidgets.QTableWidgetItem(fetched[i][z]))
        
        self.statusLabel.setText("Query completed!")
        db.close()
        
    def reset_clicked(self):
        self.statusLabel.setText("Cleaned all boxes!")
        self.useridText.setText("")
        self.identifierText.setText("")
        self.firstText.setText("")
        self.lastText.setText("")
        self.motherText.setText("")
        self.fatherText.setText("")
        self.genderComboBox.setCurrentIndex(0)
        self.birthText.setText("")
        self.dateText.setText("")
        self.regcityText.setText("")
        self.regdistText.setText("")
        self.regaddressText.setText("")
        
        while self.resTable.rowCount() > 0:
            self.resTable.removeRow(0)
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

