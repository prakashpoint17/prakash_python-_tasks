class MultiplicationTable:
    def __init__(self, number, table_range):
        self.number, self.table_range = number, table_range

    def generate_table(self):
        print(f"Multiplication Table of {self.number} up to {self.table_range}:")
        for i in range(1, self.table_range + 1):
            print(f"{i} X {self.number} = {i * self.number}")

number = int(input("Enter the number for Generating Multiplication Table: "))
table_range = int(input("Enter the number to set the range for Multiplication Table: "))

table = MultiplicationTable(number, table_range)
table.generate_table()

