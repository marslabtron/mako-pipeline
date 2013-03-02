# coding: utf-8
import unittest

from mock import patch

from mako_pipeline import configure
from mako_pipeline.compress import js


MOCK_CONF = {
    'javascript': {
        'final-js-bundle': ['file1', 'file2']
    }
}


class JsCompressorTest(unittest.TestCase):
    @patch('mako_pipeline.compress.js.call')
    def test_uglifyjs_called_with_correct_args(self, call):
        in_files = ['file1.js', 'file2.js']
        out_files = 'final.min.js'
        expected_args = ['uglifyjs', 'file1.js', 'file2.js', '-o', 'final.min.js']

        js.uglifyjs(in_files, out_files)

        call.assert_called_with(expected_args)

    @patch('mako_pipeline.compress.js.uglifyjs')
    def test_compress_all_javascripts_call_uglifyjs_with_correct_options(self, uglifyjs):
        configure(MOCK_CONF)

        js.compress_all()

        in_files = ['file1.js', 'file2.js']
        out_file = 'final-js-bundle.min.js'

        uglifyjs.assert_called_with(in_files, out_file)
