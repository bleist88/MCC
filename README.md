##  MCC

The *MCC* package is designed to create a master catalog from a set of
independently created, uncorrelated catalogs.  For *N* unique objects in the set
of *M* catalogs, the master catalog will create a master catalog of size *N* as
well as *M* other extensions of size *N*.  The master catalog is stored in a
python pickle file with the extension ".mcc".  The *MCC* package also has a set
of tools to assist with batch, *SExtractor* runs as well as useful stamp
plotting routines.

![Master Object 125622](Figures/125622.png)

##  The Terminal and Configuration File

The key routines of *MCC* may be run from the command line using the *mcc*
command followed by the command desired and necessary flags.
```
mcc <command> -<key> <value> -<key> <value>
```

A configuration file is needed in order to operate *MCC* from the command line,
although none of the *MCC* routines require this when operating from within a
python shell.
```
#<  name        <U16
#<  catalog     <U18
#<  image       <U18
#<  Rc          float64
#<  append      <U6

GALEX_FUV             GALEX_FUV.cat         GALEX_FUV.1.fits       1.50   True
GALEX_FUV             GALEX_FUV.cat         GALEX_FUV.2.fits       1.50   True
GALEX_FUV             GALEX_FUV.cat         GALEX_FUV.3.fits       1.50   True
GALEX_FUV             GALEX_FUV.cat         GALEX_FUV.4.fits       1.50   True

GALEX_NUV             GALEX_NUV.cat         GALEX_NUV.1.fits       1.50   True
GALEX_NUV             GALEX_NUV.cat         GALEX_NUV.2.fits       1.50   True
GALEX_NUV             GALEX_NUV.cat         GALEX_NUV.3.fits       1.50   True
GALEX_NUV             GALEX_NUV.cat         GALEX_NUV.4.fits       1.50   True

MEGAPRIME_u           MEGAPRIME_u.cat       MEGAPRIME_u.fits       0.50   True
MEGAPRIME_g           MEGAPRIME_g.cat       MEGAPRIME_g.fits       0.50   True

z_VISTA               zVista.cat            None                   0.50   False
```
The top lines starting with `#<` indicate the line as a column format (see
*Io/README.md*).  The column definitions are indicated by this header. One thing
to notice is that the extension `GALEX_FUV` has multiple rows, only differing in
the image name.  This is the way to indicate to *MCC* that multiple images are
associated with this extension.  The column definitions are as follows:

*   name    -   name of the extension in the master
*   catalog -   name of the catalog ascii file
*   image   -   name of an image associated with the extension
*   Rc      -   correlation radius [arcsec] used in correlation
*   append  -   boolean to indicate whether or not to add unmatched objects

Any lines starting with `#` will be ignored from the configurations file.

##  Creating a Master Catalog

The *MCC* command `create` is used to create a master catalog from the configs
file as well as the existing catalogs in ASCII format.
```
mcc create -mcc Field.mcc -cfg Field.cfg -path Catalogs
```

Flags:
*   -mcc    master catalog pickle file to create
*   -cfg    configurations file
*   -path   path to the input catalog files ("." by default)

##  Adding and Correlating a New Catalog

The *MCC* command `add` is used to correlate and add a new catalog to an
existing master catalog.  This may only be done with the pickle file.
```
mcc add -mcc Field.mcc -cat MEGAPRIME_u -cfg Field.cfg -path Catalogs
```

Flags:
*   -mcc    existing master catalog pickle file
*   -cfg    configurations file
*   -path   path to the input catalog files ("." by default)
*   -cat    name of the catalog to add (name as listed in the configs file)

##  Writing an ASCII from an Extension

The *MCC* command `write` is used to write a formatted ASCII file from an
extension within the master.  The master extension is indicated by "master"
(not case sensitive).
```
mcc write -mcc Field.mcc -cat MEGAPRIME_u -ascii MEGAPRIME_u.cat
```

Flags:
*   -mcc    existing master catalog pickle file
*   -cat    name of the catalog to write
*   -ascii  name of the output ASCII file

##  Writing a FITS Master Catalog

The *MCC* command `write_fits` creates a FITS cube with the same basic structure
as the pickle file.
```
mcc write_fits -Field.mcc -fits Field.fits -clobber False
```

Flags:
*   -mcc        existing master catalog pickle file
*   -fits       name of the FITS file to write the master to
*   -clobber    if "True", it will overwrite an existing FITS file
