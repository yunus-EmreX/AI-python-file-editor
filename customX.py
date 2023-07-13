from tkinter import *
from tkinter import filedialog, messagebox
import sys
import tokenize
import io

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        with open(filepath, "r") as file:
            code_text.delete("1.0", END)
            code_text.insert(END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(code_text.get("1.0", END))
        messagebox.showinfo("Kaydedildi!", "Dosya başarıyla kaydedildi.")

def save_as_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files","*.py")])
    
    if filepath:
        with open(filepath, "w") as f: 
            f.write(code_text.get(1.0, END))

def check_syntax(event=None):
    code = code_text.get('1.0', 'end-1c')
    
    try:
        compile(code, filename="<string>", mode="exec")

        # Köşede yapımcı bilgisi ekleme
        status_label.config(text="Yapımcı: Yunus Emre Yüksel | Sürüm: 037.1 E")
         
    except SyntaxError as e:
        error_message = str(e)

        # Hata mesajını bulunan satır ve sütun bilgisiyle birleştirme
        for token in tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline):
            if token.start[0] == e.lineno:
                error_message += f"\nSatır {e.lineno}, Sütun {token.start[1]}: {e.text.strip()}"

        # Hata mesajını kullanıcıya gösterme
        messagebox.showerror(title="Syntax Hatası", message=error_message)

# Ana pencere oluşturma
root = Tk()
root.title("Python Görüntüleyici ve Düzenleyici")
root.geometry("800x600")

# Arka plan rengini belirleme
background_color = "#FFCC00"
root.configure(bg=background_color)

# Menu Bar oluşturma
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_command(label="Farklı Kaydet", command=save_as_file)
menubar.add_cascade(label="Dosya", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Syntax Kontrol Et", command=check_syntax)
menubar.add_cascade(label="Düzenle", menu=edit_menu)

root.config(menu=menubar)

# Kod görüntüleme ve düzenleme alanı oluşturma
code_text = Text(root, font=("Courier New", 12))
code_text.pack(fill=BOTH, expand=True)

# Yapımcı bilgisi etiketi oluşturma ve konumlandırma (sağ alt köşe)
status_label = Label(root, text="Yapımcı: Yunus Emre Yüksel | Sürüm: 0 37.1 E", bd=1, relief=SUNKEN, anchor=E)
status_label.pack(side=BOTTOM, fill=X)

root.mainloop()
