# coding: utf-8

import os
from latex import build_pdf

def building_pdf():
    """
     we need to supply absolute paths
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # we are adding an empty string to include the default locations (this is
    # described on the tex manpage)
    pdf = build_pdf(open('fall_texdoc.latex'), texinputs=[current_dir, ''])
    pdf.save_to('generated_pdf.pdf')

if __name__ == '__main__':
    building_pdf()
