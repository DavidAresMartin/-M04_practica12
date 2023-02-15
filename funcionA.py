
import xml.etree.ElementTree as ET

def integrantA():
    tree = ET.parse("escola.xml")
    root = tree.getroot()
    # root
    r = ET.Element('alumnes')
    # child del root
    r2 = ET.SubElement(r, 'alumne')
    r3 = ET.SubElement(r, 'alumne')
    r4 = ET.SubElement(r, 'alumne')
    r5 = ET.SubElement(r, 'alumne')
    r6 = ET.SubElement(r, 'alumne')
    # childs de alumne

    c1 = ET.SubElement(r2, 'name')
    c1.text = 'David'
    c2 = ET.SubElement(r2, 'subname')
    c2.text = 'Ares'
    c3 = ET.SubElement(r2, 'email')
    c3.text = 'davidares@gmail.com'
    c4 = ET.SubElement(r2, 'dni')
    c4.text = '12345678A'

    v1 = ET.SubElement(r3, 'name')
    v1.text = 'Elihu'
    v2 = ET.SubElement(r3, 'subname')
    v2.text = 'Valdelomar'
    v3 = ET.SubElement(r3, 'email')
    v3.text = 'elihuvaldelomar@gmail.com'
    v4 = ET.SubElement(r3, 'dni')
    v4.text = '12345678B'

    n1 = ET.SubElement(r4, 'name')
    n1.text = 'Didac'
    n2 = ET.SubElement(r4, 'subname')
    n2.text = 'Lopez'
    n3 = ET.SubElement(r4, 'email')
    n3.text = 'didaclopez@gmail.com'
    n4 = ET.SubElement(r4, 'dni')
    n4.text = '12345678C'

    j1 = ET.SubElement(r5, 'name')
    j1.text = 'Juan'
    j2 = ET.SubElement(r5, 'subname')
    j2.text = 'Ramirez'
    j3 = ET.SubElement(r5, 'email')
    j3.text = 'juanramirez@gmail.com'
    j4 = ET.SubElement(r5, 'dni')
    j4.text = '12345678D'

    m1 = ET.SubElement(r6, 'name')
    m1.text = 'Carlos'
    m2 = ET.SubElement(r6, 'subname')
    m2.text = 'Perez'
    m3 = ET.SubElement(r6, 'email')
    m3.text = 'carlosperez@gmail.com'
    m4 = ET.SubElement(r6, 'dni')
    m4.text = '12345678E'

    ET.indent(r)
    # mostrar por consola
    ET.dump(r)
    ET.indent(tree)
    # Ver como queda el archivo
    tree = ET.ElementTree(r)
    tree.write("escola.xml")

