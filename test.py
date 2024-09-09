from jdtree.jdt_engine import JDTEngine
from time import time

now = time()
tree = JDTEngine(file_path="assets/tree.json")
result = tree.decide(
      {
        'test': 1 
      })
print(now - time())
print(result)
