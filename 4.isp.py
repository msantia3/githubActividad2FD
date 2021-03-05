import abc
from abc import ABCMeta, abstractmethod

class IAve():
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def comer(self):
        pass

class IAveVoladora():
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def volar(self):
        pass

class IAveNadadora():
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def nadar(self):
        pass

class Loro(IAve, IAveVoladora):
  def volar(self):
    return 'Loro volando' 
    pass

  def comer(self):
    return 'Loro comiendo' 
    pass

class Pinguino(IAve, IAveNadadora):

  def nadar(self):
    return 'Pinguino nadando' 
    pass

  def comer(self):
    return 'Pinguino comiendo' 
    pass

if __name__ == '__main__':
    print(Loro().comer())
    print(Pinguino().comer())
    print(Loro().volar())
    print(Pinguino().nadar())
