from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
# import matplotlib.pyplot as plt
# from picamera import PiCamera
# from picamera.array import PiRGBArray
import logging
from time import sleep
from os import getcwd,listdir

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 895)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Scanner = QtWidgets.QTabWidget(self.centralwidget)
        self.Scanner.setGeometry(QtCore.QRect(0, 0, 1101, 871))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(93, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        
        self.Scanner.setPalette(palette)
        self.Scanner.setObjectName("Scanner")
        self.scanner = QtWidgets.QWidget()
        self.scanner.setObjectName("scanner")
        
        self.MainLivefeed = QtWidgets.QLabel(self.scanner)
        self.MainLivefeed.setGeometry(QtCore.QRect(40, 120, 471, 441))
        self.MainLivefeed.setObjectName("MainLivefeed")
        self.MainLivefeed.setAutoFillBackground(True)
        self.MainLivefeed.setFrameShape(QtWidgets.QFrame.Box)
        self.MainLivefeed.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid black;")
        
        self.MainProcessed = QtWidgets.QLabel(self.scanner)
        self.MainProcessed.setGeometry(QtCore.QRect(590, 120, 471, 441))
        self.MainProcessed.setObjectName("MainProcessed")
        self.MainProcessed.setAutoFillBackground(True)
        self.MainProcessed.setFrameShape(QtWidgets.QFrame.Box)
        self.MainProcessed.setStyleSheet("background-color: rgb(255, 255, 255); border: 2px solid black;")
        
        self.Exit = QtWidgets.QPushButton(self.scanner)
        self.Exit.setGeometry(QtCore.QRect(960, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit.setAutoFillBackground(False)
        self.Exit.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Exit.setObjectName("Exit")

        self.CapInst = QtWidgets.QPushButton(self.scanner)
        self.CapInst.setGeometry(QtCore.QRect(470+170, 690, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.CapInst.setFont(font)
        self.CapInst.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CapInst.setAutoFillBackground(False)
        self.CapInst.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.CapInst.setObjectName("CapInst")
        
        self.Mode = QtWidgets.QPushButton(self.scanner)
        self.Mode.setGeometry(QtCore.QRect(40, 30, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Mode.setFont(font)
        self.Mode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mode.setAutoFillBackground(False)
        self.Mode.setStyleSheet("background-color: rgb(203, 255, 238);")
        self.Mode.setObjectName("Mode")
        
        self.Process = QtWidgets.QPushButton(self.scanner)
        self.Process.setGeometry(QtCore.QRect(470, 690, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Process.setFont(font)
        self.Process.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Process.setAutoFillBackground(True)
        self.Process.setObjectName("Process")
        
        self.Stop = QtWidgets.QPushButton(self.scanner)
        self.Stop.setGeometry(QtCore.QRect(760, 690, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Stop.setFont(font)
        self.Stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Stop.setAutoFillBackground(True)
        self.Stop.setObjectName("Stop")
        
        self.Start = QtWidgets.QPushButton(self.scanner)
        self.Start.setGeometry(QtCore.QRect(180, 690, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Start.setFont(font)
        self.Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start.setAutoFillBackground(True)
        self.Start.setObjectName("Start")
        
        self.Result = QtWidgets.QLabel(self.scanner)
        self.Result.setGeometry(QtCore.QRect(480, 40, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Result.setFont(font)
        self.Result.setAutoFillBackground(False)
        self.Result.setStyleSheet("background-color: rgb(153, 255, 235);\n"
"border-color: rgb(0, 0, 0);")
        self.Result.setFrameShape(QtWidgets.QFrame.Box)
        self.Result.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Result.setLineWidth(3)
        self.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.Result.setObjectName("Result")
        
        self.Deflection = QtWidgets.QLabel(self.scanner)
        self.Deflection.setGeometry(QtCore.QRect(380, 580, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Deflection.setFont(font)
        self.Deflection.setAutoFillBackground(False)
        self.Deflection.setStyleSheet("background-color: rgb(153, 255, 235);\n"
"border-color: rgb(0, 0, 0);")
        self.Deflection.setFrameShape(QtWidgets.QFrame.Box)
        self.Deflection.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Deflection.setLineWidth(3)
        self.Deflection.setAlignment(QtCore.Qt.AlignCenter)
        self.Deflection.setObjectName("Deflection")
        
        self.Scanner.addTab(self.scanner, "")
        self.train = QtWidgets.QWidget()
        self.train.setObjectName("train")
        
        self.livefeed = QtWidgets.QLabel(self.train)
        self.livefeed.setGeometry(QtCore.QRect(30, 180, 471, 441))
        self.livefeed.setObjectName("livefeed")
        self.livefeed.setAutoFillBackground(True)
        self.livefeed.setFrameShape(QtWidgets.QFrame.Box)
        self.livefeed.setStyleSheet("border: 2px solid black; background-color: rgb(255, 255, 255);")
        
        self.processed = QtWidgets.QLabel(self.train)
        self.processed.setGeometry(QtCore.QRect(590, 180, 471, 441))
        self.processed.setObjectName("processed")
        self.processed.setAutoFillBackground(True)
        self.processed.setFrameShape(QtWidgets.QFrame.Box)
        self.processed.setStyleSheet("border: 2px solid black; background-color: rgb(255, 255, 255);")

        self.RedSlider = QtWidgets.QSlider(self.train)
        self.RedSlider.setGeometry(QtCore.QRect(50, 110, 251, 61))
        self.RedSlider.setAutoFillBackground(True)
        self.RedSlider.setStyleSheet("border: 1px solid black;")
        self.RedSlider.setMaximum(255)
        self.RedSlider.setSingleStep(5)
        self.RedSlider.setPageStep(5)
        self.RedSlider.setProperty("value", 30)
        self.RedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.RedSlider.setObjectName("RedSlider")
        
        self.GreenSlider = QtWidgets.QSlider(self.train)
        self.GreenSlider.setGeometry(QtCore.QRect(340, 110, 251, 61))
        self.GreenSlider.setAutoFillBackground(True)
        self.GreenSlider.setStyleSheet("border: 1px solid black;")
        self.GreenSlider.setMaximum(255)
        self.GreenSlider.setSingleStep(5)
        self.GreenSlider.setPageStep(5)
        self.GreenSlider.setProperty("value", 30)
        self.GreenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GreenSlider.setObjectName("GreenSlider")
        
        self.BlueSlider = QtWidgets.QSlider(self.train)
        self.BlueSlider.setGeometry(QtCore.QRect(630, 110, 251, 61))
        self.BlueSlider.setAutoFillBackground(True)
        self.BlueSlider.setStyleSheet("border: 1px solid black;")
        self.BlueSlider.setMaximum(255)
        self.BlueSlider.setSingleStep(5)
        self.BlueSlider.setPageStep(5)
        self.BlueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BlueSlider.setObjectName("BlueSlider")
        
        self.redlabel = QtWidgets.QLabel(self.train)
        self.redlabel.setGeometry(QtCore.QRect(115, 80, 126, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.redlabel.setFont(font)
        self.redlabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.redlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.redlabel.setObjectName("redlabel")
        
        self.greenlabel = QtWidgets.QLabel(self.train)
        self.greenlabel.setGeometry(QtCore.QRect(400, 80, 140, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.greenlabel.setFont(font)
        self.greenlabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.greenlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.greenlabel.setObjectName("greenlabel")
        
        self.bluelabel = QtWidgets.QLabel(self.train)
        self.bluelabel.setGeometry(QtCore.QRect(695, 80, 126, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.bluelabel.setFont(font)
        self.bluelabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.bluelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bluelabel.setObjectName("bluelabel")
        
        self.capture = QtWidgets.QPushButton(self.train)
        self.capture.setGeometry(QtCore.QRect(50, 760, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.capture.setFont(font)
        self.capture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.capture.setAutoFillBackground(True)
        self.capture.setObjectName("capture")
        
        self.selectROI = QtWidgets.QPushButton(self.train)
        self.selectROI.setGeometry(QtCore.QRect(270, 760, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.selectROI.setFont(font)
        self.selectROI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectROI.setAutoFillBackground(True)
        self.selectROI.setObjectName("selectROI")
        
        self.SaveTemplate = QtWidgets.QPushButton(self.train)
        self.SaveTemplate.setGeometry(QtCore.QRect(910, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.SaveTemplate.setFont(font)
        self.SaveTemplate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveTemplate.setAutoFillBackground(False)
        self.SaveTemplate.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.SaveTemplate.setObjectName("SaveTemplate")
        
        self.TemplateStatus = QtWidgets.QLabel(self.train)
        self.TemplateStatus.setGeometry(QtCore.QRect(660, 630, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.TemplateStatus.setFont(font)
        self.TemplateStatus.setAutoFillBackground(False)
        self.TemplateStatus.setStyleSheet("background-color: rgb(199, 255, 226);")
        self.TemplateStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.TemplateStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.TemplateStatus.setWordWrap(True)
        self.TemplateStatus.setObjectName("TemplateStatus")
        
        self.seperationlabel = QtWidgets.QLabel(self.train)
        self.seperationlabel.setGeometry(QtCore.QRect(60, 630, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.seperationlabel.setFont(font)
        self.seperationlabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.seperationlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.seperationlabel.setObjectName("seperationlabel")
        
        self.seperation = QtWidgets.QSlider(self.train)
        self.seperation.setGeometry(QtCore.QRect(30, 660, 251, 61))
        self.seperation.setStyleSheet("border: 1px solid black;")
        self.seperation.setAutoFillBackground(True)
        self.seperation.setMaximum(22)
        self.seperation.setSingleStep(1)
        self.seperation.setPageStep(1)
        self.seperation.setProperty("value", 9)
        self.seperation.setOrientation(QtCore.Qt.Horizontal)
        self.seperation.setObjectName("seperation")
        
        self.Scanner.addTab(self.train, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Set the default values for the GUI
        self.retranslateUi(MainWindow)
        self.Scanner.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect Buttons to functions
        self.Exit.clicked.connect(self.exit)
        self.Start.clicked.connect(self.start)
        self.Stop.clicked.connect(self.stop_cam)
        self.Process.clicked.connect(self.start_process)
        self.Mode.clicked.connect(self.modemsgbtn)
        self.capture.clicked.connect(self.captureimage)
        self.selectROI.clicked.connect(self.selectroi)
        self.SaveTemplate.clicked.connect(self.savetemplate)
        self.seperation.valueChanged.connect(self.seperationvalue)
        self.RedSlider.valueChanged.connect(self.redvalue)
        self.GreenSlider.valueChanged.connect(self.greenvalue)
        self.BlueSlider.valueChanged.connect(self.bluevalue)
        self.CapInst.clicked.connect(self.capInstance)

        # set default variables
        self.current_mode = 0
        self.seperation = 9
        self.redThres = 45
        self.greenThres = 45
        self.blueThres = 0
        self.template = None
        self.templateROI = None
        self.stop = None
        self.cap = None
        self.process = None
        self.pixelCount = None
        self.centroid = None

        logging.basicConfig(filename='jmScanner.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

        try:
            self.cap = PiCamera()
            self.cap.resolution = (2048,2048)
            self.cap.framerate = 24
            sleep(1)
        except Exception as e:
            logging.error(e)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Camera not found!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.CapInst.setText(_translate("MainWindow","Store"))
        self.Mode.setText(_translate("MainWindow", "Mode- Automatic"))
        self.Process.setText(_translate("MainWindow", "Process"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.Result.setText(_translate("MainWindow", "Result!"))
        self.Deflection.setText(_translate("MainWindow", "Deflection - 0 px."))
        self.Scanner.setTabText(self.Scanner.indexOf(self.scanner), _translate("MainWindow", "Scanner"))
        self.redlabel.setText(_translate("MainWindow", "Red Threshold"))
        self.greenlabel.setText(_translate("MainWindow", "Green Threshold"))
        self.bluelabel.setText(_translate("MainWindow", "Blue Threshold"))
        self.capture.setText(_translate("MainWindow", "Capture"))
        self.selectROI.setText(_translate("MainWindow", "Select ROI"))
        self.SaveTemplate.setText(_translate("MainWindow", "Save Template"))
        self.TemplateStatus.setText(_translate("MainWindow", "Please set the template!"))
        self.seperationlabel.setText(_translate("MainWindow", "Seperation"))
        self.Scanner.setTabText(self.Scanner.indexOf(self.train), _translate("MainWindow", "Train"))

    def exit(self):
        sys.exit()

    def capInstance(self):
        pwd = getcwd()
        cv2.imwrite(str(len(listdir(pwd))+1)+'.jpg',self.templateROI)
        return

    def start(self):
        if self.roi is None:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Please set the template first and try again!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            if self.cap is None:
                try:
                    self.cap = cv2.imread('right1.png') #PiCamera()
                    self.cap.resolution = (2048, 2048)
                    self.cap.framerate = 24
                    sleep(1)
                except Exception as e:
                    logging.error(e)
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Camera not found!")
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
            try:
                while True:
                    image = np.empty((2048,2048,3),dtype=np.uint8)
                    self.cap.capture(image,'bgr',use_video_port=True)
                    image = cv2.resize(image, (550,550))
                    self.displayFrame(image,self.MainLivefeed)
                    QtWidgets.QApplication.processEvents()
                    if self.stop == True:
                        self.cap.close()
                        self.cap = None
                        self.MainLivefeed.setAutoFillBackground(True)
                        self.MainProcessed.setAutoFillBackground(True)
                        QtWidgets.QApplication.processEvents()
                        break
                    if self.process == True:
                        self.process = False
                        self.templateROI = image[int(self.roi[1]):int(self.roi[1]+self.roi[3]), int(self.roi[0]):int(self.roi[0]+self.roi[2])]
                        _, pixelCount, self.ROI, cnt = self.process_image_area_method(self.templateROI)
                        # count = 0
                        # for ct in cnt:
                        #     if cv2.contourArea(ct) > 200:
                        #         count += 1
                        if pixelCount >= self.pixelCount+300 or pixelCount <= self.pixelCount-300:
                            self.Result.setText("Failed!")
                            self.Result.setStyleSheet("background-color: red")
                            self.Deflection.setText("Deflection - {} px.".format(abs(self.pixelCount-pixelCount)))
                            QtWidgets.QApplication.processEvents()
                        else:
                            for ct in cnt:
                                x,y,w,h = cv2.boundingRect(ct)
                                cx,cy = x+w//2, y+h//2
                                if cx>=self.centroid[0]+50 or cx<=self.centroid[0]-50 or cy>=self.centroid[1]+50 or cy<=self.centroid[1]-50:
                                    cv2.circle(self.ROI, (self.centroid[0], self.centroid[1]), 5, (0,0,255), -1)
                                    self.Result.setText("Pass")
                                    self.Result.setStyleSheet("background-color: yellow")
                                    self.Deflection.setText("No Deflection!")
                                    QtWidgets.QApplication.processEvents()
                                else:
                                    self.Result.setText("Failed")
                                    self.Result.setStyleSheet("background-color: green")
                                    self.Deflection.setText("Deflection - {} px.".format(abs(self.pixelCount)))
                                    QtWidgets.QApplication.processEvents()
                        self.displayFrame(self.ROI, self.MainProcessed)
                        QtWidgets.QApplication.processEvents()
            except Exception as e:
                logging.error(e)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Something went wrong!")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        return
    
    def stop_cam(self):
        self.stop = True
        return
    
    def start_process(self):
        self.process = True
        return
    
    def current_mode_selection(self,i):
        self.msg._exec()
        if i.text() == "OK":
            if self.current_mode == 0:
                self.current_mode = 1
                self.Mode.setText("Mode- Manual")
            else:
                self.current_mode = 0
                self.Mode.setText("Mode- Automatic")
        return

    def modemsgbtn(self):
        # message box
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Alert)
        self.msg.setText("Do you want to change the mode?")
        self.msg.setWindowTitle("Warning!")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.current_mode_selection)
        self.msg = None

    def captureimage(self):  
        if self.template is None:
            if self.cap is None:
                try:
                    self.cap = PiCamera()
                    self.cap.resolution = (2048,2048)
                    self.cap.framerate = 24
                    sleep(1)
                except Exception as e:
                    logging.error(e)
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Camera not found!")
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
            # message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please clean the surface and press OK!")
            msg.setWindowTitle("Information!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            image = np.empty((2048,2048,3),dtype=np.uint8)
            self.cap.capture(image,'bgr',use_video_port=True)
            self.template = cv2.resize(image, (550,550))
            self.displayFrame(self.template, self.livefeed)
            QtWidgets.QApplication.processEvents()
            self.TemplateStatus.setText("Image captured!"+"\n Please select ROI!")
        else:
            # message box
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Critical)
            self.msg.setText("Do you want to overwrite the existing Template?")
            self.msg.setWindowTitle("Warning!")
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            self.msg.buttonClicked.connect(self.capturemsgbtn)
            self.msg = None
        return

    def capturemsgbtn(self, i):
        self.msg._exec()
        if i.text() == "OK":
            self.template = None
            self.captureimage()
        else:
            return

    def selectroi(self):
        try:
            if self.template is None:
                # message box
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Please capture the image first!")
                msg.setWindowTitle("Warning!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
            if self.template is not None:
                if self.templateROI is not None:
                    # message box
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setIcon(QtWidgets.QMessageBox.Critical)
                    self.msg.setText("Do you want to overwrite the existing ROI?")
                    self.msg.setWindowTitle("Warning!")
                    self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    self.msg.buttonClicked.connect(self.selectroimsgbtn)
                    self.msg = None

                if self.templateROI is None:
                    self.roi = cv2.selectROI("Select the ROI!", self.template)
                    cv2.destroyAllWindows()
                    self.templateROI = self.template[int(self.roi[1]):int(self.roi[1]+self.roi[3]), int(self.roi[0]):int(self.roi[0]+self.roi[2])]
                    # self.ROI = self.template[int(self.templateROI[1]):int(self.templateROI[1]+self.templateROI[3]), 
                    #                 int(self.templateROI[0]):int(self.templateROI[0]+self.templateROI[2]), :]
                    _, self.pixelCount, self.ROI, cnt = self.process_image_area_method(self.templateROI)
                    count = 0
                    for ct in cnt:
                        if cv2.contourArea(ct) > 2000:
                            count+=1
                    if count==1:
                        for ct in cnt:
                            x,y,w,h = cv2.boundingRect(ct)
                            cx,cy = x+w//2, y+h//2
                            self.centroid = [cx,cy]
                        cv2.circle(self.ROI, (self.centroid[0], self.centroid[0]), 1, (0,0,255), -1)
                        cv2.circle(self.ROI, (self.centroid[0]+50, self.centroid[0]+50), 1, (0,0,255), -1)
                        cv2.circle(self.ROI, (self.centroid[0]-50, self.centroid[0]-50), 1, (0,0,255), -1)
                        self.displayFrame(self.ROI, self.processed)
                        QtWidgets.QApplication.processEvents()
                        self.TemplateStatus.setText("ROI selected!"+"\n Pixel count:"+str(self.pixelCount))
                        self.Deflection.setText("Target - {} px.".format(abs(self.pixelCount)))
                    else:
                        # message box
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Alert)
                        msg.setText("Incorrect template!"+"\n multiple objects detected!")
                        msg.setWindowTitle("Warning!")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.exec_()
                        self.template = None
                        self.templateROI = None
                        self.ROI = None
                        self.TemplateStatus.setText("Please capture the image again!")

        except Exception as e:
            # logging.error(e)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Something went wrong!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        return

    def process_image(self,frame):
        frame = frame
        frame[frame[:,:,0]] = 0
        frame[frame[:,:,1] < 45] = 0
        frame[frame[:,:,2] < 45] = 0

        thres, binary = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)
        gray = cv2.cvtColor(binary, cv2.COLOR_RGB2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        erode = cv2.erode(gray, kernel, iterations=self.seperation)
        cnt, hierarchy = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        erode = cv2.cvtColor(erode, cv2.COLOR_GRAY2BGR)
        erode = cv2.drawContours(erode, cnt, -1, (0, 255, 0), 2)
        return frame, cnt, erode

    def process_image_area_method(self,frame):
        frame = frame
        frame[:,:,0] = 0
        frame[frame[:,:,1] < 45] = 0
        frame[frame[:,:,2] < 45] = 0
        thres, binary = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)
        gray = cv2.cvtColor(binary, cv2.COLOR_BGR2GRAY)
        count = np.sum(gray > 170)
        cnt, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        bgr = cv2.drawContours(gray, cnt, -1, (0, 255, 0), 2)
        return frame, count, bgr, cnt

    def selectroimsgbtn(self, i):
        self.msg._exec()
        if i.text() == "OK":
            self.templateROI = None
            self.selectroi()
            return
        else:
            return

    def savetemplate(self):
        cv2.imwrite("template.png", self.template)
        np.save("templateROI.npy", self.templateROI)
        self.TemplateStatus.setText("Template Saved!"+"\n Go for scanning!")
        return

    def seperationvalue(self):
        if self.templateROI is None:
            # message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please select the ROI first!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        else:
            try:
                self.seperation = int(float(self.seperationSlider.value()))
            except Exception as e:
                logging.error(e)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Something went wrong!")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        return

    def redvalue(self):
        if self.templateROI is None:
            # message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please select the ROI first!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        else:
            try:
                self.redThres = int(float(self.RedSlider.value()))
            except Exception as e:
                logging.error(e)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Something went wrong!")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
    
    def greenvalue(self):
        if self.templateROI is None:
            # message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please select the ROI first!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        else:
            try:
                self.greenThres = int(float(self.GreenSlider.value()))
            except Exception as e:
                logging.error(e)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Something went wrong!")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        return

    def bluevalue(self):
        if self.templateROI is None:
            # message box
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please select the ROI first!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        else:
            try:
                self.blueThres = int(float(self.BlueSlider.value()))
            except Exception as e:
                logging.error(e)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Something went wrong!")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        return

    def displayFrame(self,frame,window):
        try:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            step = channel * width
            qformat = QtGui.QImage.Format_RGB888
            img = QtGui.QImage(frame.data, width, height, step, qformat)
            img = img.scaled(window.width(), window.height())
            window.setPixmap(QtGui.QPixmap.fromImage(img))
        except Exception as e:
            # logging.error(e)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Something went wrong!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
