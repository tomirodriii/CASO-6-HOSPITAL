import re
import datetime


def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre) is not None


def validar_apellido(apellido):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", apellido) is not None


def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()


def validar_telefono(telefono):
    return len(telefono) >= 10 and telefono.isdigit()


def validar_fecha(fecha_texto):
    try:
        fecha = datetime.datetime.strptime(
            fecha_texto,
            "%Y-%m-%d"
        ).date()

        if fecha > datetime.date.today():
            return False

        return True

    except ValueError:
        return False