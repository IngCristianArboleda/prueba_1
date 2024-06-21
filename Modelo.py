class Modelo:
    def __init__(self,correo,contrasena,plataforma):
        #self._usuario=usuario
        self._correo = correo
        self._contrasena=contrasena
        self._plataforma=plataforma


    #@property
    #def usuario(self):
        #return self._usuario

    #@usuario.setter
    #def usuario(self,usuario):
        #self._usuario=usuario


    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self,contrasena):
        self._contrasena=contrasena


    @property
    def plataforma(self):
        return self._plataforma

    @plataforma.setter
    def plataforma(self,plataforma):
        self._plataforma=plataforma

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self,correo):
        self._correo=correo






