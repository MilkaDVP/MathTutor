# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPalette, QColor

from my_fractions import FractionsWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('MathTutor')

        # Загрузка UI из файла start.ui
        loadUi('start.ui', self)

        # Привязка действия к кнопке "ДРОБИ"
        self.fractions.clicked.connect(self.show_fractions_window)

        # Применение темной темы
        self.apply_dark_theme()

        self.show()

    def show_fractions_window(self):
        fractions_window = FractionsWindow()
        fractions_window.exec_()

    def apply_dark_theme(self):
        # Установка стиля "Fusion" глобально для всего приложения
        QApplication.setStyle("Fusion")

        # Настройка цветовой схемы для темной темы
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        # Установка цветовой схемы глобально для всего приложения
        QApplication.setPalette(dark_palette)

        # Установка стилей для кнопок
        self.setStyleSheet(
            """
            QPushButton {
                color: white;
                background-color: #2a82da;
                border: 1px solid #2a82da;
                padding: 5px 10px;
                border-radius: 5px;
            }

            QPushButton:disabled {
                background-color: #7f7f7f;
                border: 1px solid #7f7f7f;
            }
            """
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    sys.exit(app.exec_())
