"""
Retrieves all hurricane data from NOAA at:
http://www.aoml.noaa.gov/hrd/hurdat/hurdat2.html

Saves raw data and multi-indexed CSV of the data in data/ in this directory.
"""

import re
import urllib2
from bs4 import BeautifulSoup
import pandas as pd

#get data from NOAA
raw_data = BeautifulSoup(
    urllib2.urlopen(
        'http://www.aoml.noaa.gov/hrd/hurdat/hurdat2.html'
    ).read(),
    'html.parser'
).find('body').text
hurdat = raw_data.split('\n')

def parse_header(line, line_num):
    """
    Parses a header line from hurricane data file.
    Documentation on header formats is available in the NOAA HURDAT2 format
    file:

    http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf

    The first group indicates the basin, cyclone number within the year, and
    year of the hurricane (or other storm). The next group indicates either the
    hurricane name or "UNNAMED". The final group indicates the number of
    rows to follow that pertain to this record.
    """

    header_row = re.compile(
        '[A-Z]{2}[0-9]{6},\s+\w+,\s+\d+'
        )

    header = header_row.search(line)

    #if this isn't a header line, return None before trying to do regex
    #stuff to None
    if not header:
        return

    return {line[4:8] + line[2:4] + line[18:28].strip(): {
        'indname': (
            line[18:28].strip(), line[:2], int(line[4:8]), int(line[2:4])
        ),
        'nrows': int(line[33:36]),
        'start_line': line_num
    }}

def unique_hurricanes(hurdat):
    """
    Returns header info for each unique hurricanes in HURDAT2-formatted text
    file hurdat.
    """

    #split on returns if hurdat is not a list
    if not isinstance(hurdat, list):
        hurdat = hurdat.split('\n')

    header_rows = [parse_header(
        line, line_num
    ) for line_num, line in enumerate(hurdat) if parse_header(
        line, line_num
    )]
    keys = [h.keys()[0] for h in header_rows]
    values = [h.values()[0] for h in header_rows]
    
    return {k: v for k, v in zip(keys, values)}
