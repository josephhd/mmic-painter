# mmic-painter
MMIC painter is a small Python program for rendering MMIC layouts as publication-quality figures. It supports reading GDS files and can save figures in vector (SVG, PDF, etc.), as well as rasterized formats (PNG, JPEG, etc.). It is currenty developed by the [Microwave Research Group at the University of Colorado at Boulder](https://www.colorado.edu/faculty/popovic-zoya/).

While MMIC painter was originally intended for MMIC layouts, it can be used with any layout that is given as a GDS. This includes PCBs or other mechanical drawings. 

## Citation <a href="https://doi.org/10.5281/zenodo.19723624"><img src="https://zenodo.org/badge/1218674272.svg" alt="DOI"></a>
mmic-painter can be cited using the DOI above, or you can copy the citation below. 

BibTeX:
```
@software{mmic-painter,
	title = {josephhd/mmic-painter: v1.1},
	rights = {{MIT} License},
	url = {https://zenodo.org/doi/10.5281/zenodo.19723624},
	doi = {10.5281/ZENODO.19723624},
	shorttitle = {josephhd/mmic-painter},
	version = {v1.1},
	publisher = {Zenodo},
	author = {Dunbar, Joseph},
	urldate = {2026-10-31},
	date = {2026-10-31},
}
```

IEEE:
J. Dunbar, josephhd/mmic-painter: v1.1. (Oct. 31, 2026). Zenodo. doi: 10.5281/ZENODO.19723624.


## Prerequisites
To run this code, the following python packages are required:

* `matplotlib`
* `numpy`
* `gdstk`

## Configuring Windows Path (Optional but recommended)
MMIC painter can be configured to be executable from a directory by adding the directory of the source file to Window's environment variables. 

MMIC Painter is intended to be run from the command line. For example, you can get the help using `python mmic_painter -h` when in the same working directory as the `mmic_painter` source file. If you want to run `mmic_painter` this way from other places in the file system, this becomes cumbersome because the entire path name must be included. 

This can be eased by simply adding the directory of `mmic_painter` to the system path. 

1. On Windows, search for `Edit the system environment variables`.
2. In the `System Properties` dialog, clock on `Environment Variables`.
3. Under the `User Variables`, find the `Path` variable and click `Edit`.
4. Click `New` and add the directory to where `mmic_painter` is on your file system. For example, `D:\OneDrive - UCB-O365\Research\utils\mmic-painter\`. 
5. Press `Ok` on all the open dialogs. 

To run mmic-painter from the command line, you can now use the command `mmicpainter`. To see the help, type `mmicpainter -h` .

## Running mmic-painter
mmic-painter comes with some example files to test installation. The following shows examples of how to execute mmic-painter on these files. The following examples assume that you have setup the path environment variable correctly. If you haven't set up the path environment, then navigate to the main folder in the PowerShell and add `./` as a prefix to all the ensuing commands.

### Commands and Tips

The figure can be saved using the `-o` or `--output` optional argument followed by the file name and extension. The file type will be inferred from the file extension. For example, running `mmicpainter examples/lna.gds processes/WIN_PQG3_0C -o lna.png -dpi 600` will save a copy of the figure as a png with a DPI of 600 (note that DPI only affects rasterized image formats) in the current working directory. 

If you don't want to show the figure itself each time `mmicpainter` is run, use the `-s` command which will suppress the figure from being shown. This is useful if you just want to output the figure as is. The command `mmicpainter examples/lna.gds processes/WIN_PQG3_0C -s -o lna.png -dpi 600` will save the figure as a png, but won't show anything after running the command. 

If you want to specify the figure width and height in inches, use the `-wi` and `-hi` arguments. By default, the figure is 3x3.5 inches. Note that the specified size is used when saving the figure, and is how large the figure will appear in a LaTeX document when imported using `\includgraphics`. This is particularly helpful for maintaining font size continuity between the main document and the figure. Running `mmicpainter examples/lna.gds processes/WIN_PQG3_0C -wi 10 -hi 10` will plot the colorized layout with a width and height of 10 inches. 

The legend can be suppressed using the `-nl` command. Running `mmicpainter examples/lna.gds processes/WIN_PQG3_0C -wi 10 -hi 10 -nl` will show the same thing as before, but without the legend. 


## Adding Process Files
You can add a custom process file by copying and modifying one of the existing process files in the `process` directory. 

Layers are defined using the following code line:\
di.addLayer(`gds layer number`  , `colormap[color code]`, `'Legend Entry'` )\
Multiple layer numbers can be mapped to a single color and legend entry by replacing the layer number with a list of layer numbers (`[a,b,c]`).

In AWR, GDS layer numbers can be identified by double-clicking the process lpf file in the layout tab. Navigate to `File Export Mappings` > `MMIC GDSII (GDSII)`. You’ll find a table with drawing layers and layer numbers.
