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

<%assets:tag name="{('all_js',)}" args="ASSETS_URL" %>
    <script src="${ASSETS_URL}">
<%/assets:tag%>

<%assets:tag name="{('all_css',)}" args="ASSETS_URL" %>
    <link rel="stylesheet" href="${ASSETS_URL}">
<%/assets:tag%>

```
