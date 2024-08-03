from estudos2c import Person, DataCollector


def main():
    collector = DataCollector()
    data = Person()
    
    print('MENU')
    print()
    print()
    print('hoose one of the options: ')
    option_allowed = ['1', '2', '3']
    while True:
        option = input('[1]ADD (person)  [2]exit [3]data:  ')
        print()

        if option not in option_allowed:
            print('number invalid')
            continue
    
        elif option == '1':
            collector.get_data()
        
        elif option == '2':
            break
        
        elif option == '3':
            Person.list_person()
main()