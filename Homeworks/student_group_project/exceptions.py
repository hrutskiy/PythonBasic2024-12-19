class GroupLimitError(Exception):
    """Виняток, якщо група перевищує 10 студентів."""
    def __init__(self, message="Досягнуто ліміт студентів у групі (максимум 10)."):
        self.message = message
        super().__init__(self.message)
