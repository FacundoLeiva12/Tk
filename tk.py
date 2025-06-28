import tkinter as tk
import time
from tkcalendar import Calendar

class Anotador:
    def __init__(self, root):
        self.root = root
        self.root.title("Anotador")
        self.root.geometry("800x600")
        self.root.config(bg="blue")
        self.root.minsize(300, 150)
        
        self.create_menu()
        self.create_clock()
        self.create_calendar()
        self.create_notepad()

    def create_menu(self):
        # Menu principal
        menu_principal = tk.Menu(self.root)
        self.root.config(menu=menu_principal)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Nuevo")
        menu_archivo.add_command(label="Guardar")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)

    def create_clock(self):
        # Reloj
        self.clock_frame = tk.Frame(self.root, padx=10, pady=10)
        self.label_reloj = tk.Label(self.clock_frame, text="Reloj", font=("Helvetica", 14))
        self.label_hora = tk.Label(self.clock_frame, font=("Helvetica", 20, "bold"), foreground="blue")
        
        self.label_reloj.pack(pady=(20,10))
        self.label_hora.pack()
        
        self.clock_frame.pack(side="right", fill="y", padx=10, pady=10)
        self.update_time()

    def update_time(self):
        hora_actual = time.strftime("%H:%M")
        self.label_hora.config(text=hora_actual)
        self.root.after(1000, self.update_time)

    def create_calendar(self):
        # Calendario
        self.label_calendario = tk.Label(self.root, text="Calendario")
        self.calendar = Calendar(self.root, selectmode='day', year=2025, month=6, day=27)

        self.label_calendario.pack()
        self.calendar.pack()

    def create_notepad(self):
        # Anotador
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.notepad_label = tk.Label(self.left_frame, text="Empeza a escribir aquí...")
        self.notepad_label.pack(pady=(0, 10), anchor="w")

        # Barra de desplazamiento
        self.scroll = tk.Scrollbar(self.left_frame)
        self.scroll.pack(side="right", fill="y")

        self.text_area = tk.Text(self.left_frame, wrap="word", font=("Helvetica", 12), yscrollcommand=self.scroll.set)
        self.text_area.pack(side="left", fill="both", expand=True)

        # Conexión texto scroll
        self.scroll.config(command=self.text_area.yview)

if __name__ == "__main__":
    root = tk.Tk()
    app = Anotador(root)
    root.mainloop()
