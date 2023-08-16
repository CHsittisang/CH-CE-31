class Account:
    def __init__(self, id, password, status ):
        self.id = id
        self.password = password
        self.status = status

class Admin(Account):
    def __init__(self, id, password, status, name, email, phone):
        super().__init__(id, password, status)
        self.name = name
        self.email = email
        self.phone = phone

class front_desk(Account):
    def __init__(self, id, password, status, name, email, phone):
        super().__init__(id, password, status)
        self.name = name
        self.email = email
        self.phone = phone 

class Customer(Account):
    def __init__(self, id, password, status, name, email, phone,address):
        super().__init__(id, password, status)
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Review(Customer):
    def __init__(self, id, name,comment,rating):
        super().__init__(self, id, name)
        self.comment = comment
        self.rating = rating

class Series_Catalog:
    def __init__(self,last_Update,series,imagre):
        self.last_Update = last_Update
        self.series = series
        self.imagre = imagre

class Book_Catalog:
    def __init__(self,last_Update,series_name,list_book,imagre):
        self.last_Update = last_Update
        self.series_name = series_name
        self.list_book = list_book
        self.imagre = imagre

class Book:
    def __init__(self,book_name,book_id,detail,type,tag,price,imagre,releae_date,number_of_product,author):
        self.book_name = book_name
        self.book_id = book_id
        self.detail = detail
        self.type = type
        self.tag = tag
        self.price = price
        self.imagre = imagre
        self.releae_date = releae_date
        self.number_of_product = number_of_product
        self.author = author

class Cart:
    def __init__(self,list_book,total,imagre,):
        self.list_book = list_book
        self.total = total
        self.imagre = imagre

class Order:
    def __init__(self,list_book,name_customer,address,email,phone,total_price,order_status,Order_id):
        self.list_book = list_book
        self.name_customer = name_customer
        self.address = address
        self.email = email
        self.phone = phone
        self.total_price = total_price
        self.order_status = order_status
        self.Order_id = Order_id

class Order_history(Order):
    def __init__(self,list_book,name_customer,address,email,phone,total_price,order_status,Order_id,date):
        super().__init__(list_book,name_customer,address,email,phone,total_price,order_status,Order_id)
        self.date = date

class Payment:
    def __init__(self,Order_tolal,bank,status):
        self.Order_tolal = Order_tolal
        self.bank = bank
        self.status = status

class Bank:
    def __init__(self,name,id,owner):
        self.name = name
        self.id = id
        self.owner = owner

class Discount_code:
    def __init__(self,code,balance,expire_date):
        self.code = code
        self.balance = balance
        self.expire_date = expire_date

class Shipment(Order):
    def __init__(self,list_book,name_customer,address,email,phone,total_price,order_status,Order_id,shipment_status,shipment_id,shipment_date,shipping_name):
        super().__init__(list_book,name_customer,address,email,phone,total_price,order_status,Order_id)
        self.shipment_status = shipment_status
        self.shipment_id = shipment_id
        self.shipment_date = shipment_date
        self.shipping_name = shipping_name 