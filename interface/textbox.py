from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtGui import QFont

class CodeProcessPanel:
  main_row_layout = QHBoxLayout()
  font_size_18 = QFont("Arial", 18) 
  font_size_12 = QFont("Arial", 12) 

  def __init__(self):
    self.input_code_entry = None
    self.output_code_entry = None
    self.input_code_size_entry = None
    self.output_code_size_entry = None

  def leftColumn(self):
    left_column_layout = QVBoxLayout()

    input_code_label = QLabel("Código de entrada:")
    input_code_label.setFont(CodeProcessPanel.font_size_18)

    self.input_code_entry = QPlainTextEdit()
    self.input_code_entry.setFixedWidth(600)
    self.input_code_entry.setFixedHeight(300)

    input_code_size_label = QLabel("Tamanho: ")
    input_code_size_label.setFont(CodeProcessPanel.font_size_12)
    self.input_code_size_entry = QLabel()

    left_column_layout.addWidget(input_code_label)
    left_column_layout.addWidget(self.input_code_entry)
    left_column_layout.addWidget(input_code_size_label)
    left_column_layout.addWidget(self.input_code_size_entry)

    CodeProcessPanel.main_row_layout.addLayout(left_column_layout)

  def rightColumn(self):
    right_column_layout = QVBoxLayout()

    output_code_label = QLabel("Código de saída:")
    output_code_label.setFont(CodeProcessPanel.font_size_18)

    self.output_code_entry = QPlainTextEdit()
    self.output_code_entry.setFixedHeight(300)
    self.output_code_entry.setFixedWidth(600)
    self.output_code_entry.setDisabled(True)

    output_code_size_label = QLabel("Tamanho: ")
    output_code_size_label.setFont(CodeProcessPanel.font_size_12)
    self.output_code_size_entry = QLabel()

    right_column_layout.addWidget(output_code_label)
    right_column_layout.addWidget(self.output_code_entry)
    right_column_layout.addWidget(output_code_size_label)
    right_column_layout.addWidget(self.output_code_size_entry)
    
    CodeProcessPanel.main_row_layout.addLayout(right_column_layout)