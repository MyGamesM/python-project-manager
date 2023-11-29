from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class SideWidget(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.widget_layout = QVBoxLayout()
		self.setLayout(self.widget_layout)
		self.widget_layout.setSpacing(5)
		self.widget_layout.setContentsMargins(0, 0, 0, 0)
		self.setFixedHeight(150)

		button_create = QPushButton("Create new project")
		button_create.setStyleSheet("width: 150px; height: 75px; font-size: 18px;")
		self.widget_layout.addWidget(button_create)
		
		button_add = QPushButton("Add Project")
		button_add.setStyleSheet("width: 150px; height: 75px; font-size: 18px;")
		self.widget_layout.addWidget(button_add)