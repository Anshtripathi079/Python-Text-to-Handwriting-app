import pywhatkit as pw

txt = """this is a text This is a textThis is a textThis is a textThis is a textThis is a text"""

pw.text_to_handwriting(txt,"file1.png",[0,0,138])
print("end")