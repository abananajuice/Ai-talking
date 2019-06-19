# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from talk_ui import *
from time import ctime


class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.textEdit.setPlainText("录音时长默认5s")
        self.pushButton.clicked.connect(self.ai)

    def ai(self):
        ping()  # 检查网络连接
        # a=input("输入")
        b = self.timeBox.value()
        LuYin(b)  # 录制音频
        a = baidu_speech_reco()  # 语音识别，返回文字结果
        self.textEdit.append("我\t{}:\n{}".format(ctime(), a))
        res = Tuling(a)  # 将结果发给图灵机器人
        print(res)  # 找到机器人的回答
        baidu_voice(res)  # 合成机器人的声音'''
        self.textEdit.append("机器人\t{}:\n{}".format(ctime(), res))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainwindow()
    win.show()
    sys.exit(app.exec_())
