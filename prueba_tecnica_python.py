
"""
a)	Escribir una función en Python que recorra los datos y agrupe los productos mediante su Ean en el siguiente arreglo de diccionarios 
[{
	“Ean”: [
		{
			“nombre producto (asumir que los productos con mismo Ean tienen el mismo nombre)”,
            "ultimo menor precio"
            "SKU"
            "mercado"
			“cantidad de markets diferentes”,
			“rango de precios (Mayor precio - Menor precio)”
},
]
},] 

"""

datos = [
    {'Ean': '111', 'nombre producto': 'Producto A', 'ultimo menor precio': 100,'mercado': 'Market1', 'SKU': 34353},
    {'Ean': '222', 'nombre producto': 'Producto B', 'ultimo menor precio': 60, 'mercado': 'Market2', 'SKU': 345645},
    {'Ean': '111', 'nombre producto': 'Producto A', 'ultimo menor precio': 50, 'mercado': 'Market4', 'SKU': 75754},
    {'Ean': '333', 'nombre producto': 'Producto D', 'ultimo menor precio': 30, 'mercado': 'Market1', 'SKU': 875565}
]

from collections import defaultdict

def agrupar_productos (datos):

    arreglo_productos = defaultdict(list)

    for producto in datos:
        ean = producto['Ean']
        nombre_producto = producto['nombre producto']
        precio = producto['ultimo menor precio']
        market = producto['mercado']
        sku = producto['SKU']
        

        if ean not in arreglo_productos:
            arreglo_productos[ean].append({
                'nombre producto': nombre_producto,
                'ultimo menor precio': [precio],
                'SKU':sku,
                'cantidad mercado':[market]
            })

        else: 
            producto_existe=0
            for dato in arreglo_productos[ean]:
                if dato['nombre producto'] == nombre_producto:
                    dato['ultimo menor precio'].append(precio)
                    dato['cantidad mercado'].append(market)
                    producto_existe=1
                    break

            if not producto_existe:
                arreglo_productos[ean].append({
                    'nombre producto': nombre_producto,
                    'ultimo menor precio': [precio],
                    'SKU': sku,
                    'cantidad mercado': {market}
                })
                    
        
    resultado = [ 
            {
                    k:[
                    {'nombre producto':v[0]['nombre producto'],
                    'ultimo menor precio':v[0]['ultimo menor precio'],
                    'SKU':v[0]['SKU'],
                    'cantidad mercado':len(set(v[0]['cantidad mercado'])),
                    'Rango precios': str(min(v[0]['ultimo menor precio'])) + "-" + str(max(v[0]['ultimo menor precio']))
                    }]
            }for k,v in arreglo_productos.items()

                ]    
    return resultado
    
resultado = agrupar_productos(datos)
print(resultado)
 


