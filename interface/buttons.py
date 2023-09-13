from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QApplication
from PyQt5.QtGui import QFont
from functions.clear import clearCode
from functions.copy import copyCode
from functions.remove import removeSpaces

class ButtonsPanel:
  buttons_row_layout = QHBoxLayout()
  font_size_14 = QFont("Arial", 14) 

  style_path = r'C:\Users\ruanb\Documentos\Python\Projetos\minifier\js-minifier\assets\styles\style.qss'

  with open(style_path, 'r') as style_file:
    style_qss = style_file.read()

  def __init__(self, input_code_entry, output_code_entry, input_code_size_entry, output_code_size_entry):
    self.input_code_entry = input_code_entry
    self.output_code_entry = output_code_entry
    self.input_code_size_entry = input_code_size_entry
    self.output_code_size_entry = output_code_size_entry

  def buttons(self):
    button_remove_spaces = QPushButton('Remover espaços')
    button_copy_code = QPushButton('Copiar código')
    button_clear_all = QPushButton('Limpar campos')

    button_remove_spaces.setFont(ButtonsPanel.font_size_14)
    button_copy_code.setFont(ButtonsPanel.font_size_14)
    button_clear_all.setFont(ButtonsPanel.font_size_14)

    button_remove_spaces.setObjectName('greenButton')
    button_copy_code.setObjectName('blueButton')
    button_clear_all.setObjectName('yellowButton')

    button_remove_spaces.setStyleSheet(ButtonsPanel.style_qss)
    button_copy_code.setStyleSheet(ButtonsPanel.style_qss)
    button_clear_all.setStyleSheet(ButtonsPanel.style_qss)

    button_remove_spaces.setMaximumWidth(350)
    button_copy_code.setMaximumWidth(350)
    button_clear_all.setMaximumWidth(350)

    ButtonsPanel.buttons_row_layout.addWidget(button_remove_spaces)
    ButtonsPanel.buttons_row_layout.addWidget(button_copy_code)
    ButtonsPanel.buttons_row_layout.addWidget(button_clear_all)

    button_remove_spaces.clicked.connect(lambda: self.call_removeSpaces())
    button_copy_code.clicked.connect(lambda: self.call_copyCode())
    button_clear_all.clicked.connect(lambda: self.call_clearCode())

  def call_removeSpaces(self):
    removeSpaces(self.input_code_entry, self.output_code_entry, self.input_code_size_entry, self.output_code_size_entry)

  def call_copyCode(self):
    cb = QApplication.clipboard()
    copyCode(self.output_code_entry, cb)

  def call_clearCode(self):
    clearCode(self.input_code_entry, self.output_code_entry)