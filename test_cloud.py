import os
from subprocess import check_call, check_output
import tempfile

def test_command():
    check_call([
        './cloud',
        '--debug',
        '--net', 'public',
        '--command', '/bin/true'
    ])

def test_script():
    with tempfile.NamedTemporaryFile() as f:
        f.write('#!/bin/sh\necho hello\n')

        check_call([
            './cloud',
            '--debug',
            '--net', 'public',
            f.name
        ])

def test_most_options():
    check_call([
        './cloud',
        '--debug',
        '--net', 'public',
        '--command', '/bin/true'
    ])
