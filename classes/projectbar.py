from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

class ProjectBar(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.widget_layout = QHBoxLayout()
		self.setLayout(self.widget_layout)

		self.setStyleSheet("width: 500px;")

		label_title = QLabel("Kitica")
		label_title.setStyleSheet("font-size: 28px;")
		self.widget_layout.addWidget(label_title)

		label_location = QLabel("~/Documents/Projects/ProjectManager")
		label_location.setStyleSheet("font-size: 20px;")
		self.widget_layout.addWidget(label_location)

		button_open = QPushButton("Open")
		button_open.setStyleSheet("font-size: 18px; width: 75px; margin-left: auto")
		self.widget_layout.addWidget(button_open)

		button_delete = QPushButton("Delete")
		button_delete.setStyleSheet("font-size: 18px; width: 75px; margin-left: auto")
		self.widget_layout.addWidget(button_delete)