import tkinter as tk
import time
from tkinter import messagebox, filedialog 
from tkcalendar import Calendar

class Anotador:
    def __init__(self, root):
        self.root = root
        self.root.title("Anotador")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        self.create_notepad()
        self.create_panel_derecha()
        self.create_menu()
 

    def create_menu(self):
        # Menu principal....
        menu_principal = tk.Menu(self.root)
        self.root.config(menu=menu_principal)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
    
    def create_panel_derecha(self):
        
        derecha_panel = tk.Frame(self.root)
        derecha_panel.pack(side="right", fill="y", padx=10, pady=10)
        
    
        self.label_reloj = tk.Label(derecha_panel, text="Reloj", font=("Helvetica", 14))
        self.label_hora = tk.Label(derecha_panel, font=("Helvetica", 20, "bold"), foreground="blue")
         
        self.label_reloj.pack(pady=(0, 10))
        self.label_hora.pack()
         
        self.update_time()

        self.label_calendario = tk.Label(derecha_panel, text="Calendario", font=("Helvetica", 14))
        self.calendar = Calendar(derecha_panel, selectmode="day", date_pattern="dd/mm/yyyy")
        
        self.label_calendario.pack(pady=(20, 10))
        self.calendar.pack()
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
    
    # Botones.
    
    def nuevo_archivo(self):
        if len(self.text_area.get("1.0", tk.END).strip()) > 0:
             respuesta = messagebox.askyesno(
                "Seguro",
                "Hay texto sin guardar ¿Seguro quieres crear una nota nueva?")
             if not respuesta:
                 return
        
        self.text_area.delete("1.0", tk.END)
        self.root.title("Nota nueva - Anotador")
        
    def guardar_archivo (self):
        
        ruta_archivo = filedialog.asksaveasfilename(
            title= "Guardar nota..",
            defaultextension=".text",
            filetypes=[("Arhivos de Texto","*.txt"), ("Todos los arhivos", "*.*")]
        )
        
        if not ruta_archivo:
            return
        
        try:
            with open(ruta_archivo, "w", encoding="utgf-8") as archivo:
                guardar_texto = self.text_area.get("1.0", tk.END)
                archivo.write(guardar_texto)
                
                self.root.title(f"Guardado: {ruta_archivo} -  Anotador")
                messagebox.showinfo("La nota se ha guardado correctamente 😎👍")
        except Exception as e:
            messagebox.showerror("OH 😵, ocurrio un error al guardar el archivo", f"El archivo. \nError: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Anotador(root)
    root.mainloop()
