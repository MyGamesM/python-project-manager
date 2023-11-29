import os, sys

from classes.window import Window
from PyQt6.QtWidgets import QApplication

os.system("cls")

# hide files
# import subprocess
# subprocess.run(["attrib","+H","myfile.txt"],check=True)

class ProjectManager:
	def __init__(self) -> None:
		self.app = QApplication([])
		self.app.setStyleSheet("""
			* { color: #eee; }
			QWidget { background-color: #3e3e3e; }
		""")
		self.window = Window()
		self.window.show()
		sys.exit(self.app.exec())

if __name__ == "__main__":
	project_manager = ProjectManager()