import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, select, and_, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import argparse


baza = create_engine('sqlite:///test.db') 

BazaModel = declarative_base()

class Friend(BazaModel):
    __tablename__= 'friend'
    id = Column(Integer, primary_key = True)
    firstname = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    number = Column(Integer)
    email = Column(String)
    borrower = relationship('Library', backref = 'friend')

class Book(BazaModel):
    __tablename__='book'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)
    borrowed = relationship('Library', backref = 'book')


class Library(BazaModel):
    __tablename__='Library'
    friend_id = Column(Integer, ForeignKey('friend.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)


BazaModel.metadata.create_all(baza)
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()

parser = argparse.ArgumentParser()
'''
parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--add", help="add 1", type=int)
args = parser.parse_args()
print(args.square**2)
print(args.add+1)
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("--add_book", )
parser.add_argument("--title")
parser.add_argument("--author")
parser.add_argument("--year")
parser.add_argument('--add_book',nargs=2,
    metavar=('title','author', 'yaer'),help='help:')
'''
parser.add_argument('--add_book', action='append', nargs='+')
parser.add_argument('--add_friend', action='append', nargs='+')
parser.add_argument('--borrow', action='append', nargs='+')
parser.add_argument('--give_back', action='append', nargs='+')
args = parser.parse_args()
if args.add_book:
    for arg in args.add_book:
        sesja.add(Book(title=arg[0], author=arg[1], year=arg[2]))
if args.add_friend:
    for arg in args.add_friend:
        sesja.add(Friend(firstname=arg[0], surname=arg[1], number=arg[2], email=arg[3]))
if args.borrow:
    for arg in args.borrow:
        s = select([Friend.id]).where(and_(Friend.firstname == arg[0], Friend.surname == arg[1]))
        id_friend = baza.execute(s).scalar()
        s = select([Book.id]).where(and_(Book.title == arg[2], Book.year == arg[3]))
        id_book = baza.execute(s).scalar()
        s = select([Library.book_id]).where(Library.book_id==id_book)
        check = baza.execute(s).scalar()
        if not check:
            sesja.add(Library(friend_id=id_friend, book_id=id_book))
if args.give_back:
    for arg in args.give_back:
        s = select([Friend.id]).where(and_(Friend.firstname == arg[0], Friend.surname == arg[1]))
        id_friend = baza.execute(s).scalar()
        s = select([Book.id]).where(and_(Book.title == arg[2], Book.year == arg[3]))
        id_book = baza.execute(s).scalar()
        query = delete(Library)
        query = query.where(and_(Library.friend_id == id_friend, Library.book_id == id_book))
        baza.execute(query)
    
sesja.commit()
sesja.close()
