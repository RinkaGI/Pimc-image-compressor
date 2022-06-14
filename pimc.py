from distutils import extension
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from tqdm import tqdm_gui

ventana = tk.Tk()

# Configuracion de la ventana
ventana.title('Pimc - Image Compressor')
ventana.geometry("950x660")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file='img/fondo.png')
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

############################################# COMPONENTES DE INTERACCIÓN ########################################3

# BOTONES

imageDir = None
imageExtensions = ['*.png', '*.jpg', '*.jpeg']

def botonImportarFunc():
    imageDir = askopenfilename(
        title = "Import image",
        filetypes = [
            (
                'Images',
                imageExtensions
            )
        ]
    )

    imagen = Image.open(imageDir)

    for i in tqdm_gui(range(int(60))):
        imagen = imagen.convert('RGB')
        imagen.save('compressed_image.jpg', quality=25)


botonImportar = tk.Button(
    master = ventana,
    text = "Import image",
    cursor = "hand2",
    width = 20,
    height = 1,
    relief = "flat",
    command = botonImportarFunc,
    font = (
        "Arial",
        32,
        "bold"
    )
)

botonImportarX = 950/2 - 250
botonImportarY = 660/2

botonImportar.place(
    x = botonImportarX,
    y = botonImportarY
)

def botonSalirFunc():
    ventana.quit()

botonSalir = tk.Button(
    master = ventana,
    text = "Exit",
    cursor = "hand2",
    width = 10,
    height = 1,
    relief = "flat",
    command = botonSalirFunc,
    font = (
        "Arial",
        24,
        "bold"
    )
)

botonSalirX = 950-200
botonSalirY = 660-50

botonSalir.place(
    x = botonSalirX,
    y = botonSalirY
)


# Ejecutar la ventana
ventana.mainloop()
