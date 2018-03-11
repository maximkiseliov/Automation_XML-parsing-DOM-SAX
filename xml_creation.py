from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml_beautiful import krasivo
import datetime

type1 = ["Fruit", "Milk Product", "Vegetable"]
name = ["Pineapple", "Milk JLC", "Tomato"]
measure = ["kg", "l", "kg"]
price = [10, 0.99, 5.5]
bardoce = ["123-123-0", "546-789-0", "888-999-0"]
country = ["Uganda", "Moldova", "Turkey"]
now = datetime.datetime.now() #Дата

store_el = Element("store")
store_el.set("magazin", "Linella 1")
store_el.set("data", now.strftime("%d-%m-%Y"))

for i in range(len(type1)):
    product_el = SubElement(store_el, "product")
    product_el.set("id", str(1+i))

    type_el = SubElement(product_el, "type")
    type_el.text = (type1[i])
    
    name_el = SubElement(product_el, "name")
    name_el.text = (name[i])
    
    measure_el = SubElement(product_el, "measure")
    measure_el.text = (measure[i])
    
    price_el = SubElement(product_el, "price")
    price_el.text = (str(price[i]))
    
    barcode_el = SubElement(product_el, "barcode")
    barcode_el.text = (str(bardoce[i]))
    
    country_el = SubElement(product_el, "country")
    country_el.text = (str(country[i]))

xml_max = krasivo(store_el)
doc_xml = open("docs\products_xml.xml", "w")
doc_xml.write(xml_max)
doc_xml.close()

