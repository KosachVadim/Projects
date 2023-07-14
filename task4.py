# This Python file uses the following encoding: UTF-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

from EDS import EDS, EDS_WORD, EDS_Formula_Word
from util import read_text, open_keyb, open_keya, name_choise, message_RSA_text, get_prime_number_forword, \
    numbers_to_string, message_EDS
from RSA import RSA_Formula_Word, RSA_word


class Window_4(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('EDS(word)')
        self.setFixedSize(700, 850)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout(self)
        page_text.setLayout(layout)
        self.text = QTextBrowser(self)
        self.text.setHtml(f"<font style='font-family: Arial; font-size: 12pt;'>{read_text('Theory_EDS.txt')}")
        layout.addRow(self.text)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout(self)
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel('Шифрование и расшифрование EDS по алгоритму RSA'))
        layout_ex.addRow(QLabel('Введите значения:'))
        self.inp_ex_p1 = QLineEdit()
        self.inp_ex_p2 = QLineEdit()
        self.inp_ex_q1 = QLineEdit()
        self.inp_ex_q2 = QLineEdit()
        self.inp_ex_oA = QLineEdit()
        self.inp_ex_oB = QLineEdit()
        self.inp_ex_m = QLineEdit()
        self.inp_ex_p1.setPlaceholderText("p1")
        self.inp_ex_p2.setPlaceholderText("p2")
        self.inp_ex_q1.setPlaceholderText("q1")
        self.inp_ex_q2.setPlaceholderText("q2")
        self.inp_ex_oA.setPlaceholderText("Открытый ключ Алисы")
        self.inp_ex_oB.setPlaceholderText("Открытый ключ Боба")
        self.inp_ex_m.setPlaceholderText("Сообщение")
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser(self)
        self.inp_ex_m.setFixedSize(620, 30)
        self.inp_ex_p1.setFixedSize(620, 30)
        self.inp_ex_p2.setFixedSize(620, 30)
        self.inp_ex_q1.setFixedSize(620, 30)
        self.inp_ex_q2.setFixedSize(620, 30)
        self.inp_ex_oA.setFixedSize(620, 30)
        self.inp_ex_oB.setFixedSize(620, 30)
        layout_ex.addRow(self.inp_ex_p1)
        layout_ex.addRow(self.inp_ex_p2)
        layout_ex.addRow(self.inp_ex_q1)
        layout_ex.addRow(self.inp_ex_q2)
        layout_ex.addRow(self.inp_ex_oA)
        layout_ex.addRow(self.inp_ex_oB)
        layout_ex.addRow(self.inp_ex_m)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Результат:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout(self)
        page_task.setLayout(layout_tsk)
        #values
        self.p1, self.p2 = get_prime_number_forword()
        self.q1, self.q2 = get_prime_number_forword()
        self.open_key_A = open_keya(self.p1, self.p2)
        self.open_key_B = open_keyb(self.q1, self.q2, self.open_key_A)
        self.m = message_RSA_text()
        self.name, self.index = name_choise()
        self.e_X, self.d_Y = EDS_WORD(self.p1, self.p2, self.q1, self.q2, self.open_key_A, self.open_key_B, self.m, int(self.index))
        print(self.e_X, self.d_Y)

        self.name_text = QLabel(self.name)
        self.task_text = QLabel(
            f"p1 = {self.p1}, p2 = {self.p2}, q1 = {self.q1}, q2 = {self.q2}. \nОткрытый ключ Алисы: {self.open_key_A}\nОткрытый ключ Боба: {self.open_key_B}\nСообщение = {self.m_t()}")

        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedSize(620, 160)
        self.inp_tsk_r = QLineEdit()
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        self.outp_tsk = QTextBrowser(self)
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)
        self.inp_tsk_r.setFixedSize(620, 30)

        layout_tsk.addRow(self.name_text)
        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('Введите значение:\nФормат ввода: 17 23 ...(через пробел, не для слов)'))
        layout_tsk.addRow(self.inp_tsk_r)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('Результат:'))
        layout_tsk.addRow(self.outp_tsk)

        # add pane to the tab widget
        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')

        main_layout.addWidget(tab, 0, 0, 2, 1)

    def m_t(self):
        if self.index == 0:
            return self.m
        elif self.index == 1:
            return self.e_X
        elif self.index == 2:
            return self.m
        elif self.index == 3:
            return self.e_X
        else:
            return None

    def click_btn_ex(self):
        try:
            v_exmpl_p1 = int(self.inp_ex_p1.text())
            v_exmpl_p2 = int(self.inp_ex_p2.text())
            v_exmpl_q1 = int(self.inp_ex_q1.text())
            v_exmpl_q2 = int(self.inp_ex_q2.text())
            v_exmpl_oA = int(self.inp_ex_oA.text())
            v_exmpl_oB = int(self.inp_ex_oB.text())
            v_exmpl_m = self.inp_ex_m.text()
            self.outp_ex.setHtml(f"<font style='font-family: Arial; font-size: 12pt;'>{EDS_Formula_Word(v_exmpl_p1, v_exmpl_p2, v_exmpl_q1, v_exmpl_q2, v_exmpl_oA, v_exmpl_oB, v_exmpl_m)}")
            self.inp_ex_p1.clear()
            self.inp_ex_p2.clear()
            self.inp_ex_q1.clear()
            self.inp_ex_q2.clear()
            self.inp_ex_oA.clear()
            self.inp_ex_oB.clear()
            self.inp_ex_m.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введите значения:\n")
            self.inp_ex_p1.clear()
            self.inp_ex_p2.clear()
            self.inp_ex_q1.clear()
            self.inp_ex_q2.clear()
            self.inp_ex_oA.clear()
            self.inp_ex_oB.clear()
            self.inp_ex_m.clear()
            self.update()

    def click_btn_tsk_chk(self):
        try:
            v_tsk_r = self.inp_tsk_r.text()
            e_X = self.e_X
            d_Y = self.d_Y

            if self.index == 0:
                v_r = numbers_to_string(e_X)
            elif self.index == 1:
                v_r = d_Y
            elif self.index == 2:
                v_r = numbers_to_string(e_X)
            elif self.index == 3:
                v_r = d_Y

            if (v_tsk_r == v_r ):
                self.outp_tsk.setText("Верно!")
            else:
                self.outp_tsk.setText("Не верно!")
            self.inp_tsk_r.clear()

            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введите значение!")
            self.inp_tsk_r.clear()

            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.p1, self.p2 = get_prime_number_forword()
            self.q1, self.q2 = get_prime_number_forword()
            self.open_key_A = open_keya(self.p1, self.p2)
            self.open_key_B = open_keyb(self.q1, self.q2, self.open_key_A)
            self.name, self.index = name_choise()
            self.m = message_RSA_text()
            self.e_X, self.d_Y = EDS_WORD(self.p1, self.p2, self.q1, self.q2, self.open_key_A, self.open_key_B, self.m, self.index)
            print(self.e_X, self.d_Y)
            self.name_text.setText(self.name)
            self.task_text.setText(f"p1 = {self.p1}, p2 = {self.p2}, q1 = {self.q1}, q2 = {self.q2}.\nОткрытый ключ Алисы: {self.open_key_A}\nОткрытый ключ Боба: {self.open_key_B}\nСообщение = {self.m_t()}")
            self.inp_tsk_r.clear()
            self.outp_tsk.setText(f"")
            self.update()
        except ValueError:
            print(ValueError)


def win4(w):
    w.window = Window_4()
    w.window.show()

