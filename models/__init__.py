#!/usr/bin/python3
"""Initializer passes storage func from engine"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
