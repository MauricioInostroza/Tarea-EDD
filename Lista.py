class Contacto:
  def __init__(self, Nombre, Apellido, Telefono, Email):
    self.nombre = Nombre
    self.apellido = Apellido
    self.telefono = Telefono
    self.email = Email
    self.next = None
  
class List:
  def __init__(self):
    self.head = None

  def empty(self): 
    return (self.head == None)

  def insertContact(self, Contact):
    if self.empty():
      self.head = Contact
    
    else:
      
      if ord(self.head.apellido[0]) >= ord(Contact.apellido[0]):
        Contact.next = self.head
        self.head = Contact
        
      else:
        aux = self.head
        while aux.next :
          if ord(aux.next.apellido[0]) >= ord(Contact.apellido[0]):
            Contact.next = aux.next
            aux.next = Contact
            break

          aux = aux.next
      
        aux.next = Contact
  
  def findContact(self, Contact): 
    aux = self.head

    while(aux.next):

      if Contact.nombre == aux.nombre and Contact.apellido == aux.apellido :
        return (aux)

      aux = aux.next

  def deleteContact(self, Contact):
    aux = self.findContact(Contact)
    aux.next = Contact.next

  def imprimirContact(self, Contact):
    contacto = self.findContact(Contact)
    print("Nombre: " + contacto.nombre)
    print("Apellido: " + contacto.apellido)
    print("Telefono: " + contacto.telefono)
    print("Email: " + contacto.email)

  def imprimirAll(self):
    if self.empty():
      print ("No existen contactos")
    
    else:
      aux = self.head
      while aux.next :
        print(aux.nombre +" "+ aux.apellido)
        aux = aux.next
      print(aux.nombre +" "+ aux.apellido)



