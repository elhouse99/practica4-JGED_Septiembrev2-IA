import tkinter as tk
from tkinter import messagebox
import re

Ventana = tk.Tk()
Ventana.geometry("350x500")
Ventana.config(bg="pink")
Ventana.title("Actividad 05 - Formulario de registro Vr.002")

# --- FUNCIONES DE VALIDACIÓN ---
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    # Se añade comprobación para evitar fallos si el string queda vacío tras aplicar strip()
    if not valor: return False
    return bool(re.match(r"^[a-zA-Z\s]+$", valor))

# --- FUNCIONES OPERATIVAS ---
def LimpiarFormulario(pedir_confirmacion=False):
    # Se añade la alerta de confirmación solicitada
    if pedir_confirmacion:
        respuesta = messagebox.askyesno("Confirmar", "¿Seguro que desea limpiar todos los campos?")
        if not respuesta:
            return

    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    varGenero.set(0)

def GuardarRegistro():
    # Optimización: Se añade .strip() para limpiar espacios vacíos accidentales
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()
    
    genero = ""
    if varGenero.get() == 1:
        genero = "Hombre"
    elif varGenero.get() == 2:
        genero = "Mujer"
    elif varGenero.get() == 3:
        genero = "Otro"
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un género.")
        return
    
    # Validación lógica
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and 
        es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and 
        es_texto_valido(apellidos)):
        
        # Optimización: Uso de f-strings en lugar de concatenación manual
        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nEstatura: {estatura}\nTelefono: {telefono}\nGenero: {genero}\n"
        
        # Mejora: Implementación de try-except y codificación UTF-8
        try:
            with open("registro.txt", "a", encoding="utf-8") as archivo:
                archivo.write(datos + "\n")
            
            messagebox.showinfo("Información", f"Datos guardados con éxito:\n\n{datos}")
            
            # Se reutiliza la función limpiando directamente sin pedir confirmación
            LimpiarFormulario(pedir_confirmacion=False)
        except Exception as e:
            messagebox.showerror("Error de Sistema", f"No se pudo escribir en el archivo: {e}")
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")

# --- INTERFAZ GRÁFICA ---
varGenero = tk.IntVar()

# Mejora estética: Se añadió bg="pink" a los controles para que no tengan fondo gris brillante
lbNombre = tk.Label(Ventana, text="Nombre: ", bg="pink")
lbNombre.pack()
tbNombre = tk.Entry(Ventana)
tbNombre.pack()

lbApellidos = tk.Label(Ventana, text="Apellido: ", bg="pink")
lbApellidos.pack()
tbApellidos = tk.Entry(Ventana)
tbApellidos.pack()

lbTelefono = tk.Label(Ventana, text="Telefono: ", bg="pink")
lbTelefono.pack()
tbTelefono = tk.Entry(Ventana)
tbTelefono.pack()

lbEdad = tk.Label(Ventana, text="Edad: ", bg="pink")
lbEdad.pack()
tbEdad = tk.Entry(Ventana)
tbEdad.pack()

lbEstatura = tk.Label(Ventana, text="Estatura: ", bg="pink")
lbEstatura.pack()
tbEstatura = tk.Entry(Ventana)
tbEstatura.pack()

groupBox = tk.LabelFrame(Ventana, text="Género:", padx=12, pady=12, bg="pink")
groupBox.pack(pady=10)

rbMasculino = tk.Radiobutton(groupBox, text="Masculino", variable=varGenero, value=1, bg="pink")
rbMasculino.grid(row=0, column=0)

rbFemenino = tk.Radiobutton(groupBox, text="Femenino", variable=varGenero, value=2, bg="pink")
rbFemenino.grid(row=0, column=1)

rbOtro = tk.Radiobutton(groupBox, text="Otro", variable=varGenero, value=3, bg="pink")
rbOtro.grid(row=0, column=2)

btnGuardar = tk.Button(Ventana, text="Guardar", command=GuardarRegistro)
btnGuardar.pack(pady=5)

# Se utiliza una función lambda para enviar el parámetro True al botón de la interfaz
btnLimpiar = tk.Button(Ventana, text="Limpiar", command=lambda: LimpiarFormulario(pedir_confirmacion=True))
btnLimpiar.pack(pady=5)

Ventana.mainloop()