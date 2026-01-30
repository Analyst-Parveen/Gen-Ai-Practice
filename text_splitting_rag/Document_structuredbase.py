from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
text='''
class Calculator:
    """
    A simple Calculator class demonstrating
    class, constructor, and multiple methods.
    """

    def __init__(self, name: str):
        self.name = name

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def info(self) -> str:
        return f"Calculator name: {self.name}"


# Example usage
if __name__ == "__main__":
    calc = Calculator("MyCalculator")

    print(calc.info())
    print("Add:", calc.add(10, 5))
    print("Subtract:", calc.subtract(10, 5))
    print("Multiply:", calc.multiply(10, 5))
    print("Divide:", calc.divide(10, 5))  '''


splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0
)

chunk=splitter.split_text(text)
print(len(chunk))
print(chunk[2])

# for i in chunk:
#     print(i)