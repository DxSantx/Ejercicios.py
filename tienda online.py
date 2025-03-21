productos = [{"id": "001", "nombre": "Azucar", "precio": "$40", "stock": "31"},
             {"id": "002", "nombre": "Sal", "precio": "$35", "stock": "32"},
             {"id": "003", "nombre": "Pimienta", "precio": "$25", "stock": "37"}]
pedidos = [{"id_pedido": "001", "productoSolicitado": "Azucar", "estado": "entregado"},
           {"id_pedido": "002", "productoSolicitado": "Sal", "estado": "pendiente"}]
clientesRegistrados = [{"nombre": "Santiago", "Email": "santiafjs@gmail.com", "direccion": "calle 20 #6"},
                       {"nombre": "Samuel", "Email": "samuelfjs@gmail.com", "direccion": "calle 2 #63"}]

#agregar nuevo producto
nuevo_producto = {
    "id": "004", "nombre": "Oregano", "precio": "16", "stock": "87" 
}
productos.append(nuevo_producto)

#cambiar el estado
for pedido in pedidos:
    if pedido["productoSolicitado"] == "Sal":
        pedido["estado"] = "entregado"
print(f"productos: {productos} \npedidos:{pedidos} \nclientes registrados: {clientesRegistrados}")