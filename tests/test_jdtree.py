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


    def test_condition_empty_true(self):
        tree = JDTEngine(file_path="assets/test_condition_empty_true.json")
        
        aspected_result = []
        result = tree.decide(
          {
              'temperatura': '12',
          })
        assert result == aspected_result

        aspected_result = [{'result': True}]
        result = tree.decide(
          {
              'temperatura': None,
          })
        assert result == aspected_result

        aspected_result = [{'result': True}]
        result = tree.decide(
          {
              'temperatura': '',
          })
        assert result == aspected_result


    def test_condition_empty_false(self):
        tree = JDTEngine(file_path="assets/test_condition_empty_false.json")
        
        aspected_result = [{'result': True}]
        result = tree.decide(
          {
              'temperatura': '12',
          })
        assert result == aspected_result

        aspected_result = []
        result = tree.decide(
          {
              'temperatura': None,
          })
        assert result == aspected_result

        aspected_result = []
        result = tree.decide(
          {
              'temperatura': '',
          })
        assert result == aspected_result
