from PyQt5.QtWidgets import *

from calc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("CALCULATOR")
        self.temp_nums = []
        self.fin_nums = []

        # buttons

        self.enter_btn.pressed.connect(self.func_result)
        self.clear_btn.pressed.connect(self.clear_calc)
        self.nine_btn.pressed.connect(lambda: self.num_press('9'))
        self.eight_btn.pressed.connect(lambda: self.num_press('8'))
        self.seven_btn.pressed.connect(lambda: self.num_press('7'))
        self.six_btn.pressed.connect(lambda: self.num_press('6'))
        self.five_btn.pressed.connect(lambda: self.num_press('5'))
        self.four_btn.pressed.connect(lambda: self.num_press('4'))
        self.three_btn.pressed.connect(lambda: self.num_press('3'))
        self.two_btn.pressed.connect(lambda: self.num_press('2'))
        self.one_btn.pressed.connect(lambda: self.num_press('1'))
        self.zero_btn.pressed.connect(lambda: self.num_press('0'))
        self.add_btn.pressed.connect(lambda: self.func_press('+'))
        self.sub_btn.pressed.connect(lambda: self.func_press('-'))
        self.mul_btn.pressed.connect(lambda: self.func_press('*'))
        self.div_btn.pressed.connect(lambda: self.func_press('/'))

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.input_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.input_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.input_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)

        fin_string = str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.input_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = QApplication([])
window = MainWindow()
window.show()
app.setStyle(QStyleFactory.create("Fusion"))
app.exec()
