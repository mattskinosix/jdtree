from tree_parser import TreeParser

tree = TreeParser()
print(tree.decide(
    {
        'category': '"veicolo-medio"',
        'km': 0.2,
        'day': 6
    }))
