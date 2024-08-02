from estudos1 import Person, DataCollector


def main():
    collector = DataCollector()
    
    print('MENU')
    print()
    print()
    print('hoose one of the options: ')
    option_allowed = ['1', '2']
    while True:
        option = input('[1]ADD (person)  [2]exit')

        if option not in option_allowed:
            print('number invalid')
            continue
    
        elif option == '1':
            collector.get_data()
        