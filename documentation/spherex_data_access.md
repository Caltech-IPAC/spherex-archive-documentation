(data-access)=
# SPHEREx Data Access

IRSA serves SPHEREx data from two locations: (1) on-premises at IPAC; and (2) on the cloud via Amazon Web Services (AWS).
IRSA provides layered access to these data to support a variety of use cases and users.
These layers include:

- **Browsable Directories:** SPHEREx on-premises data products are laid out in directories that can be navigated with standard web browsers.
  These data products are mirrored on AWS.
- **Application Program Interfaces:** IRSA provides program-friendly Application Program Interfaces (APIs) to access SPHEREx Spectral Image and All-Sky Cube data.
  The on-premises and cloud-hosted DR1 and QR3 Spectral Images and DR1 All-Sky Cube FITS files are accessible via the [Simple Image Access V2 protocol](https://ivoa.net/documents/SIA/20151223/) defined by the International Virtual Observatory Alliance ([IVOA](https://ivoa.net)).
  Cutouts of the Spectral Image data held on-premises are available via IRSA's Cutout Service.
- **Python Packages:** SPHEREx data at IRSA are accessible via the Python packages [pyvo](https://pyvo.readthedocs.io/en/latest/) and [astroquery](https://astroquery.readthedocs.io/en/latest/ipac/irsa/irsa.html).
- **SPHEREx Data Explorer:** IRSA provides a web-based Graphical User Interface (GUI) that makes it easy to search for, visualize, and download SPHEREx data.
  This tool provides access to the on-premises copy of the data.

Each of these data access layers is described in greater detail in the subsections below.

(browsable-directories)=
## Browsable Directories

SPHEREx data products are laid out in directories that can be navigated with standard web browsers.
This is convenient for users to get a quick sense of the types of data products that are available, to quickly download some examples by clicking through the directory tree, and to script bulk downloads using `wget` or `curl`.

The root of the SPHEREx on-premises data directories is: [https://irsa.ipac.caltech.edu/ibe/data/spherex/](https://irsa.ipac.caltech.edu/ibe/data/spherex/).
All of the data products are also available on the cloud via AWS.
Please see our [instructions for accessing on-cloud SPHEREx data](https://irsa.ipac.caltech.edu/cloud_access/#spherex).

There is one subdirectory per data release: `dr1`, `qr3`, and `qr2`.
QR2 data remain available for direct download through February 2027 but are no longer searchable.
Under each, the public data products are organized into subdirectories based on the organizational scheme listed below.
The content of each subdirectory and the filename formats are described in greater detail in the [Data Products](#data-products) section of this user guide and in the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp.pdf).

- **Spectral Image Multi-Extension FITS Files (MEFs):** `level2/[Planning Period]/l2b-v[Version]-[Processing Date]/[Detector]/`
- **All-Sky Cube:** (DR1 only) `hips5_cube/hips_20261026/Norder5/Dir[Directory Number]/`
- **Absolute Gain Matrix:** `abs_gain_matrix/cal-agm-v[Version]-[Processing Date]/[Detector]/`
- **Auroral Line Template:** (DR1 and QR3 only) `aurora_template/base-[Processing Date]/[Detector]/`
- **Exposure-Averaged Point Spread Functions (PSFs):** (QR2 only) `average_psf/cal-psf-v[Version]-[Processing Date]/[Detector]/`
- **Dark Current:** `dark/cal-drk-v[Version]-[Processing Date]/[Detector]/`
- **Dichroic:** `dichroic/base-[Processing Date]/[Detector]/`
- **Effective Point Spread Functions (ePSFs):** (DR1 and QR3 only) `epsf/cal-epsf-v[Version]-[Processing Date]/[Detector]/`
- **Electronic Gain Factors:** `gain_factors/base-[Processing Date]/`
- **He Emission Template:** (DR1 and QR3 only) `he_template/base-[Processing Date]/[Detector]/`
- **Flux Corrections:** (DR1 and QR3 only) `l3_flux_corrections/cal-flxc-v[Version]-[Processing Date]/[Detector]/`
- **Nonfunctional Pixels:** `nonfunc_v2/base-[Processing Date]/[Detector]/` (DR1 and QR3) or `nonfunc/base-[Processing Date]/[Detector]/` (QR2)
- **Nonlinearity Parameters:** `nonlinear_pars/base-[Processing Date]/[Detector]/`
- **Read Noise Parameters:** `readnoise_pars/base-[Processing Date]/[Detector]/`
- **Shuttle Glow Template:** (DR1 and QR3 only) `shuttle_glow_template/base-[Processing Date]/[Detector]/`
- **Simple Imaging Polynomials (SIP):** `sip/cal-sip-v[Version]-[Processing Date]/[Detector]/`
- **Solid Angle Pixel Map:** `solid_angle_pixel_map/cal-sapm-v[Version]-[Processing Date]/[Detector]/`
- **Spectral Channels:** `spectral_channels/cal-sch-v[Version]-[Processing Date]/`
- **Spectral WCS:** `spectral_wcs/cal-wcs-v[Version]-[Processing Date]/[Detector]/`
- **Crosstalk Parameters:** (DR1 and QR3 only) `xtalk_class[Crosstalk Type]/base-[Processing Date]/[Detector]/`
- **Zodi Scaling:** (DR1 and QR3 only) `zodi_scaling_v[Version]/cal-zodi-v[Version]-[Processing Date]/[Detector]/`

(apis)=
## Application Program Interfaces (APIs)

### IVOA Simple Image Access V2 Protocol

IRSA provides API access to SPHEREx Spectral Image Multi-Extension FITS files (MEFs) and All-Sky Cube FITS files through [version 2 of the VO Simple Image Access (SIA2) protocol](https://ivoa.net/documents/SIA/20151223/).
SIA2 allows users to query for a list of images that satisfy constraints based on position(s) on the sky, band, time, ID, and instrument.

:::{note}
Calibration files are not available via SIA2.
They can be retrieved from the [](#browsable-directories) described above.
:::

The table returned by the SIA2 service includes an `access_url` column containing a data access URL for each image.
These can be used to retrieve the on-premises images using `wget` or `curl`.
The returned table also includes a `cloud_access` column containing cloud-hosted data access information.
The Python tutorial notebooks [IRSA Cloud Access Introduction](https://caltech-ipac.github.io/irsa-tutorials/cloud-access-intro) and [SPHEREx Source Discovery Tool](https://caltech-ipac.github.io/irsa-tutorials/spherex-source-discovery-tool-demo/) include examples that show how to use the `cloud_access` information.

A brief summary of using SIA2 to access SPHEREx data at IRSA is given below.
Additional [documentation on IRSA’s SIA2 service](https://irsa.ipac.caltech.edu/ibe/sia.html) can be found on the IRSA website.

:::{note}
SPHEREx data are ingested on a weekly basis.
Due to the nature of the ingestion process, new SPHEREx data will first be available in the browsable directories, the SPHEREx Data Explorer GUI, and certain TAP queries (see the [cutouts notebook](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/) for a TAP example).
Availability via SIA2 will lag on the order of a day.
:::

IRSA's generic SIA2 endpoint is:

`https://irsa.ipac.caltech.edu/SIA?`

Users must add a `COLLECTION` parameter to this endpoint to specify which dataset to search.
There are five SPHEREx-related SIA2 collections:

- SPHEREx DR1 Spectral Image MEFs that are part of the SPHEREx **Wide Survey** can be accessed with: `COLLECTION=spherex_dr1`.
  Use this collection if you are interested in more uniform coverage across the entire sky and want to ignore the additional coverage in the deep fields.

- SPHEREx DR1 Spectral Image MEFs that are part of the SPHEREx **Deep Survey** can be accessed with: `COLLECTION=spherex_dr1_deep`.

- SPHEREx DR1 All-Sky Cube FITS files can be accessed with: `COLLECTION=spherex_dr1_cube`.

- SPHEREx QR3 Spectral Image MEFs that are part of the SPHEREx **Wide Survey** can be accessed with: `COLLECTION=spherex_qr3`.
  Use this collection if you are interested in more uniform coverage across the entire sky and want to ignore the additional coverage in the deep fields.

- SPHEREx QR3 Spectral Image MEFs that are part of the SPHEREx **Deep Survey** can be accessed with: `COLLECTION=spherex_qr3_deep`.

DR1 and QR3 together supersede QR2, so to search all current SPHEREx Spectral Images, search both `spherex_dr1` and `spherex_qr3` (and the corresponding `_deep` collections if you want the deep fields).
QR2 data are not searchable via SIA2.

You can use `wget` or `curl` to submit SIA2 queries from the command line.
For example:

```bash
wget -O spherex-example1.html "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex_qr3&POS=circle+127.69444+-39.17760+0.01&RESPONSEFORMAT=HTML"
```

or:

```bash
curl -o spherex-example2.html "https://irsa.ipac.caltech.edu/SIA?COLLECTION=spherex_dr1&POS=circle+127.69444+-39.17760+0.01&RESPONSEFORMAT=HTML"
```

See the section on {ref}`Python packages <access-python-packages>` to learn how to use Python wrappers around IRSA’s SIA2 service.

(access-spectral-image-cutouts)=
### Cutouts of SPHEREx Spectral Image MEFs

If you have identified the access URL for an on-premises Spectral Image MEF using SIA2 as described above, you can request a cutout of this MEF by appending a query string containing the center and size parameters.
The parameters are described in more detail at [https://irsa.ipac.caltech.edu/ibe/cutouts.html](https://irsa.ipac.caltech.edu/ibe/cutouts.html).

**Example:**

```bash
curl -o cutout.fits "https://irsa.ipac.caltech.edu/ibe/data/spherex/qr3/level2/2026W21_2A/l2b-v27-2026-268/1/level2_2026W21_2A_0001_2D1_spx_l2b-v27-2026-268.fits?center=337.8783221,-5.1891588&size=0.1"
```

This cutout service is also invoked by the SPHEREx Data Explorer when users select the cutout option upon download.

This cutout service can also be invoked via Python, as illustrated in the Python Tutorial notebook titled [Download a collection of SPHEREx Spectral Image cutouts as a multi-extension FITS file](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/).
Information on how to work with the ePSF extension in DR1 and QR3 cutouts is provided in the {ref}`products-spectral-image-cutouts` section of this User Guide and demonstrated in the Python Tutorial notebook titled [Understanding and Extracting the ePSF Extension in a SPHEREx Cutout](https://caltech-ipac.github.io/irsa-tutorials/spherex-psf/).

(access-python-packages)=
## Python Packages

For Python access to IRSA’s VO-compliant [API services](#apis), we recommend the following libraries:

- [Astroquery](https://astroquery.readthedocs.io/en/latest/ipac/irsa/irsa.html): The `astroquery.ipac.irsa` module provides convenient functions for searching IRSA’s images (SIA2), catalogs (TAP), and spectra (SSA), including the SPHEREx collections listed in [APIs](#apis).
  We recommend it for most users.
- [PyVO](https://pyvo.readthedocs.io/en/latest/): PyVO is a general-purpose library for VO services at IRSA and at any other archive that supports the standard IVOA protocols.
  Use PyVO when you want lower-level access to the services than Astroquery provides, or want to use the same code to query several archives.

IRSA’s [Python Tutorial Notebooks: SPHEREx](https://caltech-ipac.github.io/irsa-tutorials/spherex) contain many examples of how to access and analyze SPHEREx data.
For example:

- The notebook titled [Introduction to SPHEREx Spectral Images](https://caltech-ipac.github.io/irsa-tutorials/spherex-intro/) shows how to use the Astroquery library to execute an IVOA Simple Image Access (SIA2) query for SPHEREx spectral images that cover the specified coordinates and collection.
- The notebook titled [Download a collection of SPHEREx Spectral Image cutouts as a multi-extension FITS file](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/#id-5-query-irsa-for-a-list-of-cutouts-that-satisfy-the-criteria-specified-above) demonstrates how to use the PyVO library to execute an IVOA Table Access Protocol (TAP) query for SPHEREx spectral images that cover the specified coordinates and match the specified bandpass.

:::{note}
SPHEREx data are ingested on a weekly basis.
Due to the nature of the ingestion process, new SPHEREx data will first be available in the browsable directories, the SPHEREx Data Explorer GUI, and certain TAP queries (see the [cutouts notebook](https://caltech-ipac.github.io/irsa-tutorials/spherex-cutouts/) for a TAP example).
Availability via SIA2 will lag on the order of a day.
:::

## SPHEREx Data Explorer Web Application

Users who prefer an interactive graphical user interface (GUI) for specifying search constraints, submitting queries, and visualizing the results should consider the [SPHEREx Data Explorer](https://irsa.ipac.caltech.edu/applications/spherex), which includes its own context-sensitive help.
