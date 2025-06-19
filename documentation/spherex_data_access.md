## SPHEREx Data Access

IRSA serves SPHEREx data on premises at IPAC. IRSA provides layered access to these data to support a variety of use cases and users. These layers include:

* **Browsable Directories:** SPHEREx on-premises data products are laid out in directories that can be navigated with standard web browsers.
* **Application Program Interfaces:** IRSA provides SPHEREx data access APIs that are compliant with International Virtual Observatory Alliance (IVOA) standards.
* **Python Packages:** SPHEREx data at IRSA are accessible via the Python packages pyvo and astroquery
* **SPHEREx Data Explorer:** IRSA provides a web-based Graphical User Interface (GUI) that makes it easy to search for, visualize, and download SPHEREx data.

Each of these data access layers is described in greater detail in the subsections below.

### Browsable Directories
SPHEREx data products are laid out in directories that can be navigated with standard web browsers. This is convenient for users to get a quick sense of the types of data products that are available, to quickly download some examples by clicking through the directory tree, and to script bulk downloads using wget or curl.

The root of the SPHEREx data directories is:
https://irsa.ipac.caltech.edu/ibe/data/spherex

The data are organized into subdirectories based on the following organizational scheme
* qr (quick release)
    * level2
        * planning_period
            * detector (1-6)
                * FITS files
    * calib_type
        * run_collection
            * detector (1-6)
                * FITS files

The content of each subdirectory is described in greater detail in the subsections below.

#### level2

* The `level2` subdirectory contains calibrated spectral images, also known as linear variable filter (LVF) images. These images are photometrically and astrometrically calibrated and are ready for science analysis, including photometric measurements. They are made available to the public within two months of acquisition.

#### planning_period

* `planning_period` is a designation by the SPHEREx project of the survey plan uploaded to the spacecraft, generally twice a week.  An example is `2025W22_1B`

#### calib_type

* What calibration files are in here?

#### run_collection

* `run_collection` is an SPHEREx Science Data Center (SSDC) tag to track the data processing.

#### detector

* The SPHEREx focal plane is split with a dichroic to three short-wavelength and three long-wavelength detector arrays. Two focal plane assemblies (FPAs) simultaneously image the sky through a dichroic beam splitter. Each FPA contains three 2K x 2K detector arrays placed behind a set of linear variable filters (LVFs), providing narrow-band response with a band center that varies along one axis of the array. SPHEREx obtains spectra through multiple exposures, placing a given source at multiple positions in the field of view, where it is measured at multiple wavelengths by repointing the spacecraft.

* Band 1: λ= 0.75 - 1.09 µm; R=41
* Band 2: λ= 1.10 - 1.62 µm; R=41
* Band 3: λ= 1.63 - 2.41 µm; R=41
* Band 4: λ= 2.42 - 3.82 µm; R=35
* Band 5: λ= 3.83 - 4.41 µm; R=110
* Band 6: λ= 4.42 - 5.00 µm; R=130


### Application Program Interfaces (APIs)

IRSA provides API access to SPHEREx LVF images through version 2 of the VO Simple Image Access (SIA2) protocol. SIA2 allows users to query for a list of images that satisfy constraints based on position(s) on the sky, band, time, ID, and instrument. The list returned by the service includes data access URLs, which can be used to retrieve some or all of the images in the list using wget or curl. A brief summary of SIA2 for accessing SPHEREx data for IRSA is given below. Additional documentation on IRSA’s SIA2 service can be found on the IRSA website:

https://irsa.ipac.caltech.edu/ibe/sia.html

IRSA's generric SIA2 endpoint is:

https://irsa.ipac.caltech.edu/SIA?

Users must add a COLLECTION to this endpoint to specify which dataset to saerch. SPHEREx-related COLLECTIONS include:

SPHEREx Quick Release Wide-Field Spectral Images: COLLECTION=spherex_qr

IRSA’s SIA2 endpoint for querying SPHEREx quick release spectral images that are part of the **deep survey** is:

https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex_qr_deep

IRSA’s SIA2 endpoint for querying SPHEREx quick release **calibration files** is:

https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex_qr_cal

You can use wget or curl to submit SIA queries from the command line. For example:

wget -O example1.csv "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex&POS=circle+164.7+-5.8+0.01&RESPONSEFORMAT=CSV"

curl --output example2.csv "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex&POS=circle+164.7+-5.8+0.01&RESPONSEFORMAT=CSV"

See the next section to learn how to use Python wrappers around IRSA’s SIA2 service.

### Python packages: PyVO & Astroquery

If you would like to take advantage of IRSA’s SIA2 service for querying SPHEREx images, but prefer to use Python rather than the command line, you may be interested in using one of two Python libraries:

*	PyVO  -- PyVO lets you find and retrieve astronomical data available from archives that support standard IVOA protocols.
*	Astroquery  -- This module provides access to the public astrophysics catalogs, images, and spectra curated by the NASA/IPAC Infrared Science Archive (IRSA) at Caltech. IRSA hosts data from many missions, including SPHEREx, Euclid, Spitzer, WISE/NEOWISE, SOFIA, IRTF, 2MASS, Herschel, IRAS, and ZTF.

Examples of data queries using both of these libraries can be found in IRSA’s Python Notebook Tutorial Repository:

https://caltech-ipac.github.io/irsa-tutorials/

### SPHEREx Data Explorer Web Application

Users who prefer an interactive graphical user interface (GUI) for specifying search constraints, submitting queries, and visualizing the results should consider the SPHEREx Data Explorer:

https://irsa.ipac.caltech.edu/applications/spherex

The tool includes its own context-sensitive help, but we summarize the main functionality below.

* LVF Search
* Spectrophotometry Tool
