#!/usr/bin/env python
"""Console script for variant_intersections."""
from pathlib import Path
import argparse
import os
from pathlib import Path
from variant_intersections import __version__
from variant_intersections import variant_intersections


def check_file(path: str) -> Path:
    """
    Check an input file exists and is readable
    """
    path = Path(path)
    if path.exists() and path.is_file():
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} can't be read")


def check_output_suffix(path: str) -> Path:
    """
    Check specified output has .html or .png
    """
    path = Path(path)
    if path.suffix in ['.html', '.png']:
        return path
        #if os.access(path, os.W_OK):
        #    return path
        #else:
        #    raise argparse.ArgumentTypeError(f"{path} cannot be written")
    else:
        raise argparse.ArgumentTypeError(f"{path} must end in .html or .png")


def main():
    """Console script for variant_intersections"""
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', "--input", required=True, type=check_file,
                         help="Input type_variants or ncov_watch file")
    parser.add_argument('-t', '--type', required=True,
                         choices=['type_variants', 'ncov_watch'],
                         help="Program used to generate the input file")
    parser.add_argument('-o', '--output', default="output.html",
                        type=check_output_suffix,
                        help="Output file name (ending in .html for an "
                             "interactive plot or .png for static image)")

    args = parser.parse_args()
    variant_intersections.variant_intersections(args.input, args.type,
                                                args.output)


if __name__ == "__main__":
    main()
