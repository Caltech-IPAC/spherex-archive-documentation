## SPHEREx Data Access

IRSA serves SPHEREx data on premises at IPAC. IRSA provides layered access to these data to support a variety of use cases and users. These layers include:

* **Browsable Directories:** SPHEREx on-premises data products are laid out in directories that can be navigated with standard web browsers.
* **Application Program Interfaces:** IRSA provides SPHEREx data access APIs that are compliant with International Virtual Observatory Alliance (IVOA) standards.
* **Python Packages:** SPHEREx data at IRSA are accessible via the Python packages pyvo and astroquery
* **SPHEREx Data Explorer:** IRSA provides a web-based Graphical User Interface (GUI) that makes it easy to search for, visualize, and download SPHEREx data.

Each of these data access layers is described in greater detail in the subsections below.

### Browsable Directories
SPHEREx data products are laid out in directories that can be navigated with standard web browsers. This is convenient for users to get a quick sense of the types of data products that are available, to quickly download some examples by clicking through the directory tree, and to script bulk downloads using wget or curl.

The root of the SPHEREx data quick release data directories is:
https://irsa.ipac.caltech.edu/ibe/data/spherex/qr

The public data products are organized into subdirectories based on the following organizational scheme:
* `abs_gain_matrix/cal-agm-v[Version]-[Processing Date]/[Detector]/`
* `average_psf/cal-psf-v[Version]-[Processing Date]/[Detector]/`
* `dark/cal-drk-v[Version]-[Processing Date]/[Detector]/`
* `dichroic/base-[Processing Date]/[Detector]/`
* `gain_factors/base-[Processing Date]/`
* `level2/[Planning Period]/l2b-v[Version]-[Processing Date]/[Detector]/`
* `nonfunc/base-[Processing Date]/[Detector]/`
* `nonlinear_pars/base-[Processing Date]/[Detector]/`
* `readnoise_pars/base-[Processing Date]/[Detector]/`
* `spectral_wcs/base-[Processing Date]/[Detector]/`

The content of each subdirectory is described in greater detail in the Data Products section of this user guide and in the SPHEREx Explanatory Supplement.


### Application Program Interfaces (APIs)

IRSA provides API access to SPHEREx Spectral Images through version 2 of the VO Simple Image Access (SIA2) protocol. SIA2 allows users to query for a list of images that satisfy constraints based on position(s) on the sky, band, time, ID, and instrument. The list returned by the service includes data access URLs, which can be used to retrieve some or all of the images in the list using wget or curl. A brief summary of SIA2 for accessing SPHEREx data for IRSA is given below. Additional [documentation on IRSA’s SIA2 service](https://irsa.ipac.caltech.edu/ibe/sia.html) can be found on the IRSA website:

IRSA's generric SIA2 endpoint is:

`https://irsa.ipac.caltech.edu/SIA?`

Users must add a `COLLECTION` parameter to this endpoint to specify which dataset to search.  There are three SPHEREx-related SIA2 collections:

* SPHEREx Quick Release Spectral Image MEFs that are part of the SPHEREx **Wide Survey** can be accessed with: `COLLECTION=spherex_qr`

* SPHEREx Quick Release Spectral Image MEFs that are part of the SPHEREx **Deep Survey** can be accessed with: `COLLECTION=spherex_qr_deep`
  
* SPHEREx Quick Release **Calibration files** can be accessed with: `COLLECTION=spherex_qr_cal`

You can use `wget` or `curl` to submit SIA2 queries from the command line. For example:

* `wget -O example1.csv "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex&POS=circle+164.7+-5.8+0.01&RESPONSEFORMAT=CSV"`

* `curl --output example2.csv "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex&POS=circle+164.7+-5.8+0.01&RESPONSEFORMAT=CSV"`

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
