import csv


def guardar_csv(ventas, archivo="ventas.csv"):
    # Guarda kis datos en "ventas" o en el archivo especificado en formato CSV.

    if not ventas:  # Lista vacia, se detiene la funcion
        print("No hay datos para guardar.")
        return
    try:
        with open(archivo, mode="w", newline="", encoding="utf-8") as base:

            columnas = ["Producto", "Cantidad", "Precio", "Cliente", "Fecha"]
            writer = csv.DictWriter(base, fieldnames=columnas)

            writer.writeheader()
            writer.writerows(ventas)

            print(f"Archivo {archivo} creado y datos guardados.")

        with open(archivo, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for venta in ventas:
                writer.writerow(venta.values())  # Escribir datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")


def ingresar_ventas(ventas):
    # Función para ingresar datos de ventas desde la consola
    while True:
        try:
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio del producto: "))
            cliente = input("Ingrese el nombre del cliente: ")
            # fecha se geenera automaticamente con la fecha actual
            fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
            # fecha se geenera automaticamente con la funcion date.today()
            # fecha = date.today().isoformat()

            if cantidad < 0 or precio < 0:
                print(
                    "❌ ERROR: Cantidad y Precio deben ser números positivos. Por favor, intente de nuevo."
                )
                continue

            venta = {
                "Producto": producto,
                "Cantidad": cantidad,
                "Precio": precio,
                "Cliente": cliente,
                "Fecha": fecha,
            }

            ventas.append(venta)

            continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
            if continuar != "s":
                guardar_csv(ventas)
                break

        except ValueError:
            print(
                "❌ ERROR: Cantidad y Precio deben ser números enteros o decimales. Por favor, intente de nuevo."
            )
            continue
        except Exception as e:
            print(f"❌ Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue

    return {
        "Producto": producto,
        "Cantidad": cantidad,
        "Precio": precio,
        "Cliente": cliente,
        "Fecha": fecha,
    }


if __name__ == "__main__":
    # Ejemplo de uso
    ventas_ejemplo = [
        {
            "Producto": "Laptop",
            "Cantidad": 2,
            "Precio": 1200,
            "Cliente": "Juan Perez",
            "Fecha": "2024-01-15",
        },
        {
            "Producto": "Mouse",
            "Cantidad": 5,
            "Precio": 25,
            "Cliente": "Ana Gomez",
            "Fecha": "2024-01-16",
        },
    ]
    ingresar_ventas(ventas_ejemplo)
