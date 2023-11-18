import aspose.words
from main import get_product_info


def writer(parametr):
    doc = aspose.words.Document()

    builder = aspose.words.DocumentBuilder(doc)
    builder.write("product")

    for item in parametr:
        builder.write('\n')
        builder.write(f"Name: {item[0]}")
        builder.write('\n')
        builder.write(f"Price: {item[1]}")
        builder.write('\n')
        builder.write(f"Description: {item[2]}")
        builder.write('\n')
        builder.write(f"Image link: {item[3]}")
        builder.write('\n')
        builder.write('\n')
        builder.write('\n')

    doc.save("products.docx")


writer(list(get_product_info()))
