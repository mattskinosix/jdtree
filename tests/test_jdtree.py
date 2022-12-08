from jdtree import JDTEngine


class TestTree():

    def test_decision(self):
        aspected_result = [{'result': {'ciao': 'ciao'}}]
        tree = JDTEngine(file_path="assets/test.json")
        result = tree.decide(
          {
              'temperatura': '12',
          })
        assert result == aspected_result

