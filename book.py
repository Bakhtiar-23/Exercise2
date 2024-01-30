class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year



# Example usage
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

# Test the function
if __name__ == "__main__":
    # Accessing attributes
    print(f"{python.author}: {python.name} ({python.year}).")
    print(f"The genre of the book {everest.name} is {everest.genre}.")
