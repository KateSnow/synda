#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module contains search-API 'fields' related routines."""

import sdconst

def get_timestamp_fields():
    return ','.join(sdconst.TIMESTAMP_FIELDS)

def get_sample_fields():
    return ','.join(sdconst.TIMESTAMP_FIELDS)

def get_file_variable_fields():
    return 'title,instance_id,variable,size,type'

def get_dataset_version_fields():
    return 'master_id,version,timestamp,size,type'

# init.