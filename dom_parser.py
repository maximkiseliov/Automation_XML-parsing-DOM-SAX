from xml.dom.minidom import *


def ordinary_parser(store, products):
    """Выводим информацию о магазине + дата"""
    if store.hasAttribute("magazin") and store.hasAttribute("dataa"):
        print("Magazin: %s\nData: %s" % (store.getAttribute("magazin"), store.getAttribute("dataa")))
    
    """Выводим на печать делали о каждом продукте"""
    for product in products:
        print("*---Product---*")
        if product.hasAttribute("id"):
            print("ID: %s" % product.getAttribute("id"))

        typee = product.getElementsByTagName("type")[0]
        print("Type: %s" % typee.childNodes[0].data)
        
        name = product.getElementsByTagName("name")[0]
        print("Name: %s" % name.childNodes[0].data)
        
        measure = product.getElementsByTagName("measure")[0]
        print("Measure: %s" % measure.childNodes[0].data)
        
        price = product.getElementsByTagName("price")[0]
        print("Price: %s" % price.childNodes[0].data)
        
        barcode = product.getElementsByTagName("barcode")[0]
        print("Barcode: %s" % barcode.childNodes[0].data)
        
        country = product.getElementsByTagName("country")[0]
        print("Country: %s\n" % country.childNodes[0].data)

def query_parser(products):
    """Вывод информации по тегу введенному пользователем"""
    query = str(input('Введите имя тега:\n-> '))
    
    for product in products:
        if product.hasAttribute("id"):
            print("ID: %s" % product.getAttribute("id"))

        query_tag = product.getElementsByTagName(query)[0]
        print("%s: %s" % (query, query_tag.childNodes[0].data))

def menu():
    """Меню вызывает функцию в зависимости от выбора пользователя"""
    choice = int(input("""Выберите желаемый пункт:
1. Парсинг всего документа.
2. Вывод информации по введенному тегу.
3. Выход.
-> """))
    if choice == 1:
        ordinary_parser(store, products)
    elif choice == 2:
        query_parser(products)
    elif choice == 3:
        exit()
    else:
        print("Выберите пункт 1-3")
        menu()
        
        
#------------------------------------MAIN-------------------------------
'''Отрываем xml файл с помощью minidom parser'''
document = xml.dom.minidom.parse("docs/products_xml.xml")
store = document.documentElement

'''Получаем все продукты в магазине'''
products = store.getElementsByTagName("product")

menu()
 
