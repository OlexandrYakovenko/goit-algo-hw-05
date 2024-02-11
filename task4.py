class ParametersError(Exception):
    ''' class for wrong quantity parameters exception '''
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner

@input_error
def parse_input(user_input):
    ''' розбиратиме введений користувачем рядок на команду та її аргументи. 
    Команди та аргументи мають бути розпізнані незалежно від регістру введення. '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    ''' додати контакт '''
    if len(args)<2 or len(args)>2:
        raise ParametersError("Input 2 parameters")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args, contacts):
    ''' показати телефон '''
    if len(args)<1 or len(args)>1:
        raise ParametersError("Input 1 parameters")
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

@input_error
def change_contact(args, contacts):
    ''' змінити контакт '''
    if len(args)<2 or len(args)>2:
        raise ParametersError("Input 2 parameters")
    name, phone = args
    if not name in contacts:
        raise ParametersError("Name is not found.")
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_all(args, contacts):
    ''' надрукувати всі контакти '''
    if len(args)!=0:
        raise ParametersError("Function don't take parameters")
    s=''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]}\n")
    return s


def main():
    ''' головна програма '''
    contacts = {'John':"123", 'Jane':"234", 'Steve':"555"}  #    [{'name':'John Doe', 'phone':'+380988858880'},
                        #{'name':'Alice Cooper', 'phone':'+48880884215'}]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) #розбиратиме введений користувачем рядок на команду та її аргументи.

        if command in ["close", "exit"]: #вихід із програми
            print("Good bye!")
            break
        elif command == "hello": #вітання
            print("How can I help you?")
        elif command == "add": #додати контакт
            print(add_contact(args, contacts))
        elif command == "phone": #показати телефон по імені
            print(show_phone(args, contacts))
        elif command == "change": #змінити телефон по імені
            print(change_contact(args, contacts))
        elif command == "all": #роздрукувати телефонну книгу
            print(show_all(args, contacts))   
        else:
            print("Invalid command.") #невідома команда

if __name__ == "__main__": 
    main()