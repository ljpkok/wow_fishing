from ui import ScreenShotCoordinateView
from ui import FunctionalView
import FishingHelper
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTextBrowser
from PySide6.QtCore import QSize
import FishingThread
import LogFetcherThread
from PySide6 import QtWidgets

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.init_child_widget()
        self.init_log_fetch_thread()

    def init_child_widget(self):
        self.screeshot_view = ScreenShotCoordinateView.ScreenShotCoordinateView(self)
        self.functional_view = FunctionalView.FunctionalView(self)

        self.start_button = QPushButton("开始钓鱼")
        self.start_button.setCheckable(True)
        self.start_button.clicked.connect(self.start_fishing)

        self.stop_button = QPushButton("停止")
        self.stop_button.setCheckable(True)
        self.stop_button.clicked.connect(self.stop_fishing)
        self.stop_button.setEnabled(False)

        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        self.g_layout.addWidget(self.screeshot_view, 0, 0)
        self.g_layout.addWidget(self.functional_view, 0, 1)
        self.g_layout.addWidget(self.start_button, 1, 0)
        self.g_layout.addWidget(self.stop_button, 1, 1)

        self.log_browser = QTextBrowser()
        self.g_layout.addWidget(self.log_browser, 2, 0, 1, 4)

    def start_fishing(self):
        functional_config = self.functional_view.get_all_config_data()
        capture_area_coordinate = self.screeshot_view.get_capture_coordinate()
        self.fishing_helper = FishingHelper.FishingHelper(functional_config, capture_area_coordinate)
        self.fish_thread = FishingThread.FishingThread(self.fishing_helper, self)
        self.fish_thread.start()
        self.start_button.setText("钓鱼中")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_fishing(self):
        if self.fish_thread.isRunning():
            self.fish_thread.terminate()
            self.stop_button.setText("停止中...")
            self.stop_button.setEnabled(False)
            self.fish_thread.wait()
            self.stop_button.setText("停止")
            self.start_button.setText("开始钓鱼")
            self.start_button.setEnabled(True)

    def reset_fishing_button(self):
        self.stop_button.setText("停止")
        self.stop_button.setEnabled(False)
        self.start_button.setText("开始钓鱼")
        self.start_button.setEnabled(True)

    def resize_and_show(self):
        self.setWindowTitle("小蒋人钓鱼Bot")
        self.show()
        self.setFixedSize(QSize(600, 400))

    def init_log_fetch_thread(self):
        self.log_fetch_thread = LogFetcherThread.LogFetcherThread(self)
        self.log_fetch_thread.start()

    def append_text(self, text):
        if text is not None:
            self.log_browser.append(text)

    def closeEvent(self, e):
        self.log_fetch_thread.terminate()

    #def moveEvent(self, e):
    #    old_screen = QtWidgets.QApplication.screenAt(e.oldPos())
    #    new_screen = QtWidgets.QApplication.screenAt(e.pos())
    #    if old_screen != new_screen:
    #        print(old_screen, new_screen)
    #    return super().moveEvent(e)