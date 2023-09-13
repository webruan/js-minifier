def copyCode(output_code_entry, cb):
  cb.clear(mode=cb.Clipboard)
  cb.setText(output_code_entry.toPlainText(), mode=cb.Clipboard)