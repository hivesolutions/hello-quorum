#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask #@UnusedImport

import quorum

app = quorum.load(
    name = __name__,
    logger = "hello_quorum.debug"
)

import hello_quorum.views #@UnusedImport

if __name__ == "__main__":
    quorum.run(server = "netius")
