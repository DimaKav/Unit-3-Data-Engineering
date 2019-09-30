from acme import Product
import random as r


# Randomly generate x number of products
def generate_products(n=30):
    '''
    Generate a given number of products (n), randomly,
    and return them as a list.
    '''
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    name = [r.choice(adjectives) + " " + r.choice(nouns) for i in range(n)]
    price = [r.choice([i for i in range(5, 101)]) for i in range(n)]
    weight = [r.choice([i for i in range(5, 101)]) for i in range(n)]
    flammability = [round(r.uniform(0, 2.5), 2) for i in range(n)]
    products = [[name[i], price[i], weight[i],
                 flammability[i]] for i in range(n)]
    return products


def inventory_report(products):
    '''
    Takes a list of products and prints a summary
    '''
    nunique = len(set(i[0] for i in products))
    avgprice = sum(i[1] for i in products) / len(products)
    avgweight = sum(i[2] for i in products) / len(products)
    avgflammability = sum(i[3] for i in products) / len(products)
    print("Unique product names:", nunique)
    print("Average price:", avgprice)
    print("Average weight:", avgweight)
    print("Average flammability", avgflammability)


if __name__ == '__main__':
    inventory_report(generate_products())
