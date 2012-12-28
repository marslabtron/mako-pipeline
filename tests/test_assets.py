# coding: utf-8
import re
import unittest

from mako.template import Template
from mock import MagicMock

from mako_pipeline import configure
from mako_pipeline.assets import tag


MOCK_CONF_DEBUG_MODE = {
    'debug': True,
    'media_url': 'my-url/',
    'javascript': {
        'final-js-bundle': ['file1', 'file2']
    }
}

MOCK_CONF_PROD_MODE = dict(MOCK_CONF_DEBUG_MODE)
MOCK_CONF_PROD_MODE['debug'] = False


class TemplateTagTestCase(unittest.TestCase):
    def test_if_assets_url_is_generated_with_final_filename_when_debug_is_false(self):
        context = MagicMock()
        context['caller'] = MagicMock()
        context['caller'].body = MagicMock()

        configure(MOCK_CONF_PROD_MODE)
        tag(context, 'final-js-bundle')

        context['caller'].body.assert_called_with(ASSETS_URL='my-url/final-js-bundle.js')

    def test_if_assets_url_is_generated_for_each_file_when_debug_is_true(self):
        context = MagicMock()
        context['caller'] = MagicMock()
        context['caller'].body = MagicMock()

        configure(MOCK_CONF_DEBUG_MODE)
        tag(context, 'final-js-bundle')

        context['caller'].body.assert_any_call(ASSETS_URL='my-url/file1.js')
        context['caller'].body.assert_any_call(ASSETS_URL='my-url/file2.js')

    def test_if_mako_can_import_assets_plugin_from_template(self):
        configure(MOCK_CONF_PROD_MODE)

        content = Template("""
            <%namespace name="assets" module="mako_pipeline.assets"/>
            <%assets:tag name="final-js-bundle" args="ASSETS_URL">
                before:${ASSETS_URL}:after
            </%assets:tag>
        """).render().strip()

        self.assertIsNone(re.search('before:my-url/file1.js:after', content))
        self.assertIsNone(re.search('before:my-url/file2.js:after', content))
        self.assertIsNotNone(re.search('before:my-url/final-js-bundle.js:after', content))
