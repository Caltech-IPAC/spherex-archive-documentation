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
* **Absolute Gain Matrix:** `abs_gain_matrix/cal-agm-v[Version]-[Processing Date]/[Detector]/`
* **Exposure-Averaged Point Spread Functions (PSFs):** `average_psf/cal-psf-v[Version]-[Processing Date]/[Detector]/`
* **Dark Current:** `dark/cal-drk-v[Version]-[Processing Date]/[Detector]/`
* **Dichroic:** `dichroic/base-[Processing Date]/[Detector]/`
* **Electronic Gain Factors:** `gain_factors/base-[Processing Date]/`
* **Spectral Image Multi-Extension FITS Files (MEFs):** `level2/[Planning Period]/l2b-v[Version]-[Processing Date]/[Detector]/`
* **Nonfunctional Pixels:** `nonfunc/base-[Processing Date]/[Detector]/`
* **Nonlinearity Parameters:** `nonlinear_pars/base-[Processing Date]/[Detector]/`
* **Read Noise Parameters:** `readnoise_pars/base-[Processing Date]/[Detector]/`
* **Spectral WCS:** `spectral_wcs/base-[Processing Date]/[Detector]/`

The content of each subdirectory is described in greater detail in the Data Products section of this user guide and in the SPHEREx Explanatory Supplement.


### Application Program Interfaces (APIs)

IRSA provides API access to SPHEREx Spectral Images through version 2 of the VO Simple Image Access (SIA2) protocol. SIA2 allows users to query for a list of images that satisfy constraints based on position(s) on the sky, band, time, ID, and instrument. The list returned by the service includes data access URLs, which can be used to retrieve some or all of the images in the list using wget or curl. A brief summary of SIA2 for accessing SPHEREx data for IRSA is given below. Additional [documentation on IRSA’s SIA2 service](https://irsa.ipac.caltech.edu/ibe/sia.html) can be found on the IRSA website:

Note: SPHEREx data are ingested on a weekly basis. Due to the nature of the ingestion process, new SPHEREx data will first be available in the browsable directories and in the SPHEREx Data Explorer GUI. Availability via SIA2 and Python libraries like Astroquery and PyVO will lag on the order of a day.

IRSA's generric SIA2 endpoint is:

`https://irsa.ipac.caltech.edu/SIA?`

Users must add a `COLLECTION` parameter to this endpoint to specify which dataset to search.  There are three SPHEREx-related SIA2 collections:

* SPHEREx Quick Release Spectral Image MEFs that are part of the SPHEREx **Wide Survey** can be accessed with: `COLLECTION=spherex_qr`

* SPHEREx Quick Release Spectral Image MEFs that are part of the SPHEREx **Deep Survey** can be accessed with: `COLLECTION=spherex_qr_deep`
  
* SPHEREx Quick Release **Calibration files** can be accessed with: `COLLECTION=spherex_qr_cal`

You can use `wget` or `curl` to submit SIA2 queries from the command line. For example:

* `wget -O example1.html "https://irsatest.ipac.caltech.edu/SIA?COLLECTION=spherex_qr&POS=circle+127.69444+-39.17760+0.01&RESPONSEFORMAT=HTML"`

See the next section to learn how to use Python wrappers around IRSA’s SIA2 service.

### Python packages: PyVO & Astroquery

If you would like to take advantage of IRSA’s SIA2 service for querying SPHEREx images, but prefer to use Python rather than the command line, you may be interested in using one of two Python libraries:

*	**PyVO**  -- This module lets you find and retrieve astronomical data available from archives that support standard IVOA protocols.
*	**Astroquery**  -- This module provides access to IRSA's public astrophysics data from projects such as SPHEREx, Euclid, Spitzer, WISE/NEOWISE, SOFIA, IRTF, 2MASS, Herschel, IRAS, and ZTF.

Examples of data queries using both of these libraries can be found in [IRSA’s Python Notebook Tutorial Repository](https://caltech-ipac.github.io/irsa-tutorials/):

### SPHEREx Data Explorer Web Application

Users who prefer an interactive graphical user interface (GUI) for specifying search constraints, submitting queries, and visualizing the results should consider the [SPHEREx Data Explorer](https://irsa.ipac.caltech.edu/applications/spherex), which includes its own context-sensitive help.
