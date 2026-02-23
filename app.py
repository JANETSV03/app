import streamlit as st
import pandas as pd

# ---------------------------
# Lista global de actividades
# ---------------------------
if "actividades" not in st.session_state:
    st.session_state.actividades = []

# ---------------------------
# Clase para POO (Ejercicio 4)
# ---------------------------
class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    def esta_en_presupuesto(self):
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self):
        return f"{self.nombre} | Tipo: {self.tipo} | Presupuesto: {self.presupuesto} | Gasto: {self.gasto_real}"


# ---------------------------
# Navegación
# ---------------------------
menu = st.sidebar.selectbox(
    "Menú",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ===========================
# HOME
# ===========================
if menu == "Home":
    st.title("Proyecto Módulo 1 – Python Fundamentals")

    st.write("Nombre: Janet Salazar")
    st.write("Curso: Especialización Python for Analytics")
    st.write("Año: 2026")

    st.write("""
    Este proyecto integra los conceptos fundamentales de programación:
    variables, estructuras de datos, control de flujo, funciones,
    programación funcional y programación orientada a objetos.
    """)

    st.write("Tecnologías utilizadas:")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Pandas")

# ===========================
# EJERCICIO 1
# ===========================
elif menu == "Ejercicio 1":
    st.subheader("Ejercicio 1 – Variables y Condicionales")

    presupuesto = st.number_input("Ingrese su presupuesto", min_value=0.0)
    gasto = st.number_input("Ingrese su gasto", min_value=0.0)

    if st.button("Evaluar"):
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El presupuesto fue excedido.")

        st.write(f"Diferencia: {diferencia:.2f}")

# ===========================
# EJERCICIO 2
# ===========================
elif menu == "Ejercicio 2":
    st.subheader("Ejercicio 2 – Listas y Diccionarios")

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo", ["Inversión", "Ahorro", "Gasto"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0)

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)

    if st.session_state.actividades:
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df)

        st.write("Estado de las actividades:")
        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                st.success(f"{act['nombre']} está dentro del presupuesto")
            else:
                st.warning(f"{act['nombre']} excedió el presupuesto")

# ===========================
# EJERCICIO 3
# ===========================
elif menu == "Ejercicio 3":
    st.subheader("Ejercicio 3 – Funciones y Programación Funcional")

    tasa = st.slider("Tasa", 0.0, 1.0, 0.1)
    meses = st.number_input("Meses", min_value=1)

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    if st.button("Calcular retorno"):
        if st.session_state.actividades:
            retornos = list(
                map(lambda act: calcular_retorno(act, tasa, meses),
                    st.session_state.actividades)
            )

            for act, r in zip(st.session_state.actividades, retornos):
                st.write(f"{act['nombre']} → Retorno esperado: {r:.2f}")
        else:
            st.warning("No hay actividades registradas.")

# ===========================
# EJERCICIO 4
# ===========================
elif menu == "Ejercicio 4":
    st.subheader("Ejercicio 4 – Programación Orientada a Objetos")

    if st.session_state.actividades:
        objetos = [
            Actividad(a["nombre"], a["tipo"], a["presupuesto"], a["gasto_real"])
            for a in st.session_state.actividades
        ]

        for obj in objetos:
            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("No cumple el presupuesto")
    else:
        st.warning("Primero registre actividades en el Ejercicio 2.")