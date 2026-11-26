import unittest
from triage import classify, process

class TriageTests(unittest.TestCase):
    def test_billing(self):
        self.assertEqual(classify("INVOICE request")["queue"],"billing")
    def test_ambiguous(self):
        self.assertTrue(classify("payment login")["requires_review"])
    def test_unknown(self):
        self.assertEqual(classify("other")["queue"],"review")
    def test_no_substring(self):
        self.assertEqual(classify("restart")["queue"],"review")
    def test_sample(self):
        rows=list(process("sample.csv"))
        self.assertEqual(len(rows),5)
        self.assertEqual(sum(r["requires_review"] for r in rows),2)

if __name__=="__main__": unittest.main()
