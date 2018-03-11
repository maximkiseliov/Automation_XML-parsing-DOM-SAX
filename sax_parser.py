import xml.sax

class ProductHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.name = ""
        self.measure = ""
        self.price = ""
        self.barcode = ""
        self.country = ""

    '''Вызывается при старте элемента'''
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "product":
            print("*---Product---*")
            product_id = attributes["id"]
            print("ID:", product_id)

    '''Вызывается при окончании элемента'''
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "name":
            print("Name:", self.name)
        elif self.CurrentData == "measure":
            print("Measure:", self.measure)
        elif self.CurrentData == "price":
            print("Price:", self.price)
        elif self.CurrentData == "barcode":
            print("Barcode:", self.barcode)
        elif self.CurrentData == "country":
            print("Country:", self.country, "\n")
        self.CurrentData = ""

    '''Вызывается при чтении символа'''
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "measure":
            self.measure = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "barcode":
            self.barcode = content
        elif self.CurrentData == "country":
            self.country = content
   
if (__name__ == "__main__"):

    '''Создаём XML ридр'''
    parser = xml.sax.make_parser()
    '''Выключаем namespaces'''
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    '''Вызов класса'''
    Handler = ProductHandler()
    parser.setContentHandler(Handler)

    parser.parse("docs/products_xml.xml")
