# Напиши класс EmployeeSalary. Он рассчитывает почасовую заработную плату сотрудников за неделю.

class EmployeeSalary:
    hourly_payment = 400  # Переменная, устанавливает почасовой уровень оплаты 
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    # Метод класса для рассчета часов по формуле, если hours неизвестно 
    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8

        return cls(name, hours, rest_days, email)
    
    # Метод класса для генерации email
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    # Метод класса для изменения переменной hourly_payment
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    # Метод расчёта заработной платы
    def salary(self):
        return self.hours * self.hourly_payment
    



    


