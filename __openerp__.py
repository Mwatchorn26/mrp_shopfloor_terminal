# -*- coding: utf-8 -*-
{
    'name': "MRP - Shop Floor Terminal",

    'summary': """
        The interface for employees working on a shop floor. Granting quick access change MO sequences being worked on.
        """,

    'description': """MRP - Shop Floor Terminal
        
        * Allow employees to quickly switch jobs by touch-screen or a few barcodes.
        * Allow employees to issue material to job.        
        All without signing in and out over and over all day.

        Introducing quick Shop Floor Terminal
        The terminal uses a specific user account, and allows employees to scan their barcodes 
        (or select themselves from a list) to become the active user on the terminal.
        Once made the active user, all activities will be logged in the database as having been
        performed by that user (and not the generic terminal.
    """,

    'author': "Transformix Engineering Inc.",
    'website': "http://www.transformix.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'MRP',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base', 'mrp'],
    'depends': ['base'],
    'data': ['views/terminal.xml'],
    #'data': [],
    'demo': [],
    'tests': [],
}
