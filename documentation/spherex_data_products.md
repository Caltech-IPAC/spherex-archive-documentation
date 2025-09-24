# SPHEREx Data Products Available at IRSA

A detailed description of SPHEREx data products available to the public is provided in the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR.pdf).
Here we provide a concise summary of the science, calibration, and additional data products available at IRSA.
This summary includes filenaming conventions, for which we adopt the following definitions:

- `Planning Period` designates the survey plan uploaded to the spacecraft, e.g. `2025W18_2B`.
Each planning period covers approximately 3.5 days of operation.

- `Observation ID` includes the survey planning period and the large
  and small slew counters, e.g. `2025W18_2B_0001_1`. Each large slew
  has a maximum of 4 small slews, so the allowed small slew counter
  range is 1 to 4.  Some large slews will have less than 4 small
  slews.

- `Detector` is an integer from 1 through 6.

- `Version` is the version of this file, e.g. 'l2' for "level 2" data products.

- `Processing Date` includes the year and the number of days into the year, e.g. `2025-164`.


## Main Science Data Product: Spectral Image Multi-Extension FITS Files (MEF)

The main Quick Release data product is the Level 2 Spectral Image MEF.
There are 6 Spectral MEFs (one for each detector) for each sky
pointing. Because data quality assessments are evaluated per spectral
image band, some observations will not include all 6 bands in the
archive.  Each Spectral MEF is approximately 70 MB and contains 6
extensions:

HDU 1: IMAGE
 : Calibrated surface brightness flux density in units of MJy/sr, stored as a 2040 x 2040 image.
   No zodiacal light subtraction is applied.

   The SPHEREx focal plane is split with a dichroic to three short-wavelength and three long-wavelength detector arrays.
   Two focal plane assemblies (FPAs) simultaneously image the sky through a dichroic beam splitter.
   Each FPA contains three 2K x 2K detector arrays placed behind a set of linear variable filters (LVFs), providing narrow-band response with a band center that varies along one axis of the array.
   SPHEREx obtains spectra through multiple exposures, placing a given source at multiple positions in the field of view, where it is measured at multiple wavelengths by repointing the spacecraft.

   * Band 1: λ= 0.75 - 1.09 µm; R=39
   * Band 2: λ= 1.10 - 1.62 µm; R=41
   * Band 3: λ= 1.63 - 2.41 µm; R=41
   * Band 4: λ= 2.42 - 3.82 µm; R=35
   * Band 5: λ= 3.83 - 4.41 µm; R=112
   * Band 6: λ= 4.42 - 5.00 µm; R=128

HDU 2: FLAGS
 : Bitmap of per-pixel status and processing flags, stored as a 2040 x 2040 image.
   The definition of the flags are provided in Table 10 of the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR.pdf).

HDU 3: VARIANCE
 : Variance of calibrated surface brightness flux in units of (MJy/sr)^2, stored as a 2,040 x 2,040 image.

HDU 4: ZODI
 : Modeled zodiacal light background flux in units of MJy/sr, stored as a 2040 x 2040 image.
   This has not been subtracted from the IMAGE extension.

HDU 5: PSF
 : 121 Point-spread functions (PSFs); each PSF is represented as a 101 x 101 image and all 121 are assembled together into a cube.

HDU 6: WCS-WAVE
 : Spectral World Coordinate System (WCS) FITS-compliant lookup table that maps spectral image pixel coordinates to central wavelengths and bandwidths.
   The lookup table consists of 1 row with 3 columns (X, Y, VALUES).

   X and Y are each arrays defining a grid of control points in spectral image pixel space.

   VALUES is an array of two-element arrays: at each (X, Y) control point, the two-element array contains the central wavelength and the corresponding bandwidth.

   :::{note}
   This was originally adopted to support the unique nature of the SPHEREx LVF filters, this rarely-used part of the FITS standard has yet to be implemented by all readers.

   If your FITS client software doesn't automatically recognize this, you can manually determine the central wavelength or bandwidth at an arbitrary pixel location by identifying the four nearest control points and applying bilinear interpolation.
   This method yields values accurate to within approximately 1 nm.
   The information in the WCS-WAVE extension of the Spectral Image MEF is also provided in a stand-alone data product described below in [](#data-products-spectral-wcs).
   The fidelity of the WCS-WAVE lookup table is intended for visualization purposes.
   For science analysis, use the CWAVE and CBAND extensions in the Spectral WCS calibration product.
   :::

*Filename Format:*

- `level2_[Observation ID]_D[Detector]_spx_l2b_v[Version]_[Processing Date].fits`

*Example:*

- `level2_2025W18_2B_0001_1D1_spx_l2b-v12-2025-164.fits`

## Cutouts of Spectral Image MEFs

IRSA enables users to access rectangular cutouts of a SPHEREx Spectral
Image MEF by simply appending a [query
string](https://irsa.ipac.caltech.edu/ibe/cutouts.html) containing
center and size parameters to the image URL. These cutout MEFs contain
the same HDUs as the original Spectral Images (IMAGE, FLAGS, VARIANCE,
ZODI, PSF, WCS-WAVE). However, the IMAGE, FLAGS, VARIANCE, AND ZODI
HDUs have been modified to include only those pixels within the
specified cutout size. The WCS-WAVE HDU has also modified to provide
the correct mapping between the pixels in the cutout to
wavelength. The PSF HDU from the original spectral image is included
unmodified in the cutout MEF.

The spatially-varying PSF is represented as an image cube with 121
planes representing different regions of the original, full Spectral
Image. Users interested in performing photometry on a cutout using the
information in the cutout PSF HDU will need to understand how to find
the most applicable PSF cube plane for each pixel in the cutout. The
steps are described below:

1. Determine the 0-based pixel coordinates of the position of interest
in the IMAGE HDU of the cutout.

2. Determine the 0-based pixel coordinates of the position of interest
in the IMAGE HDU of the original Spectral Image.

```python
xpix_orig = 1 + xpix_cutout - CRPIX1A
ypix_orig = 1 + ypix_cutout - CRPIX2A
```

3. Examine the header of the PSF HDU of the cutout to determine the
PSF zone and cube plane corresponding to the pixel of interest in the original
Spectral Image.

The PSF HDU has a header containing the keywords `XCTR_*`, `YCTR_*`,
`XWID_*`, and `YWID_*`, where * goes from [1 to 121]. To determine if
a pixel in the original Spectral Image falls within a PSF zone, simply
find the closest `XCTR_*` and `YCTR_*` to determine the cube plane
that contains the corresponding PSF for this zone.

**Example:**

Consider this cutout:

`spectral_image_url = "https://irsa.ipac.caltech.edu/ibe/cutout?ra=305.59875000000005&dec=41.14888888888889&size=0.01&path=spherex/qr/level2/2025W18_1B/l2b-v13-2025-198/4/level2_2025W18_1B_0023_2D4_spx_l2b-v13-2025-198.fits"`

`cutout_hdulist = fits.open(spectral_image_url)`

1. Let's say that we are interested in the requested position:

```
ra_deg = 305.59875000000005
dec_deg = 41.14888888888889
```

We can use the WCS header in the cutout to determine that these coordinates correspond to

```
cutout_header = cutout_hdulist[1].header

xpix_cutout, ypix_cutout = wcs.world_to_pixel(SkyCoord(ra=ra, dec=dec, unit="deg"))

print(xpix_cutout, ypix_cutout)

2.180467000669851 2.341315802377096
```

2. We can then use the values of CRPIX1A and CRPIX2A in the cutout header to
calculate what pixels these coordinates correspond to in the original
Spectral Image:

```
CRPIX1A = -220.0
CRPIX2A = -2004.0

xpix_orig = 1 + xpix_cutout - CRPIX1A = 1 + 2.180467000669851 - -220.0 = 223.180467001
ypix_orig = 1 + xpix_cutout - CRPIX2A = 1 + 2.341315802377096 - -2004.0 = 2007.3413158
```

3. Looking at the header of the cutout PSF HDU, we see that the XCTR_* values are:

```
XCTR zone0 = 93.22727273
XCTR zone1 = 278.68181818
XCTR zone2 = 464.13636364
XCTR zone3 = 649.59090909
XCTR zone4 = 835.04545455
XCTR zone5 = 1020.5
XCTR zone6 = 1205.95454545
XCTR zone7 = 1391.40909091
XCTR zone8 = 81576.86363636
XCTR zone9 = 1762.31818182
XCTR zone10 = 1947.77272727
```

and the `YCTR_*` values are:

```
YCTR zone0 = 93.22727273
YCTR zone1 = 278.68181818
YCTR zone2 = 464.13636364
YCTR zone3 = 649.59090909
YCTR zone4 = 835.04545455
YCTR zone5 = 1020.5
YCTR zone6 = 1205.95454545
YCTR zone7 = 1391.40909091
YCTR zone8 = 1576.86363636
YCTR zone9 = 1762.31818182
YCTR zone10 = 1947.77272727
```

Our original pixel coordates of 223.180467001, 2007.3413158 fall
closest to `XCTR` zone1 and `YCTR` zone10. This PSF for this zone is
stored in cube plane 22.


## Calibration Product: Absolute Gain Matrix

The Absolute Gain Matrix products are ~16 MB FITS image files (one per detector) with dimensions 2,040 × 2,040 and units of (MJy/sr) / (e−/s).


*Filename Format:*

- `abs_gain_matrix_D[Detector]_spx_cal-agm-v[Version]-[Processing Date].fits`

*Example:*

- `abs_gain_matrix_D1_spx_cal-agm-v4-2025-161.fits`


## Calibration Product: Exposure-Averaged Point Spread Functions (PSFs)

The Exposure-Averaged Point Spread Functions (PSFs) are ~6 MB FITS cubes (one for each detector) with dimensions 101 × 101 × 121.
Each of the 121 layers represents a "super-resolution" PSF estimate in a different region (defined by an 11x11 grid) of the detector.
Each PSF is a two-dimensional array with size of 101 × 101 pixels.
The PSFs are oversampled such that 10 PSF pixels cover the same spatial extent as one spectral image pixel (0.615 arcsec).


*Filename Format:*

- `average_psf_D[Detector]_spx_cal-psf-v[Version]-[Processing Date].fits`

*Example:*

- `average_psf_D1_spx_cal-psf-v4-2025-161.fits`


## Calibration Product: Dark Current

The Dark Current products are ~16 MB FITS image files (one per detector) with dimensions 2,040 x 2,040 and units of electron/s.


*Filename Format:*

- `dark_D[Detector]_spx_cal-drk-v[Version]-[Processing Date].fits`

*Example:*

- `dark_D1_spx_cal-drk-v4-2025-161.fits`


## Calibration Product: Dichroic

The Dichroic products are ~16 MB FITS image files with dimensions 2,040 x 2,040.
The pixel value is 0 for pixels that are unaffected by flux attenuation due to the dicroic filter and 1 for impacted pixels.
A pixel is considered impacted if the flux attenuation is 50% or higher.
Note that only bands 3 and 4 have any non-zero values.


*Filename Format:*

- `dichroic_D[Detector]_spx_base-[Processing Date].fits`

*Example:*

- `dichroic_D1_spx_base-2025-158.fits`


## Calibration Product: Electronic Gain Factors

The Electronic Gain Factor product is a single YAML file that includes the provenance information for the detectors and a list of 32 gain values per detector.


*Filename Format:*

- `gain_factors_spx_base-[Processing Date].yaml`

*Example:*

- `gain_factors_spx_base-2025-158.yaml`


## Additional Product: Nonfunctional Pixels

The Nonfunctional Pixel products are ~32 MB FITS image files (one per detector) with dimensions 2,040 x 2,040.
Pixel values are 1 for pixels known to be permanently non-functioning and 0 otherwise.


*Filename Format:*

- `nonfunc_D[Detector]_spx_base-[Processing Date].fits`

*Example:*

- `nonfunc_D1_spx_base-2025-158.fits`


## Additional Product: Nonlinearity Parameters

The Nonlinearity Parameter products are ~79 MB multi-extension FITS files (one per detector).
Each file contains 5 extensions (Q_nl, b1, b2, b3, Qmax), each of which is an image with dimensions 2,040 x 2,040.
These extensions are described in Section 3.2.1 of the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR.pdf).


*Filename Format:*

- `nonlinear_pars_D[Detector]_spx_base-[Processing Date].fits`

*Example:*

- `nonlinear_pars_D1_spx_base-2025-158.fits`


## Additional Product: Read Noise Parameters

The Read Noise Parameters products are ~48 MB multi-extension FITS files (one per detector).
Each file has 2 extensions: READNOISE-1 and READNOISE-2.
Each extension is an image with dimensions 2040 × 2040 and units of electrons.


*Filename Format:*

- `readnoise_pars_D[Detector]_spx_base-[Processing Date].fits`

*Example:*

- `readnoise_pars_D1_spx_base-2025-158.fits`

(data-products-spectral-wcs)=
## Additional Product: Spectral WCS

The Spectral WCS products are ~32 MB multi-extension FITS files (one per detector).
Each file has 3 extensions: CWAVE, CBAND, and WCS-WAVE.
For science analysis, use the values in the CWAVE and CBAND layers, not the WCS-WAVE which is intended for visualization.

CWAVE is an image with dimensions 2,040 x 2,040.
It contains the central wavelength in microns for each pixel.

CBAND is an image with dimensions 2,040 x 2,040.
It contains the bandwidth in microns for each pixel.

WCS-WAVE is a table with 3 columns (X, Y, VALUES) and 1 row.
This is equivalent to the WCS-WAVE extension in the Spectral Image MEF file described above.


*Filename Format:*
- `spectral_wcs_D[Detector]_spx_base-[Processing Date].fits`

*Example:*

- `rspectral_wcs_D1_spx_base-2025-158.fits`
