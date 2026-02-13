#!/usr/bin/env python3

import sys
import os

# Add parent directory to path so we can import xml2pro
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from io import StringIO
import xml2pro


class TestXML2Pro(unittest.TestCase):
    maxDiff = None  # Show full diff

    def test_affair(self):
        """Test conversion of 'An Affair to Remember' against model file"""
        input_filename = 'test/An Affair to Remember.xml'
        model_filename = 'test/An Affair to Remember.pro'
        self.file_testers(input_filename, model_filename)

    def test_mozart(self):
        """Test conversion of 'MozartPianoSonata' against model file"""
        input_filename = 'test/MozartPianoSonata.xml'
        model_filename = 'test/MozartPianoSonata.pro'
        self.file_testers(input_filename, model_filename)

    def test_mozart_notes(self):
        """Test conversion of 'MozartPianoSonata' against model file with notes"""
        input_filename = 'test/MozartPianoSonata.xml'
        model_filename = 'test/MozartPianoSonataNotes.pro'
        self.file_testers(input_filename, model_filename, output_notes=True)

    def test_chant(self):
        """Test conversion of 'Chant' against model file"""
        input_filename = 'test/Chant.xml'
        model_filename = 'test/Chant.pro'
        self.file_testers(input_filename, model_filename, output_notes=True)

    def file_testers(self, input_filename, model_filename, output_notes=False):
        fout = StringIO()
        x1 = xml2pro.XML2Pro(input_filename, fout, output_notes=output_notes)
        x1.process_file()

        generated_text = fout.getvalue()
        with open(model_filename, 'r', encoding='utf-8') as f:
            model_text = f.read()

        self.assertEqual(generated_text, model_text)


if __name__ == '__main__':
    unittest.main()
