"""
Логика работы с кейсами
"""

from src.models import Case

class FinanceManager:
    """Управление финансами"""
    
    def __init__(self):
        self.cases = []  # Список всех кейсов
    
    def create_case(self, name: str, currency: str, initial_balance: float = 0.0) -> Case:
        """
        Создать новый кейс
        """
        # Проверяем, нет ли уже кейса с таким именем
        for case in self.cases:
            if case.name == name:
                raise ValueError(f"Кейс с именем '{name}' уже существует")
        
        new_case = Case(name, currency, initial_balance)
        self.cases.append(new_case)
        return new_case
    
    def get_case(self, name: str) -> Case:
        """
        Найти кейс по имени
        """
        for case in self.cases:
            if case.name == name:
                return case
        raise ValueError(f"Кейс '{name}' не найден")
    
    def transfer(self, from_name: str, to_name: str, amount: float):
        """
        Перевести деньги между кейсами
        """
        from_case = self.get_case(from_name)
        to_case = self.get_case(to_name)
        
        # Проверяем совместимость валют
        if from_case.currency != to_case.currency:
            raise ValueError("Нельзя переводить между разными валютами")
        
        # Снимаем с одного, кладем в другой
        from_case.withdraw(amount)
        to_case.deposit(amount)
        
    def show_all(self):
        """Показать все кейсы"""
        print("\n=== Все кейсы ===")
        for case in self.cases:
            print(f"  {case}")
        print("=" * 20)