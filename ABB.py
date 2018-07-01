class Contacto:
  def __init__(self, Nombre, Apellido, Telefono, Email):
    self.nombre = Nombre
    self.apellido = Apellido
    self.telefono = Telefono
    self.email = Email
    self.left = None
    self.right = None
    self.parent = None

class ABB:
  def __init__(self):
    self.root = None
  
  def empty(self):
    return self.root == None
  
  def _insert(self, Contact, node):
    if ord(Contact.apellido[0]) < ord(node.apellido[0]):
      if node.left == None :
        node.left = Contact
        node.left.parent = node
      
      else:
        self._insert(Contact, node.left)
    
    elif ord(Contact.apellido[0]) > ord(node.apellido[0]):
      if node.right == None:
        node.right = Contact
        node.right.parent = node
      else:
        self._insert(Contact, node.right)
    
    else:
      print("Error, intente con otro contacto")

  def insertContact(self, Contact):
    if self.empty():
      self.root = Contact
    else:
      self._insert(Contact, self.root)
  
  def _find(self, Contact, node):
     
    if node == None:
      return None
    elif Contact.apellido == node.apellido :
      return node
    elif ord(Contact.apellido[0]) < ord(node.apellido[0]) and node.left != None:
      return self._find(Contact, node.left)
    elif ord(Contact.apellido[0]) > ord(node.apellido[0]) and node.right != None:
      return self._find(Contact, node.right)
  
  def find(self, Contact):
    if self.empty():
      return None
    else:
      return self._find(Contact, self.root)
    
  def delete(self, Contact):
    if self.empty():
      return None
    return self.deleteContact(self.find(Contact))
  
  def deleteContact(self, node):
    def min_value_node(n):
      current = n
      while current.left != None:
        current = current.left
      return current
    def number_children(n):
      number_children = 0
      if n.left != None:
        number_children += 1
      if n.right != None:
        number_children += 1
      return number_children

    node_parent = node.parent
    node_children = number_children(node)

    if node_children == 0 :
      if node_parent.left == node:
        node_parent.left = None
      else:
        node_parent.right = None

    if node_children == 1:
      if node.left != None:
        child = node.left
      else:
        child = node.right

      if node_parent.left == node:
        node_parent.left = child 

      else:
        node_parent.rigth = child  

      child.parent = node_parent

    if node_children == 2:
      successor = min_value_node(node.right)
      node = successor
      self.deleteContact(successor)
  
  def imprimirContact(self, Contact):
    if self.empty():
      return None
    contacto = self.find(Contact)
    print("Nombre: " + contacto.nombre)
    print("Apellido: " + contacto.apellido)
    print("Telefono: " + contacto.telefono)
    print("Email: " + contacto.email)

  def InOrder(self, node):
    if node == None:
      pass
    else:
      self.InOrder(node.left)
      print(node.nombre +" "+ node.apellido)
      self.InOrder(node.right)
  
  def imprimirAll(self):
    if self.empty():
      print("Carpeta vacia")
    else:
      self.InOrder(self.root)


