#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name              = 'Chiplotle',
      version           = '0.4.3',
      description       = 'Chiplotle is an HPGL Python API.',
      long_description  = 'Chiplotle is an HPGL Python API.',
      author            = 'Víctor Adán and Douglas Repetto',
      author_email      = 'chiplotle@music.columbia.edu',
      url               = 'http://music.columbia.edu/cmc/chiplotle',
      keywords          = 'vector graphics hpgl plotter plot pen',
      license           = 'GPL',

      include_package_data = True,
      packages             = find_packages(), 
      install_requires     = ['pyserial<=3', 'numpy<=2'],
      entry_points         = {'console_scripts':
         ['chiplotle = chiplotle.core.cfg._run_chiplotle:_run_chiplotle',]},
      scripts              = [
         'chiplotle/scripts/envelope.py',
         'chiplotle/scripts/find_hpgl_file_dimensions.py',
         'chiplotle/scripts/plot_hpgl_file_max_size.py',
         'chiplotle/scripts/plot_hpgl_file.py',
         'chiplotle/scripts/plot_hpgl_file_virtual.py',
         'chiplotle/scripts/typewriter.py',
         'chiplotle/scripts/view_hpgl_file.py',
         ],
      )

