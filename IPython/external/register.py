"""Register directories with static files that are served along with the IPython
notebook in a unique namespace.

To be used for developing packages and widgets that embed javascript and css in
the IPython notebook.

* Zachary King

"""

from __future__ import print_function

#-----------------------------------------------------------------------------
#  Copyright (C) 2014  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------

class NamespaceRegistered(Exception):
    pass

class ExternalNamespaces(object):
    def __init__():
        self.registered_namespaces = {}

def register_external_directory(directory, namespace):
    """The directory needs to be served on all notebooks.

    directory: A local directory

    namespace: A unique string that specifies the namespace under which files
    will be served. If the namespace is already taken, a NamespaceRegistered
    expection is thrown.

    Files are served as follows:

    hostname:port/static_url/external/my_namespace/*

    Directories inside the specified directory are respected. Thus, a require.js
    call like the following is possible:

    require(["external/my_namespace/my_custom_js"], function(MyCustomJS) {

    });

    WARNING: These files won't be served with nbconvert, and a page won't load
    properly immediately after restarting the notebook server. Thus, this is
    really designed for development and testing. Finished code should be served
    from an external website or cdn.
    
    """
    if namespace in 
    pass
