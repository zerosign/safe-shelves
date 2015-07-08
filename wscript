#!/usr/bin/env python

import pdb

VERSION = "1.0.0"
VERSION_MAJOR_MINOR = ".".join(VERSION.split(".")[0:2])
APP_NAME = "safe-shelves"


srcdir = '.'
blddir = 'bin'

def options(opt):
    opt.load('compiler_c')
    opt.load('gnu_dirs')

def configure(conf):
    conf.load('compiler_c vala gnu_dirs')
    conf.check_vala(min_version=(0,28,0))
    
    conf.check_cfg(package='glib-2.0', uselib_store='GLIB',
                   atleast_version='2.14.0', mandatory=True, args='--cflags --libs')
    conf.check_cfg(package='gobject-2.0', uselib_store='GOBJECT',
                   atleast_version='2.14.0', mandatory=True, args='--cflags --libs')
    conf.check_cfg(package='gtk+-3.0', uselib_store='GTK',
                   mandatory=True, args='--cflags --libs')
    conf.define('PACKAGE', APP_NAME)
    conf.define('PACKAGE_NAME', APP_NAME)
    conf.define('PACKAGE_STRING', APP_NAME + '-' + VERSION)
    conf.define('PACKAGE_VERSION', APP_NAME + '-' + VERSION)
    
    conf.define('VERSION', VERSION)
    conf.define('VERSION_MAJOR_MINOR', VERSION_MAJOR_MINOR)

    
def build(bld):
    bld.recurse('src')
