import sys
from PyQt5.QtWidgets import QApplication
from interface.window import JSMinifierApp

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = JSMinifierApp()
  window.show()
  sys.exit(app.exec_())