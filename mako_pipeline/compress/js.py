# coding: utf-8
"""
Compress the javascript files
"""
from subprocess import call

from mako_pipeline import ASSETS


def uglifyjs(in_files, out_file):
    args = ['uglifyjs'] + in_files + ['-o', out_file]
    call(args)


def compress_all():
    for compressed, files in ASSETS['javascript'].iteritems():
        compressed_name = "{}.min.js".format(compressed)
        uglifyjs(["{}.js".format(f) for f in files], compressed_name)
