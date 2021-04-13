# Parser
<h2>Objetivo</h2>
<p>
 Implementar un analizador sintáctico descendente para una gramática especificada.
</p>
<h2>Enunciado</h2>
<p>
El tipo de ASDR deberá ser implementado mediante procedimientos, esto es, deberá haber
un procedimiento Principal, un procedimiento Procesar y luego un procedimiento
por cada no terminal de la gramática.
El programa que resulte de la implementación deberá aceptar una cadena y luego
indicar si dicha cadena pertenece al lenguaje generado por la grmática y además
deberá indicar qué producciones de la gramática deben ser usadas para derivar la
cadena de entrada.
</p>
<h2>Gramática</h2>
<p>
El símbolo distinguido es Programa.
Los terminales se hallan entre “ ”, por ejemplo “var” es un terminal llamado var .
Los no terminales no se hallan entre “ ” y siempre comienzan en mayúsculas,
pudiendo contener mayúsculas intermedias para aclarar su significado.
Terminales y No Terminales se hallan separados por espacios en blanco para
claridad de la gramática.
</p>
<h2>Gramática Sintáctica</h2>
<p>
Programa → Declaracion “;” Sentencia
  <br>
| Sentencia
  <br>
Declaracion → Declaracion “;” Declaracion
  <br>
| Sentencia
Sentencia → Sentencia “;” Sentencia
  <br>
| Identificador “:=” Expresion
  <br>
| ”si” Expresion “entonces“ Sentencia “sino” Sentencia
  <br>
| ”si” Expresion “entonces“ Sentencia
  <br>
| “mientras” Expresion “hacer” Sentencia
  <br>
Expresion → Literal
  <br>
| Numero
  <br>
| Identificador
  <br>
| Expresion Op Expresion
  <br>
| Expresion “[“ Expresion ”]”
  <br>
| Expresion “(“ Expresion ”)”
  <br>
| “aceptar” Literal Identificador
  <br>
| “mostrar” Literal ListaIdentificadores
  <br>
ListaIdentificadores → Identificador
  <br>
| Identificador “,” ListaIdentificadores
</p>
<h2>Gramática Léxica</h2>
<p>
Op → Relop
  <br>
| Mulop
    <br>
| Sumop
    <br>
Relop → “== “| “>” |”<” | “>=” | “<= “ | “!=”
                                       <br>
Mulop → “*“| “/” |”mod” | “and”
    <br>
Sumop → “+“| “-” |”or”
    <br>
Numero → ListaDigito
    <br>
| ListaDigito "." ListaDigito
    <br>
ListaDigito → Digito
    <br>
| Digito ListaDigito
    <br>
Literal → “’” ListaSimbolos “’”
    <br>
Identificador → Letra
    <br>
| Letra ListaSimbolos
    <br>
ListaSimbolos → Letra
    <br>
| Digito
    <br>
| Letra ListaSimbolos
    <br>
| Digito ListaSimbolos
    <br>
Letra → “a”| ... |“z” | “A”| ... |“Z”
    <br>
Digito → “0”| ... |“9”
</p>
