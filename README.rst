PTVSD Wrapper
=============

This simple package exposed a script to proxy python script to debug on remote
host with `Visual Studio Code`_ editor.

.. _`Visual Studio Code`: https://code.visualstudio.com/

Why not just putting the following snippet code in the remote file to debug?:

.. code:: python

    import ptvsd
    ptvsd.enable_attach('my_secret', address=('0.0.0.0', 3000))
    ptvsd.wait_for_attach()

Because sometimes, for some strange reason, this is not enough and debugger
server needs be run very quickly...

By wrapping the command, this is worth for performance but works in most cases.

Furthermore, editing your code to put some breakpoints is not really comfortable...!

Get started
-----------

Install the package::

    pip install ptvsd-wrapper

Be sure to have a remote debug configuration in your ``launch.json`` of your
Visual Studio Code editor:

.. code-block:: javascript

    {
        "name": "Remote Debug",
        "type": "python",
        "request": "attach",
        "localRoot": "${workspaceRoot}",
        "remoteRoot": "<REMOTE_ROOT>",
        "port": <PORT>,
        "secret": "<SECRET>",
        "host": "<HOST>"
    }

Put some breakpoint and then connect on the remote host to execute the command
to debug with the wrapper script::

    ptvsd-wrapper <MY_PYTHON_SCRIPT>

For example::

    ptvsd-wrapper manage.py runserver 0.0.0.0:8000

If you can't have enought time to start the debugger in VSCode, you may ask for
waiting::

    ptvsd-wrapper --ptvsd-wait manage.py tests --settings=my_testing_settings.py --noinput

In that way, you have enough time to start debugging with ``F3`` key ;-)

You can see all availables options of the wrapper script by typing::

    ptvsd -h

