def registroVacunacion ():
    ans= True
    while ans== True:
        razones= ""
        residencia= input("¿Reside en el distrito de Cali: ?")
        if residencia== "no":
            razones+= ("no es residente de Cali")
            razones+= (", ")
        cedula= input("numero de cedula: ")
        if cedula== "":
            razones+= ("no presento la cedula")
            razones+= (", ")
        vacunacion= input("¿ha sido vacunado contra Covid19 anteriormente? ")
        if vacunacion == "si":
            razones+= ("ya fue vacunado anteriormente contra Covid19")
            razones+= (", ")
        otrasVacunas= input("¿ha sido vacunado contra otro tipo de enfermedades en el ultimo mes? ")
        if otrasVacunas == "si":
            razones+= ("fue vacunado contra otro tipo de enfermedades en el ultimo mes")
            razones+= (", ")
        estado= input("¿ha tenido sintomas de Covid19? o ¿ha tenido Covid19 recientemente? ")
        if estado== "si":
            razones+= ("ha presentado sintomas de Covid19 recientemente ")
        if razones== "":
            print ("“Paciente apto para vacuna Covid19, por favor, siga a la mesa de inscripción”")
        if razones!= "":
            print ("no puede ser vacunado por las siguientes razones: ")
            print (razones)
        ejecucion= input("¿desea continuar o cerrar jornada?")
        if ejecucion == "si":
            ans= True
        else:
            ans= False

# registroVacunacion()

def registroPacientes ():
    vacunados= 0
    citasAsig= 0
    promedio= 0
    ans= True
    while ans== True:
        nombre= input("digite su nombre: ")
        apellidos= input("digite sus apellidos: ")
        edad= int(input("digite su edad: "))
        sexo= input("digite su sexo: ")
        barrio= input("digite el nombre de su barrio: ")
        dosis= input("¿primera o segunda dosis? ")
        eps= input("digite el nombre de su EPS: ")
        cita= input("¿tiene cita para el dia de hoy? si/no: ")
        if cita== "si":
            vacunados+= 1
            promedio+=edad
            print ("gracias por la informacion, le atenderemos en un momento: ")
        else:
            citasAsig+= 1
            print ("cita asignada para el dia de mañana")
        
        ejecucion= input("¿desea continuar o cerrar jornada?")
        if ejecucion == "si":
            ans= True
        else:
            ans= False
    promedio//= (vacunados)
    print ("Cantidad de pacientes Registrados en el dia: ", str(vacunados+citasAsig))
    print ("Cantidad de pacientes vacunados: ",str(vacunados))
    print ("Promedio de edad de pacientes vacunados: ", str(promedio))
    print ("Cantidad de citas para el dia siguiente: ", str(citasAsig))
    


# registroPacientes()