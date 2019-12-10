import win32com.client
import pytesseract
from PIL import Image

a="扁 担 长 ， 板 凳 宽 ， 扁 担 比 板 凳 长 ， 板 凳 比 扁 担 宽 ， 扁 担 绑 在 了 板 凳 上 ， 板 凳 不 让 扁 担 绑 在 板 凳 上 ， 扁 担 非 要 绑 在 板 凳 上"
speaker=win32com.client.Dispatch("SAPI.SpVoice")
#speaker.Speak("You are my everything!我们都有一个家，名字叫中国")
speaker.Speak(a)

#pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('C://Users/kangl/Desktop/test.jpg'))

print(text)
speaker.Speak(text)
