# Importamos
import tkinter as tk
import time
from tkcalendar import Calendar

root = tk.Tk() 
root.title ("Anotador")
root.geometry("800x600") 
root.config(bg=("blue")) 
root.minsize(300,150)



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
posicion = tk.Frame(root, padx=10, pady=10)

def actualizacion_tiempo():
    hora_actual = time.strftime("%H:%M")
    etiqueta_reloj.config(text=hora_actual) 
    root.after(1000, actualizacion_tiempo)

etiqueta_reloj = tk.Label(posicion, text="Reloj", font=("Helvetica", 14))
etiqueta_reloj.pack(pady=(20,10))
reloj_label= tk.Label(posicion, font=("Helvetica", 20, "bold"), foreground="blue")
etiqueta_reloj.pack()
posicion.pack(side="right", fill="y", padx=10, pady=10)
actualizacion_tiempo()


#Calendario
calendario = tk.Label(posicion, text="Calendario")
calendario = Calendar(posicion, selectmode='day', year=2025, moth=6, day=27)
calendario.pack()
calendario.get_date()


#Anotador 
lado_izquierdo = tk.Frame(root)
lado_izquierdo.pack(side="left", fill="both", expand=True,  padx=10, pady=10 )
anotador = tk.Label(lado_izquierdo, text="Empeza a escribir aquí...")
anotador.pack(pady=(0, 10), anchor="w")



# Barra para desplzar
scroll = tk.Scrollbar(lado_izquierdo)
scroll.pack(side="right", fill="y")

#texto
texto = tk.Text(lado_izquierdo, wrap="word", font=("Helvetica", 12), yscrollcommand=scroll.set)
texto.pack(side="left",fill="both", expand=True)

# conexion texto scroll
scroll.config(command=texto.yview)


root.mainloop()  