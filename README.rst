mako-pipeline
=============

A sort of django-pipeline, but for mako.

Install
-------

mako-pipeline is avaiable on pypi:

.. code-block::

  $ pip install mako-pipeline


Usage
-----

On your python script, call `mako_pipeline.configure` to setup file mapping:

.. code-block:: python

  from mako_pipeline import configure

  configure({
      'debug': True,
      'javascript': {
          'final-js': ['file1', 'file2']
      }
  })

On templates, import the module using `namespace` tag and use like following:

.. code-block:: html

  <%namespace name="assets" module="mako_pipeline.assets" />

  <%assets:tag name="final-js" args="ASSETS_URL" %>
    <script src="${ASSETS_URL}"></script>
  <%/assets:tag%>

License
-------

This project is licensed under MIT license (please see LICENSE file).

Some random thoughts
====================

- when compressing css, delegate the task to scss/less/etc
- when compressing js, delegate the task to uglifyjs2/yui/etc
- when writing files, include the md5/sha1/etc on filename
- use a manifest file to control how img/css/js urls will be generated
  (write the hashes there)

```
CONFIG = {
    'debug': True,
    'media_url': '/media/',
    'js': {
        'main': ['file1.js', 'file2.js'],
    },
    'css': {
        'main': ['fila1.css', 'file2.css'],
    },
}

$ tornado-pipeline --help
  --compress-css
  --compress-js
  --compress-all

```
