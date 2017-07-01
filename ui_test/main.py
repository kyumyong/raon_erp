from PyQt5.QtWidgets import QApplication, QMainWindow
from test_20170624 import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.pushButton_ham.clicked.connect(self.onClick)

	def onClick(self):
		print("clicked!")

def main():
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
