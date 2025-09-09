# SPHEREx Data Products Available at IRSA

A detailed description of SPHEREx data products available to the public is provided in the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR_v1.0.pdf).
Here we provide a concise summary of the science, calibration, and additional data products available at IRSA.
This summary includes filenaming conventions, for which we adopt the following definitions:

- `Planning Period` designates the survey plan uploaded to the spacecraft, e.g. `2025W18_2B`.
Each planning period covers approximately 3.5 days of operation.

- `Observation ID` includes the survey planning period and the large and small slew counters, e.g. `2025W18_2B_0001_1`.

- `Detector` is an integer from 1 through 6.

- `Version` is the version of this file, e.g. 'l2' for "level 2" data products.

- `Processing Date` includes the year and the number of days into the year, e.g. `2025-164`.


## Main Science Data Product: Spectral Image Multi-Extension FITS Files (MEF)

The main Quick Release data product is the Level 2 Spectral Image MEF.
There are 6 Spectral MEFs (one for each detector) for each sky pointing.
Each Spectral MEF is approximately 70 MB and contains 6 extensions:

IMAGE
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

FLAG
 : Bitmap of per-pixel status and processing flags, stored as a 2040 x 2040 image.
   The definition of the flags are provided in Table 8 of the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR_v1.0.pdf).

VARIANCE
 : Variance of calibrated surface brightness flux in units of (MJy/sr)^2, stored as a 2,040 x 2,040 image.

ZODI
 : Modeled zodiacal light background flux in units of MJy/sr, stored as a 2040 x 2040 image.
   This has not been subtracted from the IMAGE extension.

PSF
 : 121 Point-spread functions (PSFs); each PSF is represented as a 101 x 101 image and all 121 are assembled together into a cube.

WCS-WAVE
 : Spectral World Coordinate System (WCS) FITS-compliant lookup table that maps spectral image pixel coordinates to central wavelengths and bandwidths.
   The lookup table consists of 1 row with 3 columns (X, Y, VALUES).

   X and Y are each arrays defining a grid of control points in spectral image pixel space.

   VALUES is an array of two-element arrays: at each (X, Y) control point, the two-element array contains the central wavelength and the corresponding bandwidth.

   :::{note}
   This was originally adopted to support the unique nature of the SPHEREx LVF filters, this rarely-used part of the FITS standard has yet to be implemented by all readers.

   If your FITS client software doesn't automatically recognize this, you can manually determine the central wavelength or bandwidth at an arbitrary pixel location by identifying the four nearest control points and applying bilinear interpolation.
   This method yields values accurate to within approximately 1 nm.
   The information in the WCS-WAVE extension of the Spectral Image MEF is also provided in a stand-alone data product described below ("Additional Product: Spectral WCS").
   The fidelity of the WCS-WAVE lookup table is intended for visualization purposes.
   For science analysis, use the CWAVE and CBAND extensions in the Spectral WCS calibration product.
   :::

*Filename Format:*

- `level2_[Observation ID]_D[Detector]_spx_l2b_v[Version]_[Processing Date].fits`

*Example:*

- `level2_2025W18_2B_0001_1D1_spx_l2b-v12-2025-164.fits`


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
These extensions are described in Section 3.2.1 of the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR_v1.0.pdf).


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
