from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from NatNetClient import NatNetClient

import sys

class WidgetGallery(QDialog):

    serverIpAddress = "172.29.37.169"
    serverPort = "1511"

    targetIpAddress = "172.29.37.169"
    targetPort = "1612"

    multicastAddress = "172.29.37.169"

    streamStatus = False
    interceptStatus = False

    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("PS19 Client")

        self.initStreamingClient()

    def initStreamingClient(self):

        # This will create a new NatNet client
        self.streamingClient = NatNetClient()

        # Set specs
        self.streamingClient.setServerIpAndPort(self.serverIpAddress, self.serverPort)
        self.streamingClient.setTargetIpAndPort(self.targetIpAddress, self.targetPort)
        self.streamingClient.setMulticastAddress(self.multicastAddress)

        # Start up the streaming client now that the callbacks are set up.
        # This will run perpetually, and operate on a separate thread.
        # streamingClient.run()

        self.streamingClient.setStreamConnectionListener(self.onStreamConnectionChanged)
        self.streamingClient.setStreamInterceptListener(self.onInterceptionChanged)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Stream")

        serverIpLabel = QLabel("Server IP")
        serverPortLabel = QLabel("Server Port")
        multicastLabel = QLabel("Multicast Addr")

        serverIpLineEdit = QLineEdit(self.serverIpAddress)
        serverPortLineEdit = QLineEdit(self.serverPort)
        multicastLineEdit = QLineEdit(self.multicastAddress)

        streamStatusLabel = QLabel("Status")

        self.radioButtonStreamConnected = QRadioButton("Connected")
        self.radioButtonStreamDisconnected = QRadioButton("Disconnected")
        self.radioButtonStreamConnected.setEnabled(False)
        self.radioButtonStreamDisconnected.setEnabled(False)
        self.radioButtonStreamDisconnected.setChecked(True)

        toggleStreamButton = QPushButton("Toggle Stream")
        toggleStreamButton.clicked.connect(self.toggleStream)
        toggleStreamButton.setCheckable(True)
        toggleStreamButton.setChecked(False)

        layout = QGridLayout()

        layout.addWidget(serverIpLabel, 0, 0, 1, 1)
        layout.addWidget(serverIpLineEdit, 0, 1, 1, 1)
        layout.addWidget(serverPortLabel, 1, 0, 1, 1)
        layout.addWidget(serverPortLineEdit, 1, 1, 1, 1)

        layout.addWidget(multicastLabel, 2, 0, 1, 1)
        layout.addWidget(multicastLineEdit, 2, 1, 1, 1)

        layout.addWidget(streamStatusLabel, 3, 0, 2, 1)
        layout.addWidget(self.radioButtonStreamConnected, 3, 1, 1, 1)
        layout.addWidget(self.radioButtonStreamDisconnected, 4, 1, 1, 1)
        layout.addWidget(toggleStreamButton, 5, 0, 1, 2)

        layout.setRowStretch(6, 1)

        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Intercept")

        targetIpLabel = QLabel("Target IP")
        targetPortLabel = QLabel("Target Port")

        targetIpLineEdit = QLineEdit(self.targetIpAddress)
        targetPortLineEdit = QLineEdit(self.targetPort)

        interceptStatusLabel = QLabel("Status")

        self.radioButtonInterceptEnabled = QRadioButton("Enabled")
        self.radioButtonInterceptDisabled = QRadioButton("Disabld")
        self.radioButtonInterceptEnabled.setEnabled(False)
        self.radioButtonInterceptDisabled.setEnabled(False)
        self.radioButtonInterceptDisabled.setChecked(True)

        toggleInterception = QPushButton("Toggle Intercept")
        toggleInterception.clicked.connect(self.toggleIntercept)
        toggleInterception.setCheckable(True)
        toggleInterception.setChecked(False)

        layout = QGridLayout()

        layout.addWidget(targetIpLabel, 0, 0, 1, 1)
        layout.addWidget(targetIpLineEdit, 0, 1, 1, 1)
        layout.addWidget(targetPortLabel, 1, 0, 1, 1)
        layout.addWidget(targetPortLineEdit, 1, 1, 1, 1)

        layout.addWidget(interceptStatusLabel, 2, 0, 2, 1)

        layout.addWidget(self.radioButtonInterceptEnabled, 2, 1, 1, 1)
        layout.addWidget(self.radioButtonInterceptDisabled, 3, 1, 1, 1)

        layout.addWidget(toggleInterception, 5, 0, 1, 2)
        layout.setRowStretch(6, 1)

        self.topRightGroupBox.setLayout(layout)

    def onStreamConnectionChanged(self, status):
        if status == True:
            self.radioButtonStreamConnected.setChecked(True)
            self.radioButtonStreamDisconnected.setChecked(False)
        else:
            self.radioButtonStreamConnected.setChecked(False)
            self.radioButtonStreamDisconnected.setChecked(True)

    def onInterceptionChanged(self, status):

        if status == True:
            self.radioButtonInterceptEnabled.setChecked(True)
            self.radioButtonInterceptDisabled.setChecked(False)
        else:
            self.radioButtonInterceptEnabled.setChecked(False)
            self.radioButtonInterceptDisabled.setChecked(True)

    def toggleStream(self):
        self.streamStatus^=True
        print(self.streamStatus)
        # Start client
        if self.streamStatus == True:
            self.onStreamConnectionChanged(True)
            self.streamingClient.run()

        # Stop client
        else:
            self.onStreamConnectionChanged(False)
            #self.streamingClient.stop()

    def toggleIntercept(self, status):
        self.interceptStatus^=True

        if(self.interceptStatus==True):
            self.streamingClient.setInterceptStatus(True)



if __name__ == '__main__':

    app = QApplication([])
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())










