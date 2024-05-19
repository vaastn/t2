import xml.etree.ElementTree as ET

# создаем XML-файл с данными о товарах
def create_xml_file(file_path):
    products = ET.Element("products")

    product1 = ET.SubElement(products, "product")
    ET.SubElement(product1, "name").text = "Ноутбук"
    ET.SubElement(product1, "category").text = "Электроника"
    ET.SubElement(product1, "price").text = "1500"

    product2 = ET.SubElement(products, "product")
    ET.SubElement(product2, "name").text = "Книга"
    ET.SubElement(product2, "category").text = "Литература"
    ET.SubElement(product2, "price").text = "20"

    tree = ET.ElementTree(products)
    tree.write(file_path)

# функция для чтения и обработки XML-файла
def process_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # сортировка товаров по цене
    products_sorted_by_price = sorted(root.findall("product"), key=lambda x: float(x.find("price").text))

    print("Сортировка товаров по цене:")
    for product in products_sorted_by_price:
        name = product.find("name").text
        category = product.find("category").text
        price = float(product.find("price").text)
        print(f"Название: {name}, Категория: {category}, Цена: {price}")

    # фильтрация товаров по категории
    category_to_filter = "Электроника"
    filtered_products = [product for product in root.findall("product") if product.find("category").text == category_to_filter]

    print("\nФильтрация товаров по категории 'Электроника':")
    for product in filtered_products:
        name = product.find("name").text
        category = product.find("category").text
        price = float(product.find("price").text)
        print(f"Название: {name}, Категория: {category}, Цена: {price}")

    # расчет общей стоимости заказа
    total_cost = sum(float(product.find("price").text) for product in root.findall("product"))
    print(f"\nОбщая стоимость заказа: {total_cost}")

if __name__ == "__main__":
    xml_file_path = "products.xml"
    create_xml_file(xml_file_path)
    process_xml(xml_file_path)
