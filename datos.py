class datos:

    def __init__(self, fecha, usuario, afectado, error):
        self.fecha = fecha
        self.usuario = usuario
        self.afectado = afectado
        self.error = error

    def get_fecha(self):
        return self.fecha

    def get_usuario(self):
        return self.usuario

    def get_afectado(self):
        return self.afectado

    def get_error(self):
        return self.error

    def set_fecha(self, dato):
        self.fecha = dato

    def set_usuario(self, dato):
        self.usuario = dato
    
    def set_afectado(self, dato):
        self.afectado = dato

    def set_error(self, dato):
        self.error = dato