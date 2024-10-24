import xml.etree.ElementTree as ET

def process_quantity(value):
    """Remove o sinal de negativo se houver"""
    if value.startswith('-'):
        return value[1:]  # Remove o primeiro caractere (o sinal de negativo)
    return value

def remove_namespace(tree):
    """Remove os namespaces do XML"""
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # Remove o namespace

def process_xml(xml_file):
    """Lê o arquivo XML, processa a tag <Quantity> e remove o sinal negativo"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Remover namespaces (opcional)
    remove_namespace(tree)

    # Iterar sobre todas as tags 'Quantity' (maiuscula Q)
    for quantity in root.findall('.//Quantity'):
        original_value = quantity.text.strip()  # Pega o valor da tag <Quantity>
        new_value = process_quantity(original_value)
        
        if original_value != new_value:
            print(f'Alterando valor de {original_value} para {new_value}')
        
        # Atualiza o valor na tag <Quantity>
        quantity.text = new_value
    
    # Salva o XML modificado em um novo arquivo ou sobrescreve o original
    tree.write('janeiro 2024.xml', encoding='utf-8', xml_declaration=True)
    print('Processamento completo. Arquivo atualizado salvo como output.xml')

# Exemplo de uso
process_xml('janeiro.xml')
