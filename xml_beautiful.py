from xml.etree import ElementTree
from xml.dom import minidom

def krasivo(element):
    '''Вовзращает красиво распечатанную XML строку для element'''
    rough_string = ElementTree.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)

    return reparsed.toprettyxml(indent="  ")
