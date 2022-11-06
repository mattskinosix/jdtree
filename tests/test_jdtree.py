from jdtree import JDTEngine


class TestTree():

    def test_decision(self):
        aspected_result = [{'result': {'ciao': 'ciao4'}}]
        tree = JDTEngine(file_path="assets/test.json")
        result = tree.decide(
          {
              'category': '"veicolo-medio"',
              'km': 0.2,
              'day': 6
          })
        assert result == aspected_result

