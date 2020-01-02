#Herencia
class instrumento:
  instrument='Bateria'
  typeInstrument=''
  def setPrice(self):
    self.price=int(input('Ingrese el valor del instrumento '))

  def showPrice(self):
    print('El valor del instrumento es ',self.price)

  def playInstrument(self):
    print('Ahora suena el instrumento')

  def broken():
    print ('has quebrado el instrumento, sos un rockstar!')

  def material(self):
    self.principalMaterial=input('Digite el material principal del instrumento ')
    self.secundaryMaterial=input('Digite el material Secundario del instrumento ')

  def showMaterial(self):
    print ('El material principal del instrumento es: ', self.principalMaterial)
    print ('El material secundario del instrumento es: ', self.secundaryMaterial)

  def whatsInstrument(self):
    self.typeInstrument=input('digite el tipo de instrumento que desea acustico o electronico ')
    if(self.typeInstrument=='electronica'):
      self.setPrice()
      self.totalPrice=self.price+500
    elif (self.typeInstrument=='acustico'):
      self.setPrice()
      self.material()
      self.totalPrice=self.price+200
    else:
      print ('por favor digite un tipo de instrumento valido. (electronica o acustico)')
      self.whatsInstrument ()

  def setPriceTotal(self):
    print ('el precio total de la ',self.instrument, 'es' , self.totalPrice )




#i=instrumento()
#i.setPrice()
#i.showPrice()
#i.material()

class guitarra (instrumento):
  def __init__(self):
    self.setPrice()

#g=guitarra()

class drums(instrumento):
  def __init__ (self):
    self.whatsInstrument()
    self.setPriceTotal()



d=drums()
