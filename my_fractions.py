# fractions_window.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import randint
from fractions import Fraction

class FractionsWindow(QDialog):
    def __init__(self):
        super(FractionsWindow, self).__init__()

        self.setWindowTitle('MathTutor')
        self.setGeometry(100, 100, 400, 200)

        self.current_fraction_1 = self.generate_fraction()
        self.current_fraction_2 = self.generate_fraction()
        self.current_operation = self.generate_operation()
        self.incorrect_attempts = 0  # Количество неправильных попыток

        layout = QVBoxLayout()

        self.label = QLabel('Решите дробь: {} {} {}'.format(self.format_fraction(self.current_fraction_1),
                                                            self.current_operation,
                                                            self.format_fraction(self.current_fraction_2)), self)
        self.label.setFont(QFont("Times New Roman", 14))

        self.answer_edit = QLineEdit(self)
        self.answer_edit.setFont(QFont("Times New Roman", 12))

        check_button = QPushButton('Проверить', self)
        check_button.clicked.connect(self.check_answer)
        check_button.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                border: 1px solid #2a82da;
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
            }

            QPushButton:hover {
                background-color: #1e5ea5;
                border: 1px solid #1e5ea5;
            }
        """)

        continue_button = QPushButton('Продолжить дальше', self)
        continue_button.clicked.connect(self.continue_next)
        continue_button.setEnabled(False)
        continue_button.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                border: 1px solid #2a82da;
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
            }

            QPushButton:hover {
                background-color: #1e5ea5;
                border: 1px solid #1e5ea5;
            }
        """)

        skip_button = QPushButton('Пропустить задание', self)
        skip_button.clicked.connect(self.skip_question)
        skip_button.setEnabled(False)
        skip_button.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                border: 1px solid #2a82da;
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
            }

            QPushButton:hover {
                background-color: #1e5ea5;
                border: 1px solid #1e5ea5;
            }
        """)

        layout.addWidget(self.label)
        layout.addWidget(self.answer_edit)
        layout.addWidget(check_button)
        layout.addWidget(continue_button)
        layout.addWidget(skip_button)

        self.setLayout(layout)

        # Добавлены атрибуты для доступа из main.py
        self.continue_button = continue_button
        self.skip_button = skip_button

    def generate_fraction(self):
        numerator = randint(1, 10)
        denominator = randint(1, 10)
        return Fraction(numerator, denominator)

    def generate_operation(self):
        operations = ['+', '-', '×', '÷']
        return operations[randint(0, 3)]

    def format_fraction(self, fraction):
        if fraction.denominator == 1:
            return str(fraction.numerator)
        elif fraction.numerator % fraction.denominator == 0:
            return str(fraction.numerator // fraction.denominator)
        else:
            return '{}/{}'.format(fraction.numerator, fraction.denominator)

    def check_answer(self):
        user_answer = self.answer_edit.text()
        try:
            user_fraction = Fraction(user_answer)
            if self.check_operation(user_fraction):
                self.label.setText('Правильно!')
                self.continue_button.setEnabled(True)
                self.skip_button.setEnabled(False)
                self.incorrect_attempts = 0
            else:
                self.label.setText('Неправильно. Пример: {} {} {}'.format(
                    self.format_fraction(self.current_fraction_1),
                    self.current_operation,
                    self.format_fraction(self.current_fraction_2)))
                self.incorrect_attempts += 1
                if self.incorrect_attempts == 2:
                    self.skip_button.setEnabled(True)
        except (ValueError, ZeroDivisionError):
            self.label.setText('Неправильный формат дроби или деление на ноль. Попробуйте ещё раз.')

    def check_operation(self, user_fraction):
        if self.current_operation == '+':
            expected_result = self.current_fraction_1 + self.current_fraction_2
        elif self.current_operation == '-':
            expected_result = self.current_fraction_1 - self.current_fraction_2
        elif self.current_operation == '×':
            expected_result = self.current_fraction_1 * self.current_fraction_2
        elif self.current_operation == '÷':
            expected_result = self.current_fraction_1 / self.current_fraction_2

        return user_fraction == expected_result

    def continue_next(self):
        self.current_fraction_1 = self.generate_fraction()
        self.current_fraction_2 = self.generate_fraction()
        self.current_operation = self.generate_operation()

        self.label.setText('Решите дробь: {} {} {}'.format(self.format_fraction(self.current_fraction_1),
                                                            self.current_operation,
                                                            self.format_fraction(self.current_fraction_2)))
        self.answer_edit.clear()
        self.continue_button.setEnabled(False)
        self.skip_button.setEnabled(False)  # После перехода к следующему вопросу отключаем кнопку "Пропустить задание"
        self.incorrect_attempts = 0  # Сбрасываем счетчик неправильных попыток

    def skip_question(self):
        self.current_fraction_1 = self.generate_fraction()
        self.current_fraction_2 = self.generate_fraction()
        self.current_operation = self.generate_operation()

        self.label.setText('Решите дробь: {} {} {}'.format(self.format_fraction(self.current_fraction_1),
                                                            self.current_operation,
                                                            self.format_fraction(self.current_fraction_2)))
        self.answer_edit.clear()
        self.continue_button.setEnabled(False)
        self.skip_button.setEnabled(False)  # После перехода к следующему вопросу отключаем кнопку "Пропустить задание"
        self.incorrect_attempts = 0  # Сбрасываем счетчик неправильных попыток
