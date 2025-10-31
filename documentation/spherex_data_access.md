(data-access)=
# SPHEREx Data Access

IRSA serves SPHEREx data from two locations: (1) on premises at IPAC; and (2) on the cloud via Amazon Web Services (AWS).
IRSA provides layered access to these data to support a variety of use cases and users.
These layers include:

* **Browsable Directories:** SPHEREx on-premises data products are laid out in directories that can be navigated with standard web browsers.
These data products are mirrored on AWS.
* **Application Program Interfaces:** IRSA provides program-friendly Application Program Interfaces (APIs) to access SPHEREx Spectral Image data.
The on-prem and cloud-hosted Quick Release 2 Spectral Images that have been released thus far are accessible via the [Simple Image Access V2 protocol](https://ivoa.net/documents/SIA/20151223/) defined by the International Virtual Observatory Alliance ([IVOA](https://ivoa.net)).
Cutouts of the Spectral Image data held on-prem are available via IRSA's Cutout Service.
* **Python Packages:** SPHEREx data at IRSA are accessible via the Python packages [pyvo](https://pyvo.readthedocs.io/en/latest/) and [astroquery](https://astroquery.readthedocs.io/en/latest/ipac/irsa/irsa.html).
* **SPHEREx Data Explorer:** IRSA provides a web-based Graphical User Interface (GUI) that makes it easy to search for, visualize, and download SPHEREx data.
This tool provides access to the on-prem copy of the data.

Each of these data access layers is described in greater detail in the subsections below.

## Browsable Directories

SPHEREx data products are laid out in directories that can be navigated with standard web browsers.
This is convenient for users to get a quick sense of the types of data products that are available, to quickly download some examples by clicking through the directory tree, and to script bulk downloads using `wget` or `curl`.

The root of the SPHEREx QR2 on-premises data directories is: [https://irsa.ipac.caltech.edu/ibe/data/spherex/qr2](https://irsa.ipac.caltech.edu/ibe/data/spherex/qr2).
For QR1, replace '/qr2' with '/qr'.
Note that QR1 is superseded by QR2 and only available through January 2026.
All of the data products are also available on the cloud via AWS.
Please see our [instructions for accessing cloud-hosted SPHEREx data](https://irsa.ipac.caltech.edu/cloud_access/#spherex).

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
* **Solid Angle Pixel Map:** `solid_angle_pixel_map/cal-sapm-v[Version]-[Processing Date]/[Detector]/`
* **Spectral WCS:** `spectral_wcs/cal-wcs-v[Version]-[Processing Date]/[Detector]/` (QR2) or `spectral_wcs/base-[Processing Date]/[Detector]/` (QR1)

The content of each subdirectory and the filename formats are described in greater detail in the {ref}`Data Products <data-products>` section of this user guide and in the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR.pdf).

## Application Program Interfaces (APIs)

### IVOA Simple Image Access V2 Protocol

IRSA provides API access to SPHEREx Spectral Image Multi-Extension FITS files (MEFs) and associated calibration files through [version 2 of the VO Simple Image Access (SIA2) protocol](https://ivoa.net/documents/SIA/20151223/).
SIA2 allows users to query for a list of images that satisfy constraints based on position(s) on the sky, band, time, ID, and instrument.
The list returned by the service includes a data access URL for each image.
These can be used to retrieve the on-prem-hosted images using `wget` or `curl`. The returned list also returns cloud access information.
A brief summary of SIA2 for accessing SPHEREx data for IRSA is given below.
Additional [documentation on IRSA’s SIA2 service](https://irsa.ipac.caltech.edu/ibe/sia.html) can be found on the IRSA website.

:::{note}
SPHEREx data are ingested on a weekly basis.
Due to the nature of the ingestion process, new SPHEREx data will first be available in the browsable directories, the SPHEREx Data Explorer GUI, and certain TAP queries (see the [cutouts notebook](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/) for a TAP example).
Availability via SIA2 will lag on the order of a day.
:::

IRSA's generic SIA2 endpoint is:

`https://irsa.ipac.caltech.edu/SIA?`

Users must add a `COLLECTION` parameter to this endpoint to specify which dataset to search.
There are three SPHEREx-related SIA2 collections:

* SPHEREx QR2 Spectral Image MEFs that are part of the SPHEREx **Wide Survey** can be accessed with: `COLLECTION=spherex_qr2`.
  Use this collection if you are interested in more uniform coverage across the entire sky and want to ignore the additional coverage in the deep fields.

* SPHEREx QR2 Spectral Image MEFs that are part of the SPHEREx **Deep Survey** can be accessed with: `COLLECTION=spherex_qr2_deep`.

* SPHEREx QR2 **Calibration files** can be accessed with: `COLLECTION=spherex_qr2_cal`.

You can use `wget` or `curl` to submit SIA2 queries from the command line.
For example:

* `wget -O example1.html "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex_qr2&POS=circle+127.69444+-39.17760+0.01&RESPONSEFORMAT=HTML"`

See the section on Python packages to learn how to use Python wrappers around IRSA’s SIA2 service.

(access-spectral-image-cutouts)=
### Cutouts of SPHEREx Spectral Image MEFs

If you have identified the access URL for an on-premises Spectral Image MEF using SIA2 as described above, you can request a cutout of this MEF by appending a query string containing the center and size parameters.
The parameters are described in more detail at [https://irsa.ipac.caltech.edu/ibe/cutouts.html](https://irsa.ipac.caltech.edu/ibe/cutouts.html).

**Example:**

`curl -o cutout.fits "https://irsa.ipac.caltech.edu/ibe/data/spherex/qr2/level2/2025W19_2B/l2b-v20-2025-247/3/level2_2025W19_2B_0073_2D3_spx_l2b-v20-2025-247.fits?center=156.09328159,-41.64466331&size=0.1"`

This cutout service is also invoked by the SPHEREx Data Collection Explorer Spectral Image Search when users select the cutout option upon download.

This cutout service can also be invoked via Python, as illustrated in the Python Tutorial notebook titled [Download a collection of SPHEREx Spectral Image cutouts as a multi-extension FITS file](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/).
Information on how to work with the PSF extension in these cutouts is documented in the {ref}`products-spectral-image-cutouts` of this User Guide and demonstrated in the Python Tutorial notebook titled [Understanding and Extracting the PSF Extension in a SPHEREx Cutout](https://caltech-ipac.github.io/irsa-tutorials/spherex-psf/).

## Python packages: PyVO & Astroquery

If you would like to take advantage of IRSA’s SIA2 service for querying SPHEREx images, but prefer to use Python rather than the command line, you may be interested in using one of two Python libraries:

[PyVO](https://github.com/astropy/pyvo)
 : This module lets you find and retrieve astronomical data available from archives that support standard IVOA protocols.

[Astroquery](https://github.com/astropy/astroquery)
 : This module provides access to IRSA's public astrophysics data from projects such as SPHEREx, Euclid, Spitzer, WISE/NEOWISE, SOFIA, IRTF, 2MASS, Herschel, IRAS, and ZTF.

Examples of data queries using both of these libraries can be found in [IRSA’s Python Notebook Tutorial Repository](https://caltech-ipac.github.io/irsa-tutorials/). For example:

The notebook titled [Introduction to SPHEREx Spectral Images](https://caltech-ipac.github.io/irsa-tutorials/spherex-intro/) shows how to use the Astroquery library to execute an IVOA Simple Image Access (SIA2) query for SPHEREx spectral images that cover the specified coordinates and collection.

The notebook titled [Download a collection of SPHEREx Spectral Image cutouts as a multi-extension FITS file](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/#id-5-query-irsa-for-a-list-of-cutouts-that-satisfy-the-criteria-specified-above) demonstrates how to use the PyVO library to execute an IVOA Table Access Protocol (TAP) query for SPHEREx spectral images that cover the specified coordinates and match the specified bandpass.

:::{note}
SPHEREx data are ingested on a weekly basis.
Due to the nature of the ingestion process, new SPHEREx data will first be available in the browsable directories, the SPHEREx Data Explorer GUI, and certain TAP queries (see the [cutouts notebook](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/) for a TAP example).
Availability via SIA2 will lag on the order of a day.
:::

## SPHEREx Data Explorer Web Application

Users who prefer an interactive graphical user interface (GUI) for specifying search constraints, submitting queries, and visualizing the results should consider the [SPHEREx Data Explorer](https://irsa.ipac.caltech.edu/applications/spherex), which includes its own context-sensitive help.
