# SPHEREx Archive at IRSA User Guide
Last updated 24 April 2025

[toc]

## Introduction

### Document Purpose and Scope
The purpose of this document is to facilitate science with SPHEREx data by providing users with an overview of the SPHEREx data that are available at the NASA/IPAC Infrared Science Archive (IRSA) at Caltech, as well as instructions for accessing and downloading these data. We also provide tips for exploring the data and getting help with any questions you may have. This User Guide will evolve as the SPHEREx project delivers new data products and tools to IRSA to make available to the public.

### SPHEREx Overview

SPHEREx is a NASA Astrophysics Medium Explorer mission that launched in March 2025. During its planned two-year mission, SPHEREx will obtain 0.75-5 micron spectroscopy over the entire sky, with deeper data in the SPHEREx Deep Fields. SPHEREx data will be used to:

* **constrain the physics of inflation** by measuring its imprints on the three-dimensional large-scale distribution of matter,
* **trace the history of galactic light production** through a deep multi-band measurement of large-scale clustering,
* **investigate the abundance and composition of water and biogenic ices** in the early phases of star and planetary disk formation.

The community will also mine SPHEREx data and combine it with synergistic data sets to address a variety of additional topics in astrophysics.

More information is available in the "Mission Overview" section of the SPHEREx Explanatory Supplement.

### Additional Resources

SPHEREx archive at IRSA:
https://irsa.ipac.caltech.edu/Missions/spherex.html

SPHEREx project website: https://spherex.caltech.edu/

SPHEREx Explanatory Supplement:
https://irsa.ipac.caltech.edu/data/SPHEREx/docs/spherex_explanatory_supplement.pdf

## SPHEREx Data Products Available at IRSA

A detailed description of SPHEREx data products available to the public is provided in Section 2 ("The SPHEREx Data Products") of the SPHEREx Explanatory Supplement. Here we provide a concise summary.

### Spectral Multi-Extension FITS (MEF)

The main Quick Release data product is the Spectral Multi-Extension FITS file (MEF). Each Spectral MEF contains 6 extensions:

1. **IMAGE** - Calibrated surface brightness flux density in units of MJy/sr, stored as a 2040 x 2040 image.

2. **FLAG** - Bitmap of per-pixel status and processing flags, stored as a 2040 x 2040 image. The definition of the flags are provided in Table 8 of the SPHEREx Explanatory Supplement.

3. **VARIANCE** - Variance of calibrated surface brightness flux in units of (MJy/sr)^2, stored as a 2,040 x 2,040 image.

4. **ZODI** - Estimated zodiacal light background flux in units of MJy/sr, stored as a 2040 x 2040 image.

5. **PSF** - 121 Point-spread functions (PSFs); each PSF is represented as a 101 x 101 image and all 121 are assembled together into a cube.

6. **WCS-WAVE** - Spectral World Coordinate System (WCS) lookup table that maps spectral image pixel coordinates to central wavelengths and bandwidths. The lookup table consists of 1 row with 3 columns (X, Y, VALUES). X and Y are each arrays of length 7, defining a 7x7 grid of control points in spectral image pixel space. VALUES is a 7x7 array of two-element arrays: at each (X, Y) control point, the two-element array contains the central wavelength and the corresponding bandwidth. To determine the central wavelength or bandwidth at an arbitrary pixel location, identify the four nearest control points and apply bilinear interpolation. This method yields values accurate to within approximately 1 nm.



## SPHEREx Data Access

IRSA serves SPHEREx data both on premises at IPAC and in the cloud via Amazon Web Services (AWS). IRSA provides layered access to these data to support a variety of use cases and users. These layers include:

* **Browsable Directories:** SPHEREx on-premises data products are laid out in directories that can be navigated with standard web browsers.
* **Cloud Access:** SPHEREx data are available in Amazon Web Services (AWS) Open Data Repository (ODR).
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

Within each detector directory are the spectral image MEFs, which adhere to the following filename convention:

`level1_[Observation ID]_D[Detector Number]_spx_l2b_v4_[Processing Date]`

where 

`Observation ID` includes the survey planning period and the large and small slew counters

`Detector Number` is an integer from 1 through 6

`Processing Date` includes the year and the number of days into the year

An example is `level2_2025W22_2B_0001_1D3_spx_l2b-v4-2025-152.fits`

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

### Cloud Access

SPHEREx data are available in Amazon Web Services (AWS) Open Data Repository (ODR). Downloads from AWS can be made without logging in and without incurring any egress costs. Information on how to access these data are available at IRSA’s Cloud Data Access webpage:

 https://irsa.ipac.caltech.edu/cloud_access/

### Bulk Downloads

Users interested in downloading large data volumes should plan for long download times and substantial local storage. IRSA has staged SPHEREx data both on premises at IPAC and in the cloud using AWS. IRSA’s synchronous data services, including the SIA and TAP APIs and the SPHEREx Data Explorer, rely on the on-premises copy of the SPHEREx data. To avoid interfering with the use of these synchronous services, we recommend that users download large amounts of data from the AWS copy.


The minimum information you need to download data from AWS are:

* bucket name
* prefix

For SPHEREx, bucket name = nasa-irsa-spherex-qr

Each subdirectory has a different prefix:

qr/level2

Once you have identified the bucket name and prefix of the directory or file you wish to download, you can use the AWS Command Line Interface (CLI):

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

* **Example 1:** List the files in a directory
```
aws s3 ls --no-sign-request s3://nasa-irsa-spherex-q3/q3/level2/
```
    
* **Example 2:** Synchronize the contents of a bucket with a directory on your own machine, but just as a dry run, to see what would happen
```
aws s3 sync --no-sign-request --dryrun s3://nasa-irsa-spherex-
qr/qr/level2/ .
```

* **Example 3:** synchronize the contents of a bucket with a directory on your own 
```
aws s3 sync --no-sign-request s3://nasa-irsa-spherex-qr/qr/level2/ .
```

* **Example 4:** Copy a single file from a bucket to your own machine
```
aws s3 cp --no-sign-request s3://nasa-irsa-spherex-qr/qr/level2/CAW.fits .
```

* **Example 5:** Alter download script from SPHEREx Data Explorer to pull data from cloud instead of from on-prem at IPAC
```
curl "https://irsa.ipac.caltech.edu/ibe/data/spherex/qr/level2/caw.fits" -o caw.fits
```
turns into:
```
aws s3 cp --no-sign-request --dryrun s3://nasa-irsa-spherex-qr/qr/level2/caw.fits .
```






