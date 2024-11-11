from models import company
from models import product

if __name__ == "__main__":
    data = []

    c1 = company.Company(name="Microsoft", products=[
        product.Product(name="Windows", category="Operating Systems"),
        product.Product(name="Linux", category="Operating Systems"),
    ])
    data.append(c1)

    c2 = company.Company(name="Mattel", products=[
        product.Product(name="Hot Wheels", category="Car Toys"),
        product.Product(name="Toy Story", category="Cartoon Toys"),
    ])
    data.append(c2)

    for x in data:
        x.info()
