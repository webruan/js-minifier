def removeComments(code):
  in_string = False
  new_code = ''
  i = 0

  while i < len(code):
    if i < len(code) - 1 and code[i:i+2] == '//' and not in_string:
      # Encontrou um comentário de linha fora de uma string
      while i < len(code) and code[i] != '\n':
        i += 1
    elif code[i] in ['"', "'"]:
      # Iniciou ou finalizou uma string
      if in_string:
        in_string = False
      else:
        in_string = True
      new_code += code[i]
      i += 1
    else:
      new_code += code[i]
      i += 1

  return new_code

def removeSpaces(input_code_entry, output_code_entry, input_code_size_entry, output_code_size_entry):
  code_input = input_code_entry.toPlainText()

  if code_input.strip():
    code_input_no_comments = removeComments(code_input)

    result = []
    inside_quotes = False
    current_word = ''
    keep_spaces_around = ('var', 'const', 'let', 'instanceof', 'in')
    keep_spaces_after = ('function', 'typeof', 'else', 'return', 'instance', 'throw', 'case')
    keep_spaces_before = ('TypeError')

    for char in code_input_no_comments:
      if char in ('"', "'", '`'):
        inside_quotes = not inside_quotes
        result.append(current_word + char)

        current_word = ''
      elif inside_quotes:
        current_word += char
      else:
        if char.isspace():
          if current_word:
            if current_word in keep_spaces_around:
              result.append(' ' + current_word + ' ')
            elif current_word in keep_spaces_after:
              result.append(current_word + ' ')
            elif current_word in keep_spaces_before:
              result.append(' ' + current_word)
            else:
              result.append(current_word)
          current_word = ''
        else:
          current_word += char
    if current_word:
      if current_word in keep_spaces_around:
        result.append(' ' + current_word + ' ')
      elif current_word in keep_spaces_after:
        result.append(current_word + ' ')
      elif current_word in keep_spaces_before:
        result.append(' ' + current_word)
      else:
        result.append(current_word)

    formatted_code = ''.join(result)

    output_code_entry.clear()
    output_code_entry.insertPlainText(formatted_code)

    actual_size = len(code_input.encode('utf-8'))
    actual_insert_size = round((actual_size / 1024), 2)

    new_size = len(formatted_code.encode('utf-8'))
    new_output_size = round((new_size / 1024), 2)
    
    if new_output_size < 1:
      size_out = ' Bytes'
    else:
      size_out = ' KB'
    
    if actual_insert_size < 1:
      size_in = ' Bytes'
    else:
      size_in = ' KB'

    input_code_size_entry.setText(str(actual_insert_size) + str(size_in))
    output_code_size_entry.setText(str(new_output_size) + str(size_out))

  else:
    print('Nenhum código!')


  
