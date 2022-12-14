from inventario.producto import Producto
from inventario.stock import Stock
from inventario.excel_exporter import ExcelExporter

def ejecutar():
    stock = Stock()

    prod1 = Producto("p1", "Laptop Lenovo Thinkpad T250", 1450, 20)
    stock.agregar_producto(prod1)

    prod2 = Producto("p2", "Celular Xiaomi Redmi Note 9", 350, 50)
    stock.agregar_producto(prod2)
    
    print(f"El inventario tiene: {stock.productos.__len__()} productos")
    
    exporter = ExcelExporter()
    exporter.exportar(stock, "d:\\inventario_prod.xlsx")
    
    print("Inventario exportado correctamente")
    
if __name__ == "__main__":
    ejecutar()
    
# comentario de Gissella T
# Comentario ingresado por gvillacis
# Comentario ingresado por agatoclesdesiracusa lalala
# Comentario ingresado por Jefferson 
