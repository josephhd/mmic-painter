# mmic-painter
MMIC painter is a small Python program for rendering MMIC layouts as publication quality figures. It supports reading GDS files, and can save figures in vector (svg, pdf, etc.), as well as rasterized formats (png, jpeg, etc.). 

While MMIC painter was originally intended for MMIC layouts, it can be used with any layout that is given as a GDS. This includes PCBs, or other mechanical drawings. 

## Prerequisits
To run this code, the following packages are required:

* `matplotlib`
* `numpy`
* `gdspy`

Before installing `gdspy`, Microsofts Visual Studio C++ compiler tools must be installed. 
1. Navigate to the download for Microsoft's Visual Studio Build Tools found **[here] (https://visualstudio.microsoft.com/downloads/?q=build+tools)**. Download the build tools installer which is found towards the bottom of the page under `Tools for Visual Studio->Build Tools for Visual Studio 2022`. 
2. Run the downloaded installer.
3. Once installed, launch the `Visual Studio Installer` which was installed on your computer. 
4. Under the installed applications, find `Visual Studio Build Tools 2022` and click on `Modify`. 
5. Find the `Desktop development with C++` icon, and click it so that it is checked and selected.
6. With the `Desktop development with C++` tools selected, find the `Installation details` on the right side. 
7. Under the `Optional` drop down, make sure that only the following are selected (note that versions may differ):
    * MSVC v143 - VS 2022 C++ x64/x86 build tools
    * Windows 11 SDK
    * C++ CMake tools for Windows
8. In the bottom right, select `Modify`.
9. Once complete, you can close the application and the correct tools will have been installed. 

After completeing the above install the prerequisite packages using `pip install matplotlib numpy gdspy`. 

## Configuring Windows Path (Optional but recommended)
MMIC painter can be configured to be executable from directory by adding the directory of the source file to Window's environment variables. 

MMIC Painter is intended to be run from the command line. For example, you can get the help using `python mmic_painter -h` when in the same working directory as the `mmic_painter` source file. If you want to run `mmic_painter` this way from other places in the file system, this becomes cumbersome because the entire path name must be included. 

This can be eased by simply adding the directory of `mmic_painter` to the system path. 

1. On Windows, search for `Edit the system environment variables`.
2. In the `System Properties` dialog, clock on `Environment Variables`.
3. Under the `User Variables`, find the `Path` variable and click `Edit`.
4. Click `New` and add the directory to where `mmic_painter` is on your file system. For example, `D:\OneDrive - UCB-O365\Research\utils\mmic-painter\`. 
5. Press `Ok` on all the open dialogs. 

To run mmic-painter from the command line, you can now use the command `mmicpainter`. To see the help, type `mmicpainter -h` .

## Running mmic-painter
mmic-painter comes with some example files to test installation. The following shows examples of how to execute mmic-painter on these files. The following examples assume that you have setup the path environment variable correctly. 
### LNA Example
`mmicpainter examples/lna.gds processes/WIN_PQG3_0C`

### Differential Pair Example
`mmicpainter examples/diffpair.gds processes/WIN_PQG3_0C`

## Adding Process Files
A custom process file can be added by copying and modifying one of the existing process files found in the `process` directory. 