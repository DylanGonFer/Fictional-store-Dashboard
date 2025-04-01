import pandas as pd
from faker import Faker
import random
import os

# Configuración de Faker
fake = Faker('es_ES')  # Puedes elegir un idioma específico para mayor realismo
Faker.seed(42)

# Generar datos para las tablas
def generar_tabla_clientes():
    data = []
    for _ in range(100):  # Número de registros
        data.append({
            'id_cliente': fake.unique.random_int(min=1000, max=9999),
            'nombre': fake.name(),
            'email': fake.email(),
            'dirección': fake.address(),
            'teléfono': fake.phone_number()
        })
    return pd.DataFrame(data)

def generar_tabla_productos():
    data = []
    for _ in range(50):
        data.append({
            'id_producto': fake.unique.random_int(min=100, max=999),
            'nombre_producto': fake.word(),
            'precio': round(random.uniform(10, 1000), 2),  # Precio entre 10 y 1000
            'categoría': fake.random_element(elements=('Electrónica', 'Ropa', 'Hogar', 'Juguetes', 'Libros')),
            'stock': random.randint(0, 500)
        })
    return pd.DataFrame(data)

def generar_tabla_ventas(clientes, productos):
    data = []
    for _ in range(400):
        cliente = clientes.sample(1).iloc[0]
        producto = productos.sample(1).iloc[0]
        cantidad = random.randint(1, 10)
        total = round(cantidad * producto['precio'], 2)
        data.append({
            'id_venta': fake.unique.random_int(min=10000, max=99999),
            'fecha': fake.date_this_year(),
            'id_cliente': cliente['id_cliente'],
            'id_producto': producto['id_producto'],
            'id_sucursal': fake.random_int(min=1, max=20),  # Asumiendo que hay 20 sucursales
            'cantidad': cantidad,
            'total': total
        })
    return pd.DataFrame(data)

def generar_tabla_metodos_pago():
    data = []
    for _ in range(5):
        data.append({
            'id_pago': fake.unique.random_int(min=1, max=100),
            'tipo_pago': fake.random_element(elements=('Tarjeta de Crédito', 'Tarjeta de Débito', 'Paypal', 'Transferencia', 'Efectivo')),
            'detalles_pago': fake.credit_card_number()
        })
    return pd.DataFrame(data)

def generar_tabla_inventario(productos):
    data = []
    for _, producto in productos.iterrows():
        data.append({
            'id_inventario': fake.unique.random_int(min=1000, max=9999),
            'id_producto': producto['id_producto'],
            'fecha_actualización': fake.date_this_month(),
            'cantidad_disponible': producto['stock']
        })
    return pd.DataFrame(data)

def generar_tabla_proveedores(productos):
    data = []
    for _, producto in productos.iterrows():
        data.append({
            'id_proveedor': fake.unique.random_int(min=100, max=999),
            'nombre_proveedor': fake.company(),
            'contacto': fake.phone_number(),
            'dirección': fake.address(),
            'id_producto': producto['id_producto']
        })
    return pd.DataFrame(data)

def generar_tabla_sucursales():
    data = []
    for _ in range(20):  # Número de sucursales
        data.append({
            'id_sucursal': fake.unique.random_int(min=1, max=100),
            'nombre_sucursal': fake.company(),
            'región': fake.random_element(elements=('América del Norte', 'América del Sur', 'Europa', 'Asia', 'Oceanía')),
            'país': fake.random_element(elements=('Argentina', 'Brasil', 'México', 'Estados Unidos', 'España')),
            'ciudad': fake.city(),
            'dirección': fake.address()
        })
    return pd.DataFrame(data)

# Incorporarlo al flujo general del proyecto
def crear_datos_con_sucursales():
    clientes = generar_tabla_clientes()
    productos = generar_tabla_productos()
    ventas = generar_tabla_ventas(clientes, productos)
    metodos_pago = generar_tabla_metodos_pago()
    inventario = generar_tabla_inventario(productos)
    proveedores = generar_tabla_proveedores(productos)
    sucursales = generar_tabla_sucursales()

    # Guardar todas las tablas en CSV
    os.makedirs("datos_realistas", exist_ok=True)
    clientes.to_csv("datos_realistas/clientes.csv", index=False)
    productos.to_csv("datos_realistas/productos.csv", index=False)
    ventas.to_csv("datos_realistas/ventas.csv", index=False)
    metodos_pago.to_csv("datos_realistas/metodos_pago.csv", index=False)
    inventario.to_csv("datos_realistas/inventario.csv", index=False)
    proveedores.to_csv("datos_realistas/proveedores.csv", index=False)
    sucursales.to_csv("datos_realistas/sucursales.csv", index=False)

    print("Datos generados, incluyendo la tabla de sucursales, y guardados en la carpeta 'datos_realistas'.")

# Llamar a la función principal
crear_datos_con_sucursales()

# Crear las tablas y guardarlas como CSV
def crear_datos_realistas():
    clientes = generar_tabla_clientes()
    productos = generar_tabla_productos()
    ventas = generar_tabla_ventas(clientes, productos)
    metodos_pago = generar_tabla_metodos_pago()
    inventario = generar_tabla_inventario(productos)
    proveedores = generar_tabla_proveedores(productos)

    os.makedirs("datos_realistas", exist_ok=True)
    clientes.to_csv("datos_realistas/clientes.csv", index=False)
    productos.to_csv("datos_realistas/productos.csv", index=False)
    ventas.to_csv("datos_realistas/ventas.csv", index=False)
    metodos_pago.to_csv("datos_realistas/metodos_pago.csv", index=False)
    inventario.to_csv("datos_realistas/inventario.csv", index=False)
    proveedores.to_csv("datos_realistas/proveedores.csv", index=False)

    print("Datos generados y guardados en la carpeta 'datos_realistas'.")

# Ejecutar la función
crear_datos_realistas()