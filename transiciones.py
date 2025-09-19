import tkinter as tk
import time

def animacion_carga(callback_final):
    ventana=tk.Tk()
    ventana.title("Cargando Sentencia Binaria...")
    
    texto=tk.Label(ventana,text="⏳ Preparando dilemas...", font=("Helvetica", 14))
    texto.pack(pady=20)
    
    barra=tk.Canvas(ventana,width=300, height=20)
    barra.pack()
    rect=barra.create_rectangle(0,0,0,20,fill="green")
    
    def cargar():
        for i in range(0,301,30):
            barra.coords(rect,0,0,i,20)
            ventana.update()
            time.sleep(0.2)
        ventana.destroy()
        callback_final()
    ventana.after(100,cargar)
    ventana.mainloop()