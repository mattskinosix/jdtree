from tree_parser import TreeParser

tree = TreeParser()
print(tree.decide(
    {
        'category': 'veicolo-leggero',
        'km': 20,
        'day': 6
    }))
