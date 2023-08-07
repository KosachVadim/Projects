from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Модель для банка
class Bank(Base):

    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    #managers = relationship('Manager', back_populates='bank')
    #clients = relationship('Client', back_populates='bank')


# Модель для менеджера
class Manager(Base):

    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bank_id = Column(String)

    #bank = relationship('Bank', back_populates='managers')


# Модель для клиента
class Client(Base):

    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bank_id = Column(String)
    #bank = relationship('Bank', back_populates='clients')
    accounts = relationship('Account', back_populates='client')


# Модель для счёта
class Account(Base):

    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    type_account = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship('Client', back_populates='accounts')


