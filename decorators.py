def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper
    
@be_polite
def greet():
    print("My name is Brandon.")

# greet = be_polite(greet) - replaced by @be_polite
greet()
