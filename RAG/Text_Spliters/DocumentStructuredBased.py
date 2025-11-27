from langchain_text_splitters import RecursiveCharacterTextSplitter,Language



text = """
class Car:
    
    
    # Class attribute (shared by all instances of the class)
    wheels = 4

    def __init__(self, make, model, year):
       
        self.make = make        # Instance attribute
        self.model = model      # Instance attribute
        self.year = year        # Instance attribute
        self.speed = 0          # Instance attribute with a default value
        print(f"A new {self.year} {self.make} {self.model} has been created.")

    def accelerate(self, speed_increase):
        
        self.speed += speed_increase
        print(f"Accelerating... Current speed: {self.speed} mph.")

    def brake(self):
        
        self.speed = 0
        print("Braking... Car is stopped.")

    def get_description(self):
        
        description = f"This car is a {self.year} {self.make} {self.model}."
        return description

# --- Using the Class (Creating Objects/Instances) ---

# 1. Create instances of the Car class
my_car = Car(make="Toyota", model="Corolla", year=2024)
neighbor_car = Car("Honda", "Civic", 2020)

print("\n--- Interacting with my_car ---")

# 2. Access instance attributes
print(f"My car's model is: {my_car.model}")

# 3. Call methods
my_car.accelerate(30)
my_car.accelerate(15)
my_car.brake()

# 4. Use a method to get information
description_string = my_car.get_description()
print(description_string)

# 5. Accessing the class attribute
print(f"All cars have {Car.wheels} wheels.")

"""


doc_text_splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = doc_text_splitter.split_text(text)


for i,chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")