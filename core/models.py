from django.db import models
from django.db.models.query_utils import Q
from core.funciones import ModeloBase
from djangoProject import settings

# Create your models here.
class Sexo(ModeloBase):
  nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombre')

  def __str__(self):
    return u'%s' % self.nombre

  class Meta:
    verbose_name = u"Sexo"
    verbose_name_plural = u"Sexos"
    unique_together = ('nombre',)

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Sexo, self).save(*args, **kwargs)

class Pais(ModeloBase):
  nombre = models.CharField(default='', max_length=100, verbose_name=u"Nombre")

  @staticmethod
  def flexbox_query(q, extra=None):
    if extra:
      return eval('Pais.objects.filter(Q(nombre__contains="%s")).filter(%s).distinct()[:25]' % (q, extra))
    return Pais.objects.filter(Q(nombre__contains=q)).distinct()[:25]

  def flexbox_repr(self):
    return self.__str__()

  def __str__(self):
    return u'%s' % self.nombre

  class Meta:
    verbose_name = u"País"
    verbose_name_plural = u"Paises"
    ordering = ['nombre']
    unique_together = ('nombre',)

  def en_uso(self):
    return self.provincia_set.values('id').all().exists()

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Pais, self).save(*args, **kwargs)

class Provincia(ModeloBase):
  pais = models.ForeignKey(Pais, blank=True, null=True, verbose_name=u'País', on_delete=models.CASCADE)
  nombre = models.CharField(default='', max_length=100, verbose_name=u"Nombre")

  @staticmethod
  def flexbox_query(q, extra=None):
    if extra:
      return eval('Provincia.objects.filter(Q(nombre__contains="%s")).filter(%s).distinct()[:25]' % (q, extra))
    return Provincia.objects.filter(Q(nombre__contains=q)).distinct()[:25]

  def flexbox_repr(self):
    return self.__str__()

  def __str__(self):
    return u'%s' % self.nombre

  class Meta:
    verbose_name = u"Provincia"
    verbose_name_plural = u"Provincias"
    ordering = ['nombre']
    unique_together = ('nombre', 'pais')

  def en_uso(self):
    return self.ciudad_set.values('id').all().exists()

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Provincia, self).save(*args, **kwargs)

class Ciudad(ModeloBase):
  provincia = models.ForeignKey(Provincia, blank=True, null=True, verbose_name=u'Provincia', on_delete=models.CASCADE)
  nombre = models.CharField(default='', max_length=100, verbose_name=u"Nombre")

  @staticmethod
  def flexbox_query(q, extra=None):
    if extra:
      return eval('Canton.objects.filter(Q(nombre__contains="%s")).filter(%s).distinct()[:25]' % (q,extra))
    return Ciudad.objects.filter(Q(nombre__contains=q)).distinct()[:25]

  def flexbox_repr(self):
    return self.__str__()

  def __str__(self):
    return u'%s' % self.nombre

  class Meta:
    verbose_name = u"Canton"
    verbose_name_plural = u"Cantones"
    ordering = ['nombre']
    unique_together = ('nombre', 'provincia')


  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Ciudad, self).save(*args, **kwargs)

class Vendedor(ModeloBase):
  class TipoDocumento(models.IntegerChoices):
    NINGUNO = 0, "Ninguno"
    CEDULA = 1, "Cédula"
    PASAPORTE = 2, "Pasaporte"
    RUC = 3, "Ruc"

  tipodocumento = models.IntegerField(choices=TipoDocumento.choices, default=TipoDocumento.NINGUNO, blank=True, null=True,
                                      verbose_name=u"Tipo Documento")
  identificacion = models.CharField(default='', max_length=13, verbose_name=u"Identificación")
  nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombres')
  apellido = models.CharField(default='', max_length=100, verbose_name=u"Apellidos")
  nacimiento = models.DateField(verbose_name=u"Fecha de nacimiento", null=True, blank=True)
  sexo = models.ForeignKey(Sexo, default=2, verbose_name=u'Sexo', on_delete=models.CASCADE)
  email = models.CharField(default='', max_length=200, verbose_name=u"Correo electronico personal")
  pais = models.ForeignKey(Pais, blank=True, null=True, verbose_name=u'País residencia', on_delete=models.SET_NULL)
  provincia = models.ForeignKey(Provincia, blank=True, null=True, verbose_name=u"Provincia de residencia", on_delete=models.SET_NULL)
  ciudad = models.ForeignKey(Ciudad, blank=True, null=True, verbose_name=u"Ciudad de residencia", on_delete=models.SET_NULL)
  direccion = models.CharField(default='', max_length=100, verbose_name=u"Calle principal", null=True, blank=True)
  celular = models.CharField(default='', max_length=50, verbose_name=u"Celular")
  #usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return u'%s %s' % (self.apellido, self.nombre)

  class Meta:
    verbose_name = u"Vendedor"
    verbose_name_plural = u"Vendedores"
    ordering = ['apellido', 'nombre']
    unique_together = ('identificacion',)


class Marca(ModeloBase):
  nombreMarca = models.CharField(default='', max_length=100, verbose_name=u'Marca')

  def __str__(self):
    return u'%s' % self.nombreMarca

  class Meta:
    verbose_name = u"Marca"
    verbose_name_plural = u"Marcas"
    unique_together = ('nombreMarca',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.nombreMarca = self.nombreMarca.upper()
    super(Marca, self).save(*args, **kwargs)

class Panel(ModeloBase):
  nombrePanel = models.CharField(default='', max_length=100, verbose_name=u'Panel')

  def __str__(self):
    return u'%s' % self.nombrePanel

  class Meta:
    verbose_name = u"Panel"
    verbose_name_plural = u"Paneles"
    unique_together = ('nombrePanel',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.nombrePanel = self.nombrePanel.upper()
    super(Panel, self).save(*args, **kwargs)

class Televisor(ModeloBase):
  nombretv = models.CharField(default='Plasma', max_length=15, verbose_name=u'Televisor')
  marca = models.ForeignKey(Marca,blank=True, null=True, default='', verbose_name=u'Marca',on_delete=models.SET_NULL)
  pulgadas = models.CharField(default='', max_length=50, verbose_name=u'Pulgadas')
  tipoPanel = models.ForeignKey(Panel,blank=True, null=True, default='', verbose_name=u'Panel',on_delete=models.SET_NULL)
  resolucion = models.CharField(default='', max_length=50, verbose_name=u'Resolución')
  imagen = models.FileField("Foto", upload_to="core/televisores", blank=True, null=True)
  costo = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0, blank=True, null=True,verbose_name=u"Stock")

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')
  pass

  def __str__(self):
    return u'%s' % self.imagen

#******************************************** Refrigeradora ********************************************************
class MarcaRefri(ModeloBase):
  marcaRefri = models.CharField(default='', max_length=100, verbose_name=u'Marca')

  def __str__(self):
    return u'%s' % self.marcaRefri

  class Meta:
    verbose_name = u"Marca"
    verbose_name_plural = u"Marcas"
    unique_together = ('marcaRefri',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.marcaRefri = self.marcaRefri.upper()
    super(MarcaRefri, self).save(*args, **kwargs)

class ModeloRefri(ModeloBase):
  modeloRefri = models.CharField(default='', max_length=100, verbose_name=u'Modelo')

  def __str__(self):
    return u'%s' % self.modeloRefri

  class Meta:
    verbose_name = u"Modelo"
    verbose_name_plural = u"Modelos"
    unique_together = ('modeloRefri',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.modeloRefri = self.modeloRefri.upper()
    super(ModeloRefri, self).save(*args, **kwargs)

class Color(ModeloBase):
  color = models.CharField(default='', max_length=100, verbose_name=u'Color')

  def __str__(self):
    return u'%s' % self.color

  class Meta:
    verbose_name = u"Color"
    verbose_name_plural = u"Colores"
    unique_together = ('color',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.color.upper()
    super(Color, self).save(*args, **kwargs)

class Refrigeradora(ModeloBase):
  nombrerefrigeradora = models.CharField(default='', max_length=50, verbose_name=u'Televisor')
  refrigeradoramarcaRefri = models.ForeignKey(MarcaRefri,blank=True, null=True, default='', verbose_name=u'Marca',on_delete=models.SET_NULL)
  refrigeradoramodeloRefri = models.ForeignKey(ModeloRefri,default='',blank=True, null=True, verbose_name=u'Modelo',on_delete=models.SET_NULL)
  capacidadLitros = models.IntegerField(default=0, blank=True, null=True,verbose_name=u"Litros")
  dimensiones = models.CharField(default='0x0x0', max_length=50, verbose_name=u'Dimensiones altura*hancho*profundidad')
  refrigeradoraColor = models.ForeignKey(Color,blank=True, null=True, default='', verbose_name=u'Color',on_delete=models.SET_NULL)
  imagen = models.FileField("Foto", upload_to="core/refrigeradora", blank=True, null=True)
  costo = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Stock")

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')


#******************************************** Microondas ********************************************************

class marcaMicroondas(ModeloBase):
  marcaMicroondas = models.CharField(default='', max_length=20, verbose_name=u'Marca')

  def __str__(self):
    return u'%s' % self.marcaMicroondas

  class Meta:
    verbose_name = u"Marca"
    verbose_name_plural = u"Marcas"
    unique_together = ('marcaMicroondas',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.marcaMicroondas.upper()
    super(marcaMicroondas, self).save(*args, **kwargs)


class modeloMicroondas(ModeloBase):
  modelo = models.CharField(default='', max_length=20, verbose_name=u'Modelo')

  def __str__(self):
    return u'%s' % self.modelo

  class Meta:
    verbose_name = u"Modelo"
    verbose_name_plural = u"Modelo"
    unique_together = ('modelo',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.modelo.upper()
    super(modeloMicroondas, self).save(*args, **kwargs)

class Microondas(ModeloBase):
  nombremicroondas = models.CharField(default='', max_length=20, verbose_name='Microondas')
  marcaMicroondas = models.ForeignKey(marcaMicroondas, blank=True, null=True, default='', verbose_name=u'Marca',
                                              on_delete=models.SET_NULL)
  modelo = models.ForeignKey(modeloMicroondas, default='', blank=True, null=True, verbose_name=u'Modelo',
                                               on_delete=models.SET_NULL)
  capacidad = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Capacidad")
  dimensiones = models.CharField(default='0x0x0', max_length=50, verbose_name=u'Dimensiones altura*hancho*profundidad')
  microondasColor = models.ForeignKey(Color, blank=True, null=True, default='', verbose_name=u'Color',
                                         on_delete=models.SET_NULL)
  imagen = models.FileField("Foto", upload_to="core/microondas", blank=True, null=True)
  costo = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Stock")

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')
  pass
