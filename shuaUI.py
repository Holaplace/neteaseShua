# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shuaUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shuaUI(object):
    def setupUi(self, shuaUI):
        shuaUI.setObjectName("shuaUI")
        shuaUI.resize(705, 428)
        self.loadCookieBtn = QtWidgets.QPushButton(shuaUI)
        self.loadCookieBtn.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loadCookieBtn.setFont(font)
        self.loadCookieBtn.setObjectName("loadCookieBtn")
        self.cookieLable = QtWidgets.QLabel(shuaUI)
        self.cookieLable.setGeometry(QtCore.QRect(180, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.cookieLable.setFont(font)
        self.cookieLable.setObjectName("cookieLable")
        self.cookiePic = QtWidgets.QLabel(shuaUI)
        self.cookiePic.setGeometry(QtCore.QRect(130, 10, 31, 31))
        self.cookiePic.setText("")
        self.cookiePic.setPixmap(QtGui.QPixmap("1.png"))
        self.cookiePic.setScaledContents(True)
        self.cookiePic.setAlignment(QtCore.Qt.AlignCenter)
        self.cookiePic.setObjectName("cookiePic")
        self.loginBtn = QtWidgets.QPushButton(shuaUI)
        self.loginBtn.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginPic = QtWidgets.QLabel(shuaUI)
        self.loginPic.setGeometry(QtCore.QRect(130, 60, 31, 31))
        self.loginPic.setText("")
        self.loginPic.setPixmap(QtGui.QPixmap("1.png"))
        self.loginPic.setScaledContents(True)
        self.loginPic.setAlignment(QtCore.Qt.AlignCenter)
        self.loginPic.setObjectName("loginPic")
        self.introLable = QtWidgets.QLabel(shuaUI)
        self.introLable.setGeometry(QtCore.QRect(180, 60, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.introLable.setFont(font)
        self.introLable.setObjectName("introLable")
        self.playlistBtn = QtWidgets.QPushButton(shuaUI)
        self.playlistBtn.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.playlistBtn.setFont(font)
        self.playlistBtn.setObjectName("playlistBtn")
        self.playlistPic = QtWidgets.QLabel(shuaUI)
        self.playlistPic.setGeometry(QtCore.QRect(130, 110, 31, 31))
        self.playlistPic.setText("")
        self.playlistPic.setPixmap(QtGui.QPixmap("1.png"))
        self.playlistPic.setScaledContents(True)
        self.playlistPic.setAlignment(QtCore.Qt.AlignCenter)
        self.playlistPic.setObjectName("playlistPic")
        self.playlistEdit = QtWidgets.QLineEdit(shuaUI)
        self.playlistEdit.setGeometry(QtCore.QRect(180, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.playlistEdit.setFont(font)
        self.playlistEdit.setText("")
        self.playlistEdit.setObjectName("playlistEdit")
        self.lvLable = QtWidgets.QLabel(shuaUI)
        self.lvLable.setGeometry(QtCore.QRect(30, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lvLable.setFont(font)
        self.lvLable.setObjectName("lvLable")
        self.lvLcd = QtWidgets.QLCDNumber(shuaUI)
        self.lvLcd.setGeometry(QtCore.QRect(130, 320, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lvLcd.setFont(font)
        self.lvLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lvLcd.setSmallDecimalPoint(False)
        self.lvLcd.setDigitCount(2)
        self.lvLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lvLcd.setProperty("value", 0.0)
        self.lvLcd.setObjectName("lvLcd")
        self.numLable = QtWidgets.QLabel(shuaUI)
        self.numLable.setGeometry(QtCore.QRect(180, 320, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.numLable.setFont(font)
        self.numLable.setObjectName("numLable")
        self.numLcd = QtWidgets.QLCDNumber(shuaUI)
        self.numLcd.setGeometry(QtCore.QRect(270, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.numLcd.setFont(font)
        self.numLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numLcd.setSmallDecimalPoint(False)
        self.numLcd.setDigitCount(5)
        self.numLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.numLcd.setProperty("value", 0.0)
        self.numLcd.setObjectName("numLcd")
        self.playStatusLable = QtWidgets.QLabel(shuaUI)
        self.playStatusLable.setGeometry(QtCore.QRect(30, 270, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.playStatusLable.setFont(font)
        self.playStatusLable.setObjectName("playStatusLable")
        self.currentPlayLcd = QtWidgets.QLCDNumber(shuaUI)
        self.currentPlayLcd.setGeometry(QtCore.QRect(180, 270, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.currentPlayLcd.setFont(font)
        self.currentPlayLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentPlayLcd.setSmallDecimalPoint(False)
        self.currentPlayLcd.setDigitCount(3)
        self.currentPlayLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentPlayLcd.setProperty("value", 0.0)
        self.currentPlayLcd.setObjectName("currentPlayLcd")
        self.totalPlayLcd = QtWidgets.QLCDNumber(shuaUI)
        self.totalPlayLcd.setGeometry(QtCore.QRect(260, 270, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.totalPlayLcd.setFont(font)
        self.totalPlayLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.totalPlayLcd.setSmallDecimalPoint(False)
        self.totalPlayLcd.setDigitCount(3)
        self.totalPlayLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.totalPlayLcd.setProperty("value", 0.0)
        self.totalPlayLcd.setObjectName("totalPlayLcd")
        self.songLable = QtWidgets.QLabel(shuaUI)
        self.songLable.setGeometry(QtCore.QRect(30, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.songLable.setFont(font)
        self.songLable.setObjectName("songLable")
        self.songInfoLable = QtWidgets.QLabel(shuaUI)
        self.songInfoLable.setGeometry(QtCore.QRect(140, 180, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.songInfoLable.setFont(font)
        self.songInfoLable.setObjectName("songInfoLable")
        self.songStatusLable = QtWidgets.QLabel(shuaUI)
        self.songStatusLable.setGeometry(QtCore.QRect(30, 220, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.songStatusLable.setFont(font)
        self.songStatusLable.setObjectName("songStatusLable")
        self.totalSongTimeLcd = QtWidgets.QLCDNumber(shuaUI)
        self.totalSongTimeLcd.setGeometry(QtCore.QRect(260, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.totalSongTimeLcd.setFont(font)
        self.totalSongTimeLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.totalSongTimeLcd.setSmallDecimalPoint(False)
        self.totalSongTimeLcd.setDigitCount(3)
        self.totalSongTimeLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.totalSongTimeLcd.setProperty("value", 0.0)
        self.totalSongTimeLcd.setObjectName("totalSongTimeLcd")
        self.currentSongTimeLcd = QtWidgets.QLCDNumber(shuaUI)
        self.currentSongTimeLcd.setGeometry(QtCore.QRect(180, 220, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.currentSongTimeLcd.setFont(font)
        self.currentSongTimeLcd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentSongTimeLcd.setSmallDecimalPoint(False)
        self.currentSongTimeLcd.setDigitCount(3)
        self.currentSongTimeLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.currentSongTimeLcd.setProperty("value", 0.0)
        self.currentSongTimeLcd.setObjectName("currentSongTimeLcd")
        self.errorLable = QtWidgets.QLabel(shuaUI)
        self.errorLable.setGeometry(QtCore.QRect(30, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.errorLable.setFont(font)
        self.errorLable.setObjectName("errorLable")
        self.errorTextBrowser = QtWidgets.QTextBrowser(shuaUI)
        self.errorTextBrowser.setGeometry(QtCore.QRect(100, 380, 256, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.errorTextBrowser.setFont(font)
        self.errorTextBrowser.setObjectName("errorTextBrowser")

        self.retranslateUi(shuaUI)
        QtCore.QMetaObject.connectSlotsByName(shuaUI)

    def retranslateUi(self, shuaUI):
        _translate = QtCore.QCoreApplication.translate
        shuaUI.setWindowTitle(_translate("shuaUI", "刷云"))
        self.loadCookieBtn.setText(_translate("shuaUI", "Load Cookie"))
        self.cookieLable.setText(_translate("shuaUI", "Cookie Address"))
        self.loginBtn.setText(_translate("shuaUI", "Log In"))
        self.introLable.setText(_translate("shuaUI", "Your Name"))
        self.playlistBtn.setText(_translate("shuaUI", "Playlist ID"))
        self.lvLable.setText(_translate("shuaUI", "Current Lv.:"))
        self.numLable.setText(_translate("shuaUI", "Still require:                           to next level"))
        self.playStatusLable.setText(_translate("shuaUI", "Current playlist status:               with"))
        self.songLable.setText(_translate("shuaUI", "Current song:"))
        self.songInfoLable.setText(_translate("shuaUI", "Name <-> Author(s)"))
        self.songStatusLable.setText(_translate("shuaUI", "Current song status:                   with                second(s)"))
        self.errorLable.setText(_translate("shuaUI", "Error Bar"))
