from dbset import db  # ใช้ชื่อไฟล์ใหม่ dbset.py
import random

class Cow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), unique=True, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    age_year = db.Column(db.Integer, nullable=False)
    age_month = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Cow {self.code}>'

    
    def calculate_milk(self):
        if self.color == "white":
            total_months = self.age_year * 12 + self.age_month
            milk = max(0, 120 - total_months)
            flavor = "Plain Milk"  # นมจืด
        elif self.color == "brown":
            milk = max(0, 40 - self.age_year)
            flavor = "Chocolate Milk"  # นมช็อกโกแลต
        elif self.color == "pink":
            milk = max(0, 30 - self.age_month)
            flavor = "Strawberry Milk"  # นมสตรอว์เบอร์รี่
        else:
            milk = 0
            flavor = "Unknown"
        
        return milk, flavor
