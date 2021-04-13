from GrupoAceptado_TP1_V5 import lex

Terminales = [
	"puntoYComa",
	"dosPuntosIgual",
	"si",
	"entonces",
	"sino",
	"mientras",
	"hacer",
	"op",
	"corcheteAbierto",
	"corcheteCerrado",
	"parentesisAbierto",
	"parentesisCerrado",
	"aceptar",
	"mostrar",
	"coma",
	"literal",
	]

NoTerminales = [
	'PROGRAMA',
	'DECLARACION',
	'DECLARACION2',
	'SENTENCIA',
	'SENTENCIA2',
	'EXPRESION',
	'EXPRESION2',
	'LISTAIDENTIFICADORES',
	] 

#Eliminamos la recursion por la izquierda inmediata 
Producciones = {
	'PROGRAMA' : [				
		['DECLARACION', 'puntoYComa', 'SENTENCIA'],
		['SENTENCIA'],
	],

 	'DECLARACION' : [	
		['SENTENCIA','DECLARACION2'],
	],

	'DECLARACION2' : [
		['puntoYComa','DECLARACION','DECLARACION2'],
		[],
	],

	'SENTENCIA': [
		['si','EXPRESION','entonces','SENTENCIA','sino','SENTENCIA','SENTENCIA2'],
		['si','EXPRESION','entonces','SENTENCIA', 'SENTENCIA2'],
		['mientras', 'EXPRESION','hacer','SENTENCIA','SENTENCIA2'],
		['literal', 'dosPuntosIgual', 'EXPRESION', 'SENTENCIA2'],
	],

	'SENTENCIA2' : [
		['puntoYComa','SENTENCIA','SENTENCIA2'],
		[],
	],

	'EXPRESION': [	
		['aceptar','literal','op','EXPRESION2'],
		['mostrar','literal','LISTAIDENTIFICADORES','EXPRESION2'],							
		['op','EXPRESION2'],
		['literal','EXPRESION2'],
	],
 
	'EXPRESION2': [
		['op','EXPRESION','EXPRESION2'],
		['corcheteAbierto','EXPRESION','corcheteCerrado','EXPRESION2'],
		['parentesisAbierto','EXPRESION','parentesisCerrado','EXPRESION2'],
		[],
	], 

	'LISTAIDENTIFICADORES': [
		['op'],
		['op','coma','LISTAIDENTIFICADORES'],
	]
}	

def parser(cadena): 
	estado = { 
		'error' : False , 
		'tokens' : lex(cadena), 
		'index' : 0
	}
				
	def pni(noTerminal): #Expande el no terminal por cada una de las formas de reescribirlo. 
	
		for produccion in Producciones[noTerminal]:
			pivote_de_backtracking = estado['index'] 
		#	print(estado['index'])
			estado['error'] = False 
			procesar(produccion)
			if estado['error'] == False:	
				break
			if estado['error'] == True:
				estado['index'] = pivote_de_backtracking 
 
	def procesar(parteDerecha): 
		for simbolo in parteDerecha:

			if simbolo in Terminales:		
			#tomo el tipo de token (primer elemento de la tupla), ubicado en la lista de tokens, determinado por el indice. 
			
				if simbolo == estado['tokens'][estado['index']][0]: 
					estado['index'] += 1
				#print("------------------>   aceptó", simbolo)
				else:
					estado['error'] = True
					break
			if simbolo in NoTerminales:
				pni(simbolo) 
				if estado['error'] == True:
					break 		

	def parse(): #Si no hubo error y se llegó al final de la cadena podemos asegurar que pertenece al lenguaje generado por la gramática.  
		pni('PROGRAMA')
		token_actual = estado['tokens'][estado['index']]
		tipo_token_actual = token_actual[0]
		if estado['error'] == False and tipo_token_actual == 'EOF':
			return True
		else:
			return False

	return parse()

print('--------------------------------------------------------------------------------------------------------------------------------------------')
	
casos_de_prueba = [ ("si 100 > numero entonces value1 := False",True),
					("var := ventas + bonus",True), 
					("mayor := numero1 > numero2",True),
					("mientras longitud < 7 hacer senial := 1",True),
					("si cantAlumnos > 50 entonces aula := magna sino aula := aula1",True),
					("(x : xs)",False),
					("numeros  1000 + 0.5 ",False),
					("SINO SI 'Eve' 'Romi' == ACEPTAR 'Nanu' Fran",False),
					("hoy const = 2 mientras",False),
					("sino 527 ('cama' ('gaseosa')) puff Campana := 07",False)
					]

for (test_input,resultado_esperado) in casos_de_prueba:
    resultado = parser(test_input)
    assert resultado == resultado_esperado  
