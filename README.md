# Variant Intersections

Quick tool that uses the [upset_plotly](https://github.com/fmaguire/upset_plotly) 
library (a plotly version of [upsetplot](https://pypi.org/project/UpSetPlot/))
to parse the outputs of a variant checking tool and generate an interactive
upsetplot showing the co-occurrence of specific variants.

Supported inputs:

1. Output csv from [type_variants](https://github.com/cov-ert/type_variants) (must be run with --append-genotypes
2. *NOT CURRENTLY IMPLEMENTED*: Output from [`ncov-watch.py`](https://github.com/jts/ncov-random-scripts).

## Installation
    
    git clone git@github.com:fmaguire/variant_intersections
    cd variant_intersections
    python -m pip install -r requirements.txt .

## Usage

To create a plot for an output from `type_variants`:
   
    var_intersect_plot -i variant_check.tsv -t type_variants -o example.html 
