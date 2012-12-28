mako-pipeline
=============

A sort of django-pipeline, but for mako.

Install
-------

mako-pipeline is avaiable on pypi.

```
$ pip install mako-pipeline
```

Usage
-----

```
<%namespace name="assets" module="mako_pipeline.assets" />

<%assets:tag name="final-js" args="ASSETS_URL" %>
    <script src="${ASSETS_URL}">
<%/assets:tag%>

```

License
-------

This project is licensed under MIT license (please see LICENSE file).
