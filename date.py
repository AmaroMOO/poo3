from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
     
def es_bisiesto(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validar_fecha(dia, mes, año):

    if año < 1900 or año > 2050:
        año = 1900
    
    if mes < 1 or mes > 12:
        mes = 1
    
    dias_por_mes = [31, 28 if not es_bisiesto(año) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        dia = 1
    
    return dia, mes, año

dia_corregido, mes_corregido, año_corregido = validar_fecha(dia, mes, año)
    print(f"Fecha corregida: {dia_corregido}-{mes_corregido}-{año_corregido}")


    def is_leap_year(year: int) -> bool:
        resultado = False

        if year % 4 == 0 and year % 100 != 0:
            resultado == True
        elif year % 400 == 0:
            resultado == True 

        return resultado

    def days_in_month(month: int, year: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.is_leap_year)(year) and month == 2:
            return 29
        else:
            return days[month-1]

    def get_delta_days(self) -> int:
        import datetime

        dia = int(input("Introduce dia exacto: "))
        mes = int(input("Introduce mes exacto: "))
        año = int(input("Introduce año exacto: "))

        fecha_inicial= datetime.date(1900, 1, 1)
        fecha_introducida= datetime.date(año, mes, dia)

        result= fecha_introducida - fecha_inicial

        print(f'Dias transcurridos {result.days} aproximadamente')

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
       # Asignar numeros a los dias
        if day is domingo:
            print("Dia numero 0")
        if day is lunes:
            print("Dia numero 1")
        if day is martes:
            print("Dia numero 2")
        if day is miercoles:
            print("Dia numero 3")
        if day is jueves:
            print("Dia numero 4")
        if day is viernes:
            print("Dia numero 5")
        if day is sabado:
            print("Dia numero 6")

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
    # Mostrar una fecha en corto
    # Primero mostramos fecha actual
        from datetime import date
        from datetime import datetime

        today = date.today()

        now = datetime.now()

        print(today)
        print(now)

        # Obtener dia, mes, año, hora, mins y segs

        print("El dia actual es {}". format(today.day))
        print("El mes actual es {}". format(today.month))
        print("El año actual es {}". format(today.year))

        # Datetime
        print("El dia actual es {}". format(today.day))
        print("El mes actual es {}". format(today.month))
        print("El año actual es {}". format(today.year))

        print("El hora actual es {}". format(now.hour))
        print("El minuto actual es {}". format(now.minute))
        print("El segundo actual es {}". format(now.second))

        now = datetime.now()
        format = now.strftime('Dia: %d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        print(format)

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
    from datetime import datetime

    fecha_antigua = datetime(2003, 9, 2) 

    print("Fecha exacta de ese dia:", fecha_antigua)


    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
    
    from datetime import datetime, timedelta

    anio = int(input("Ingresa el año de la fecha inicial: "))
    mes = int(input("Ingresa el mes de la fecha inicial: "))
    dia = int(input("Ingresa el día de la fecha inicial: "))

    fecha_inicial = datetime(anio, mes, dia)

    dias_a_sumar = int(input("Ingresa el número de días a sumar: "))

    nueva_fecha = fecha_inicial + timedelta(days=dias_a_sumar)

    print("La nueva fecha es:", nueva_fecha)


    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
       
    from datetime import datetime

    fecha1 = datetime(2024, 3, 20)
    fecha2 = datetime(2023, 3, 20)

    diferencia = fecha1 - fecha2

    print("La diferencia entre las fechas es de:", diferencia, "días")



    from datetime import datetime, timedelta

    fecha_str = input("Ingresa la fecha inicial en formato YYYY-MM-DD: ")

    fecha_inicial = datetime.strptime(fecha_str, '%Y-%m-%d')

    dias_a_restar = int(input("Ingresa el número de días a restar: "))

    nueva_fecha = fecha_inicial - timedelta(days=dias_a_restar)

    print("Nueva fecha después de restar", dias_a_restar, "días:", nueva_fecha.strftime('%Y-%m-%d'))




    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __eq__(self, other) -> bool:
        ...



if __name__ == "__main__":
    pass