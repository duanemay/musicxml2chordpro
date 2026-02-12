
import sys
import os
# Add parent directory to path so we can import xml2pro
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import codecs
from io import StringIO
import xml2pro

class Test_XML2Pro(unittest.TestCase):
    maxDiff = None  # Show full diff

    def test_1(self):
        """Test conversion of 'An Affair to Remember' against model file"""
        input_filename = 'test/An Affair to Remember.xml'
        model_filename = 'test/An Affair to Remember.pro'

        fout = StringIO()
        x1 = xml2pro.XML2Pro(input_filename, fout)
        x1.process_file()
        
        generated_text = fout.getvalue()
        with open(model_filename, 'r', encoding='utf-8') as f:
            model_text = f.read()
            
        self.assertEqual(generated_text, model_text)


if __name__ == '__main__':
    unittest.main()

