def Calculator(input_operation):
    cadena=input_operation
    operacion=""
    operacionArreglo=[]
    operacionVieja=[]
    operacionViejaString=""
    contador=0
    for x in cadena:
        if(x=="(" or operacionArreglo!="" and x!=" "):
            operacionArreglo.append(x)
            if(x=="("):
                operacionVieja=operacionArreglo
                operacionViejaString="".join(operacionVieja)
                operacionArreglo=[]
                operacionArreglo.append(x)
            if ((operacionViejaString.__contains__("/") or operacionViejaString.__contains__("*")) and operacionViejaString.__contains__("**")):
                operacionArreglo = operacionVieja
                break
            if(x==")"):
                break

    for x in operacionArreglo:
        if(x=="*" and operacionArreglo[contador+1]=="*"):
            operacion = operacionArreglo[contador - 1] + operacionArreglo[contador] + operacionArreglo[contador + 1] + operacionArreglo[contador+2]
            break
        if(x=="*" or x=="/"):
            operacion=operacionArreglo[contador-1]+operacionArreglo[contador]+operacionArreglo[contador+1]
        if(not operacionArreglo.__contains__("*") and x=="+" or x=="-"):
            operacion=operacionArreglo[contador-1]+operacionArreglo[contador]+operacionArreglo[contador+1]
        contador=contador+1
    resultado = (eval(cadena), operacion)
    return resultado

input_operation=input()
