import subprocess as sb
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

def setClip():
	option1.setVisible(False)
	option2.setVisible(True)
	id=sb.run(["python3 smpl.py &"],shell=True)
	print("dihi")

def quitClip():
	option1.setVisible(True)
	option2.setVisible(False)
	k=sb.run(["ps ax | grep smpl.py"],shell=True)
	print(k[0])
	#k=sb.run(["kill -9 "+id],shell=True)


app = QApplication([])
app.setQuitOnLastWindowClosed(False)
  
# Adding an icon
icon = QIcon("icon.png")
  
# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
# Creating the options
menu = QMenu()
tray.setContextMenu(menu)
option1 = QAction("START"+"jhgf")
option2 = QAction("END")
#option2.setVisible(False)
option1.triggered.connect(setClip)
option1.triggered.connect(quitClip)
menu.addAction(option1)
menu.addAction(option2)


# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)
  
# Adding options to the System Tray

  
app.exec_()