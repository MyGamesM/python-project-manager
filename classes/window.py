from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QScrollArea, QVBoxLayout

from .projectbar import ProjectBar
from .sidewidget import SideWidget

class Window(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("Project Manager")

		resolution = QApplication.primaryScreen().geometry()
		screen_resolution = resolution.width(), resolution.height()

		self.setGeometry(
			QRect(
				int(screen_resolution[0] / 6),
				int(screen_resolution[1] / 6),
				int(screen_resolution[0] / 2),
				int(screen_resolution[1] / 2)
			)
		)

		self.initUI()

	def initUI(self) -> None:
		self.widget_layout = QGridLayout()
		self.setLayout(self.widget_layout)

		self.widget_layout.addWidget(SideWidget(), 1, 2)

		scroll_area = QScrollArea(self)
		self.widget_layout.addWidget(scroll_area, 1, 1)

		container_scroll = QWidget()
		widget_layout = QVBoxLayout()
		container_scroll.setLayout(widget_layout)

		for _ in range(100): widget_layout.addWidget(ProjectBar())
		scroll_area.setWidget(container_scroll)