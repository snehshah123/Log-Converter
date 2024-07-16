import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
import pandas as pd
import csv
import os
from datetime import datetime,timedelta
from LogFileUpdate import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_file_dialog)
        self.ui.Start_3.clicked.connect(self.submit_clicked)

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text and Log Files (*.log *.txt);;Log Files (*.log);;Text Files (*.txt)", options=options)
        if file_name:
            self.load_txt(file_name)
        else:    
            self.ui.lineEdit.setText("No File Selected")
            

    def load_txt(self, file_name):
        df = pd.read_csv(file_name, header=None)
        if not df.empty:
            base_name = os.path.basename(file_name)
            self.ui.lineEdit.setText(base_name)

        output_file_path = 'temp.csv'

        with open(file_name, 'r') as txt_file:
            lines = txt_file.readlines()

        with open(output_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Write header
            header = lines[0].strip().split()
            writer.writerow(header)

            # Write data rows
            for line in lines[1:]:
                row = line.strip().split()
                writer.writerow(row)

        print(f"Conversion completed. 'temp' created.")


    def submit_clicked(self):
        start_date = self.ui.dateEdit_2.date().toString("dd-MM-yy")
        start_time = self.ui.timeEdit_2.time().toString("hh:mm:ss")

        csv_file_path = r"temp.csv"
        df = pd.read_csv(csv_file_path,header = None)
        df = df.drop([0,df.columns[-1]],axis = 'columns')
        columns_to_drop = list(range(4, df.shape[1]+1, 2))
        df = df.drop(columns_to_drop,axis = 'columns')
        df[1] = df[1].str.replace('/', '-')
        df.to_csv(csv_file_path, index=False, header=False)
        
        csv_file_path = r"temp.csv"
        df = pd.read_csv(csv_file_path,header = None)
        dates = df[0].tolist()
        
        date_format = "%d-%m-%y"
        new_dates = [start_date]
        for i in range(1, len(dates)):
            previous_new_date = new_dates[-1]
            if self.check_date_increase(dates[i-1], dates[i], date_format):
                new_date = (datetime.strptime(previous_new_date, date_format) + timedelta(days=1)).strftime(date_format)
            else:
                new_date = previous_new_date
            
            new_dates.append(new_date)
        df[0] = new_dates
        df.to_csv(csv_file_path, index=False, header=False)
        
        csv_file_path = r"temp.csv"
        df = pd.read_csv(csv_file_path,header = None)
        times = df[1].tolist()
        time_format = "%H:%M:%S"
        new_times = [start_time]

        for i in range(1, len(times)):
            previous_new_time = new_times[-1]
            if self.check_time_increase(times[i-1], times[i], time_format):
                previous_time = datetime.strptime(previous_new_time, time_format)
                interval = (datetime.strptime(times[i], time_format) - datetime.strptime(times[i-1], time_format))
                new_time = (previous_time + interval).strftime(time_format)
            else:

                new_time = previous_new_time
            
            new_times.append(new_time)

        df[1] = new_times

        new_file_name = str(df.iloc[0, 0]) + ".csv"
        df.to_csv(new_file_name, index=False, header=False)
        
        print(f"File with dd-mm-yy format saved: {new_file_name}")
        
        os.remove('temp.csv')
        print("Completed")
        msg_box = QMessageBox(self)
        self.center()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Message")
        msg_box.setText("<font color='green'>Convert Successful</font>")

        msg_box.setGeometry(800,500, 200, 100) 
        msg_box.exec()
            
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    
        
    def check_date_increase(self,previous_date_str, current_date_str, date_format="%d-%m-%y"):
        previous_date = datetime.strptime(previous_date_str, date_format)
        current_date = datetime.strptime(current_date_str, date_format)

        return (current_date - previous_date).days == 1
    
    def check_time_increase(self,previous_time_str, current_time_str, time_format="%H:%M:%S"):
        previous_time = datetime.strptime(previous_time_str, time_format)
        current_time = datetime.strptime(current_time_str, time_format)

        return current_time > previous_time
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    icon = QtGui.QIcon(r"C:\Users\snehs\Downloads\1322164.png")
    window.setWindowIcon(icon)
    window.show()
    window.center() 
    sys.exit(app.exec_())
