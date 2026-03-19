"""
Модели данных для финансового учета
"""

class Case:
    """Кейс (место хранения денег)"""
    
    def __init__(self, name: str, currency: str, balance: float = 0.0):
        """
        Создание нового кейса
        
        Аргументы:
            name: название кейса (например, "Наличные", "Карта Сбера")
            currency: валюта (RUB, USD, EUR)
            balance: начальный баланс (по умолчанию 0)
        """
        self.name = name
        self.currency = currency.upper()  # Приводим к верхнему регистру
        self.balance = balance
        
    def deposit(self, amount: float) -> float:
        """
        Положить деньги в кейс
        
        Аргументы:
            amount: сумма для внесения
            
        Возвращает:
            Новый баланс
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        """
        Снять деньги из кейса
        
        Аргументы:
            amount: сумма для снятия
            
        Возвращает:
            Новый баланс
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        if amount > self.balance:
            raise ValueError(f"Недостаточно средств. Доступно: {self.balance}")
        
        self.balance -= amount
        return self.balance
    
    def __str__(self) -> str:
        """Красивое отображение кейса"""
        return f"Кейс '{self.name}': {self.balance:.2f} {self.currency}"
    
    def __repr__(self) -> str:
        """Техническое отображение"""
        return f"Case(name='{self.name}', currency='{self.currency}', balance={self.balance})"