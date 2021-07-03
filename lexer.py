#Se declaran los posibles resultados que pueden devolver los autómatas. 
#Trampa: si la cadena no pertenece a la gramática, 
#Aceptado: si la cadena pertenece a la gramática y 
#No Aceptado: si parte de la cadena pertenece pero no completa.

RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_ACEPTADO = "RESULTADO_ACEPTADO"
RESULTADO_NO_ACEPTADO = "RESULTADO_NO_ACEPTADO" 
ESTADO_TRAMPA = -1

# Se Define cada automata por cada terminal que me pide la gramática.
# Se cuenta con dos tipos de gramáticas, una Lexica y una Sintáctica.

def automata_puntoYComa (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == ';':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_dosPuntosIgual (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == ':':
            estado = 1
        elif estado == 1 and caracter == '=':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
     
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_si (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == 's':
            estado = 1
        elif estado == 1 and caracter == 'i':
            estado= 1
        else:
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_entonces (cadena):
    estado = 0
    final = 7

    for caracter in cadena:
        if estado == 0 and caracter == 'e':
            estado = 1
        elif estado == 1 and caracter == 'n':
            estado = 2
        elif estado == 2 and caracter == 't':
            estado = 3
        elif estado == 3 and caracter == 'o':
            estado = 4
        elif estado == 4 and caracter == 'n':
            estado = 5
        elif estado == 5 and caracter == 'c':
            estado = 6
        elif estado == 6 and caracter == 'e':
            estado = 7
        elif estado == 7 and caracter == 's':
            estado = 7  
        else:
            estado = ESTADO_TRAMPA
            break 

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO
        
def automata_sino (cadena):
    estado = 0
    final = 4

    for caracter in cadena:
        if estado == 0 and caracter == 's':
            estado = 1
        elif estado == 1 and caracter == 'i':
            estado = 2
        elif estado == 2 and caracter == 'n':
            estado = 3
        elif estado == 3 and caracter == 'o':
            estado = 4
        else:
            estado = ESTADO_TRAMPA
            break 

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_mientras (cadena):
    estado = 0
    final = 7

    for caracter in cadena:
        if estado == 0 and caracter == 'm':
            estado = 1
        elif estado == 1 and caracter == 'i':
            estado = 2
        elif estado == 2 and caracter == 'e':
            estado = 3
        elif estado == 3 and caracter == 'n':
            estado = 4
        elif estado == 4 and caracter == 't':
            estado = 5
        elif estado == 5 and caracter == 'r':
            estado = 6
        elif estado == 6 and caracter == 'a':
             estado = 7
        elif estado == 7 and caracter == 's':
            estado = 7
        else:
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_hacer (cadena):
    estado = 0
    final = 4

    for caracter in cadena:
        if estado == 0 and caracter == 'h':
            estado = 1
        elif estado == 1 and caracter == 'a':
            estado= 2
        elif estado == 2 and caracter == 'c':
            estado= 3
        elif estado == 3 and caracter == 'e':
            estado= 4
        elif estado == 4 and caracter == 'r':
            estado= 4
        else :
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#El autómata op integra todos aquellos terminales que pertenecen a la gramática léxica. 
#Inicia en el estado 0 y cuenta con 13 estados finales.

def automata_op (cadena): #Definicion del automata.
    estado = 0
    finales = [2,3,4,5,6,7,9,10,11,14,15,17,20] #Estados finales.
    
     #Recorre la cadena caracter a caracter comprobando si el estado que alcanza es final o no.

    for caracter in cadena:  #Usamos el ciclo for para iterar sobre la cadena y evaluar cada caracter.
        if estado == 0 and caracter == '=':
            estado = 1
        elif estado == 1 and caracter == '=':
            estado = 2
        elif estado == 0 and caracter == '>':
            estado = 3
        elif estado == 3 and caracter == '=':
            estado = 4
        elif estado == 0 and caracter == '<':
            estado = 5
        elif estado == 5 and caracter == '=':
            estado = 6
        elif estado == 0 and caracter == '+':
            estado = 7
        elif estado == 0 and caracter == '!':
            estado = 8
        elif estado == 8 and caracter == '=':
            estado = 9
        elif estado == 0 and caracter == '*':
            estado = 10
        elif estado == 0 and caracter == '/':
            estado = 11
        elif estado == 0 and caracter == 'm':
            estado = 12
        elif estado == 12 and caracter == 'o':
            estado = 13
        elif estado == 13 and caracter == 'd':
            estado = 14
        elif estado == 0 and caracter == '-':
            estado = 15
        elif estado == 0 and caracter == 'o':
            estado = 16
        elif estado == 16 and caracter == 'r':
            estado = 17
        elif estado == 0 and caracter == 'a':
            estado = 18
        elif estado == 18 and caracter == 'n':
            estado = 19 
        elif estado == 19 and caracter == 'd':
            estado = 20
        else: 
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA: #Retorna el resultado de la comparación realizada.
        return RESULTADO_TRAMPA
    elif estado in finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_corcheteAbierto (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == '[':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
        
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_corcheteCerrado (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == ']':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
        
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_parentesisAbierto (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == '(':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
        
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO
         
def automata_parentesisCerrado (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == ')':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
        
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO
    
def automata_aceptar (cadena):
    estado = 0
    final = 7

    for caracter in cadena:
        if estado == 0 and caracter == 'a':
            estado = 1
        elif estado == 1 and caracter == 'c':
            estado = 2
        elif estado == 2 and caracter == 'e':
            estado = 3
        elif estado == 3 and caracter == 'p':
            estado = 4
        elif estado == 4 and caracter == 't':
            estado = 5
        elif estado == 5 and caracter == 'a':
            estado = 6
        elif estado == 6 and caracter == 'r':
            estado = 7
        else:
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_mostrar (cadena):
    estado = 0
    final = 7

    for caracter in cadena:
        if estado == 0 and caracter == 'm':
            estado = 1
        elif estado == 1 and caracter == 'o':
            estado = 2
        elif estado == 2 and caracter == 's':
            estado = 3
        elif estado == 3 and caracter == 't':
            estado = 4
        elif estado == 4 and caracter == 'r':
            estado = 5
        elif estado == 5 and caracter == 'a':
            estado = 6
        elif estado == 6 and caracter == 'r':
            estado = 7
        else :
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO
       
def automata_coma (cadena):
    estado = 0
    final = 1

    for caracter in cadena:
        if estado == 0 and caracter == ',':
            estado = 1
        else:
            estado = ESTADO_TRAMPA
            break
        
    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado == final:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

def automata_literal (cadena): #Se define el autómata literal cuya función es aceptar cadenas alfanuméricas.
    estado = 0
    finales = [1,2,3,4,6,7]

    for c in cadena:
        if estado == 0 and c.isalpha():
            estado = 1 
        elif estado == 1 and c.isdigit(): #Funcion isdigit que me permite saber si el caracter es de tipo digito.
            estado = 3
        elif estado == 1 and c.isalpha():
            estado = 2
        elif estado == 2 and c.isalpha(): #Funcion isalpha que me permite saber si pertenece a un caracter tipo alfabeto.
            estado = 2
        elif estado == 2 and c.isdigit():
            estado = 3
        elif estado == 0 and c.isdigit():
            estado = 3
        elif estado == 3 and c.isdigit():
            estado = 4
        elif estado == 4 and c == '.': #El punto se tiene en cuenta para que el autómata pueda leer números decimales.
            estado = 5
        elif estado == 3 and c == '.':
            estado = 5
        elif estado == 4 and c.isdigit():
            estado = 4
        elif estado == 4 and c.isalpha():
            estado = 2
        elif estado == 5 and c.isdigit():
            estado = 6
        elif estado == 6 and c == '.':
            estado = 5
        elif estado == 6 and c.isdigit():
            estado = 6
        elif estado == 6 and c.isalpha():
            estado = 7
        elif estado == 7 and c.isalpha():
            estado = 7
        elif estado == 7 and c.isdigit():
            estado = 6
        else:
            estado = ESTADO_TRAMPA
            break

    if estado == ESTADO_TRAMPA:
        return RESULTADO_TRAMPA
    elif estado in finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#Lista de tokens con los tipos de tokens asociados con cada automata.
#"Tokenizamos" las cadenas.

TokenType = [
                 ("puntoYComa", automata_puntoYComa),
                 ("dosPuntosIgual", automata_dosPuntosIgual),
                 ("si", automata_si),
                 ("entonces", automata_entonces),
                 ("sino", automata_sino),
                 ("mientras", automata_mientras),
                 ("hacer", automata_hacer),
                 ("op" , automata_op),
                 ("corcheteAbierto ", automata_corcheteAbierto),
                 ("corcheteCerrado ", automata_corcheteCerrado),
                 ("parentesisAbierto ", automata_parentesisAbierto),
                 ("parentesisCerrado", automata_parentesisCerrado), 
                 ("aceptar", automata_aceptar),
                 ("mostrar", automata_mostrar),
                 ("coma", automata_coma),
                 ("literal", automata_literal)
                ]              

def calcCandidato(cadena):  #Verifica los tipos de tokens de la cadena que ingreso.
    allTrapped = True
    candidatos = []
    for tipoToken, automata in TokenType:
        if automata(cadena) == RESULTADO_ACEPTADO:
            allTrapped = False
            candidatos.append(tipoToken)
        if automata(cadena) == RESULTADO_NO_ACEPTADO:
            allTrapped = False
    return (allTrapped, candidatos) 

#Devuelve una tupla cuyo primer elemento indica si los estados son o no todos trampas,
#el segundo elemento me enlista los tipos de tokens correspondientes a la gramática.

def lex(cadena):  
    cadena = cadena + " "  #Agregamos un espacio al final para facilitar la condicion de corte.
    indice = 0
    tokens = []

    while indice < len(cadena): #Se utiliza ciclo mientras para establecer una condicion de corte mientras recorre la cadena.
        caracter = cadena[indice]
        if cadena[indice].isspace(): #Usamos isspace para saber si el primer caracter es o no un espacio en blanco.
            indice += 1
            continue
        candidatos = []
        start = indice
        lexeme = ""
        while True: #Produce un loop hasta que la cadena sea aceptada o no aceptada, es decir que no es trampa.
            next = calcCandidato(cadena[start:indice + 1]) #Transfiero el resultado que me devuelve la función.
            if next[0]: #Toma el primer elemento de la tupla que me devuelve la función.
                break
            candidatos = next[1] #Toma el segundo elemento de la tupla que me devuelve la función.
            indice += 1

        if len(candidatos) == 0: #La longitud de candidatos es 0 cuando la cadena no fue aceptada por ningún automata.
            return ('Error de token',caracter) #Si la cadena no pertenece a la gramática, retorna un error.
        else:
            tipoToken = candidatos[0]
            lexeme = cadena[start : indice]
            tokens.append((tipoToken, lexeme)) #Agrega la tupla a la lista de tokens.     
    tokens.append(("EOF", "EOF")) 
    return tokens 

casos_de_prueba = [
                    ('5+5', [('literal', '5'), ('op', '+'), ('literal', '5'), ('EOF', 'EOF')]),
                    ('¿', ('Error de token', '¿')),
                    ('21 != 22', [('literal', '21'),('op', '!='),('literal', '22'), ('EOF', 'EOF')]),
                    ('si llueve entonces salimos,sino no salimos', [('si', 'si'), ('literal', 'llueve'), ('entonces', 'entonces'), ('literal', 'salimos'), ('coma', ','), ('sino', 'sino'), ('literal', 'no'), ('literal', 'salimos'), ('EOF', 'EOF')]),
                    ('hacer [(11+22)*2]-6/1.5', [('hacer', 'hacer'), ('corcheteAbierto ', '['), ('parentesisAbierto ', '('), ('literal', '11'), ('op', '+'), ('literal', '22'), ('parentesisCerrado', ')'), ('op', '*'), ('literal', '2'), ('corcheteCerrado ', ']'), ('op', '-'), ('literal', '6'), ('op', '/'), ('literal', '1.5'), ('EOF', 'EOF')]),
                    ('aceptar y mostrar; 0>=X<=1', [('aceptar', 'aceptar'), ('literal', 'y'), ('mostrar', 'mostrar'), ('puntoYComa', ';'), ('literal', '0'), ('op', '>='), ('literal', 'X'), ('op', '<='), ('literal', '1'), ('EOF', 'EOF')]),
                    ('Python es mejor := que Pascal', [('literal', 'Python'), ('literal', 'es'), ('literal', 'mejor'), ('dosPuntosIgual', ':='), ('literal', 'que'), ('literal', 'Pascal'), ('EOF', 'EOF')]),
                    ('mientras and estado==-1 entonces trampa', [('mientras', 'mientras'), ('op', 'and'), ('literal', 'estado'), ('op', '=='), ('op', '-'), ('literal', '1'), ('entonces', 'entonces'), ('literal', 'trampa'), ('EOF', 'EOF')]),
                    ('===',('Error de token', '=')),
                    ('franleplant@gmail.com',('Error de token', '@')),
                    ('==!',('Error de token', '!'))
                    ]

#Se realizan los test correspondientes para verificar el funcionamiento del lexer.
#Se utiliza un ciclo for para ir recorriendo todos los casos de pruebas. Evita tener que realizar assert individuales.

for (test_input,resultado_esperado) in casos_de_prueba:
    resultado = lex(test_input)
    assert resultado == resultado_esperado   



