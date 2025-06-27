# Importamos
import tkinter as tk
import time
from tkcalendar import Calendar

root = tk.Tk() 
root.title ("Proyecto")
root.geometry("800x600")  



#Menu 

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)

menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label = "Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

#Reloj

def actualizacion_tiempo():
    hora_actual = time.strftime("%H:%M")
    etiqueta_reloj.config(text=hora_actual) 
    root.after(100, actualizacion_tiempo)

etiqueta_reloj = tk.Label(root, font=("Arial", 30))
etiqueta_reloj.pack(pady=10)
actualizacion_tiempo()

#Calendario
calendario = Calendar(root, selectmode='day', year=2025, moth=6, day=27)
calendario.pack(pady=10)
calendario.get_date()


#Anotador 

anotador = tk.Text(root, height=10, width=50)
anotador.pack(pady=10)

root.mainloop()  