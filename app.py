import streamlit as st
import pandas as pd
import joblib

# 1. Cargamos el modelo que descargamos de Colab
# Asegurar de que el archivo .joblib esté en la misma carpeta que este script
@st.cache_resource
def load_model():
    return joblib.load('modelo_fraude_random_forest.joblib')

modelo = load_model()

# 2. Configuración estética de la página web
st.set_page_config(page_title="Detector de Fraude E-Commerce", page_icon="🚨", layout="centered")

st.title("🚨 Sistema Inteligente Antifraude (Random Forest)")
st.write("Introduce los detalles de la transacción para evaluar el riesgo de fraude en tiempo real.")
st.markdown("---")

# 3. Formulario visual para el usuario
col1, col2 = st.columns(2)

with col1:
    dinero_gastado = st.number_input("Monto de la Transacción (€)", min_value=1.0, max_value=50000.0, value=150.0, step=10.0)
    cliente_edad = st.slider("Edad del Cliente", min_value=1, max_value=100, value=30)
    cantidad = st.number_input("Cantidad de Productos", min_value=1, max_value=20, value=1)
    hora_transaccion = st.slider("Hora de la Transacción (0-23h)", min_value=0, max_value=23, value=14)

with col2:
    # Opciones que se traducen automáticamente a los números que entiende el LabelEncoder
    metodo_pago_map = {"PayPal": 0, "Credit Card": 1, "Debit Card": 2, "Bank Transfer": 3}
    metodo_pago_sel = st.selectbox("Método de Pago", list(metodo_pago_map.keys()))
    metodo_pago = metodo_pago_map[metodo_pago_sel]

    producto_map = {"Electronics": 0, "Clothing": 1, "Home & Garden": 2, "Health & Beauty": 3}
    producto_sel = st.selectbox("Categoría del Producto", list(producto_map.keys()))
    categoria_producto = producto_map[producto_sel]

    dispositivo_map = {"Mobile": 0, "Desktop": 1, "Tablet": 2}
    dispositivo_sel = st.selectbox("Dispositivo Utilizado", list(dispositivo_map.keys()))
    dispositivo = dispositivo_map[dispositivo_sel]

st.markdown("---")

# 4. Predicción al pulsar el botón
if st.button(" Evaluar Transacción", use_container_width=True):
    
    # Creamos el DataFrame con las 6 columnas EXACTAS y en el mismo orden que Colab espera
    datos_usuario = pd.DataFrame([{
        'Transaction Amount': dinero_gastado,
        'Payment Method': metodo_pago,
        'Product Category': categoria_producto,
        'Quantity': cantidad,
        'Customer Age': cliente_edad,
        'Device Used': dispositivo
    }])
    
    # Hacemos la predicción pasándole el DataFrame estructurado
    prediccion = modelo.predict(datos_usuario)
    
    # Mostramos el resultado visual
    if prediccion[0] == 1:
        st.error("🚨 **¡ALERTA! Transacción bloqueada.** El modelo ha detectado un patrón de fraude de alto riesgo.")
    else:
        st.success("✅ **Transacción Autorizada.** El comportamiento de la operación se considera seguro.")
