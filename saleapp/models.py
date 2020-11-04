from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db



class Category(db.Model):
    __tablename__ = "cate"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False)
    products = relationship('Product.id', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id, nullalble=False))

    def __str__(self):
        return self.name

if __name__ == '__main__':
   db.create_all()
