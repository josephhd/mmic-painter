# mmic-painter
MMIC painter is a small Python program for rendering MMIC layouts as publication-quality figures. It supports reading GDS files and can save figures in vector (SVG, PDF, etc.), as well as rasterized formats (PNG, JPEG, etc.). 

While MMIC painter was originally intended for MMIC layouts, it can be used with any layout that is given as a GDS. This includes PCBs or other mechanical drawings. 

NOTE: When exporting your GDS for plotting, ensure that it's exported as a FLAT GDS file.

## Prerequisites
To run this code, the following packages are required:

* `matplotlib`
* `numpy`
* `gdspy`

Before installing `gdspy`, Microsoft Visual Studio C++ compiler tools must be installed. 
1. Navigate to the download for Microsoft's Visual Studio Build Tools found **[here](https://visualstudio.microsoft.com/downloads/?q=build+tools)**. Download the build tools installer which is found towards the bottom of the page under `Tools for Visual Studio->Build Tools for Visual Studio 2022`. 
2. Run the downloaded installer.
3. Once installed, launch the `Visual Studio Installer` which was installed on your computer. 
4. Under the installed applications, find `Visual Studio Build Tools 2022` and click on `Modify`. 
5. Find the `Desktop development with C++` icon, and click it so that it is checked and selected.
6. With the `Desktop development with C++` tools selected, find the `Installation details` on the right side. 
7. Under the `Optional` drop-down, make sure that only the following are selected (note that versions may differ):
    * MSVC v143 - VS 2022 C++ x64/x86 build tools
    * Windows 11 SDK
    * C++ CMake tools for Windows
8. In the bottom right, select `Modify`/`Install`.
9. Once complete, you can close the application and the correct tools will have been installed. 

After completing the above, install the prerequisite packages using `pip install matplotlib numpy gdspy`. 

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

### LNA Example
Change to the installation location of `mmic_painter` and run the following command: `mmicpainter examples/lna.gds processes/WIN_PQG3_0C`. This will show the layout of a 2-channel LNA using default options, with the layers specified in the WIN PQG3-0C process. 

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
