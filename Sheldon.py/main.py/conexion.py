import mysql.connector

def guardar_reserva_en_db(fecha_ingreso, fecha_salida, nombre, telefono, email, tipo_habitacion, total, id_usuario, id_habitacion):
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="hotelsheldonmsql"
    )
    cursor = conexion.cursor()

    # Asegúrate de que la consulta SQL tenga el mismo número de %s que de valores
    consulta = """
        INSERT INTO reservas (fecha_ingreso, fecha_salida, nombre, telefono, email, tipo_habitacion, total, id_usuario, id_habitacion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (fecha_ingreso, fecha_salida, nombre, telefono, email, tipo_habitacion, total, id_usuario, id_habitacion)

    # Imprime la consulta y los valores para depuración
    print("Consulta:", consulta)
    print("Valores:", valores)

    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
