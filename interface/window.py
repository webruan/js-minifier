import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtGui import QFont, QIcon

from interface.textbox import CodeProcessPanel 
from interface.buttons import ButtonsPanel 

class JSMinifierApp(QWidget):
  def __init__(self):
    super().__init__()

    path = os.path.dirname(os.path.realpath(__file__))
    self.setWindowTitle("JS Minifier v1.0 - 2023 [@webruan]")
    self.setWindowIcon(QIcon(os.path.join(path, '../assets/images/javascript-logo.svg')))
    self.setMaximumSize(1400, 700)
    self.setupUI()

  def setupUI(self):
    main_layout = QVBoxLayout()
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    
    title_label = QLabel("JS Minifier")
    title_label.setAlignment(Qt.AlignCenter)
    title_font = QFont("Arial", 34, QFont.Bold) 
    title_label.setFont(title_font)
    main_layout.addWidget(title_label)

    main_layout.addSpacing(32)

    # Criar uma instância de CodeProcessPanel
    inputs_row = CodeProcessPanel()

    # Chame os métodos leftColumn() e rightColumn() para configurar os layouts
    inputs_row.leftColumn()
    inputs_row.rightColumn()

    buttons_row = ButtonsPanel(inputs_row.input_code_entry, inputs_row.output_code_entry, inputs_row.input_code_size_entry, inputs_row.output_code_size_entry)

    buttons_row.buttons()

    # Adicione o layout principal de CodeProcessPanel a main_layout
    main_layout.addLayout(inputs_row.main_row_layout)
    main_layout.addLayout(buttons_row.buttons_row_layout)

    self.setLayout(main_layout)