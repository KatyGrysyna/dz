import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
      html = file.read()

      cleaned_text = ""
      is_tag = False
      for char in html:
          if char == "<":
              is_tag = True
          elif char == ">":
              is_tag = False
          else:
              if not is_tag:
                  cleaned_text += char
      with codecs.open(result_file, 'w', 'utf-8') as file:
          file.write(cleaned_text)

delete_html_tags('draft.html')


