## SPHEREx Data Products Available at IRSA

A detailed description of SPHEREx data products available to the public is provided in Section 2 ("The SPHEREx Data Products") of the SPHEREx Explanatory Supplement. Here we provide a concise summary of the science and calibration data products available at IRSA.

### Main Science Data Product: Spectral Image Multi-Extension FITS Files (MEF)

The main Quick Release data product is the Spectral Image MEF. There are 6 Spectral MEFs (one for each detector) for each sky pointing. Each Spectral MEF is approximately 70 MB and contains 6 extensions:

1. **IMAGE** - Calibrated surface brightness flux density in units of MJy/sr, stored as a 2040 x 2040 image. No zodiacal light subtraction is applied.

2. **FLAG** - Bitmap of per-pixel status and processing flags, stored as a 2040 x 2040 image. The definition of the flags are provided in Table 8 of the SPHEREx Explanatory Supplement.

3. **VARIANCE** - Variance of calibrated surface brightness flux in units of (MJy/sr)^2, stored as a 2,040 x 2,040 image.

4. **ZODI** - Estimated zodiacal light background flux in units of MJy/sr, stored as a 2040 x 2040 image.

5. **PSF** - 121 Point-spread functions (PSFs); each PSF is represented as a 101 x 101 image and all 121 are assembled together into a cube.

6. **WCS-WAVE** - Spectral World Coordinate System (WCS) lookup table that maps spectral image pixel coordinates to central wavelengths and bandwidths. The lookup table consists of 1 row with 3 columns (X, Y, VALUES). X and Y are each arrays of length 7, defining a 7x7 grid of control points in spectral image pixel space. VALUES is a 7x7 array of two-element arrays: at each (X, Y) control point, the two-element array contains the central wavelength and the corresponding bandwidth. To determine the central wavelength or bandwidth at an arbitrary pixel location, identify the four nearest control points and apply bilinear interpolation. This method yields values accurate to within approximately 1 nm.


*Filename Format:*
`
- 'level1_[Observation ID]_D[Detector Number]_spx_l2b_v[Version]_[Processing Date]'

*Where:* 

- `Observation ID` includes the survey planning period and the large and small slew counters

- `Detector Number` is an integer from 1 through 6

- 'Version' is the version of this file

- `Processing Date` includes the year and the number of days into the year

*Example:*

- 'level2_2025W18_2B_0001_1D1_spx_l2b-v12-2025-164.fits'


### Calibration Product: Absolute Gain Matrix

The Absolute Gain Matrix products are ~16 MB FITS image files (one per detector) with dimensions 2,040 × 2,040 and units of (MJy/sr) / (e−/s).

Filename Format:
abs_gain_matrix_D[Detector]_spx_cal-agm-v4-2025-161.fits

  Where "Detector" is one of the SPHEREx detectors: 1, 2, 3, 4, 5, or 6

### Calibration Product: Exposure-Averaged Point Spread Functions (PSFs)

The Exposure-Averaged Point Spread Functions (PSFs) are ~6 MB FITS cubes (one for each detector) with dimensions 101 × 101 × 121. Each of the 121 layers represents a "super-resolution" PSF estimate in a different region (defined by an 11x11 grid) of the detector. Each PSF is a two-dimensional array with size of 101 × 101 pixels. The PSFs are oversampled such that 10 PSF pixels cover the same spatial extent as one spectral image pixel (0.615 arcsec).


### Calibration Product: Dark Current

The Dark Current products are ~16 MB FITS image files (one per detector) with dimensions 2,040 x 2,040 and units of electron/s.

### Calibration Product: Dichroic

The Dichroic products are ~16 MB FITS image files with dimensions 2,040 x 2,040. The pixel value is 0 for pixels that are unaffected by flux attenuation due to the dicroic filter and 1 for impacted pixels. A pixel is considered impacted if the flux attenuation is 50% or higher. Note that only bands 3 and 4 have any non-zero values.

### Calibration Product: Electronic Gain Factors

The Electronic Gain Factor product is a single YAML file that includes the provenance information for the detectors and a list of 32 gain values per detector.

### Additional Product: Nonfunctional Pixels

The Nonfunctional Pixel products are ~32 MB FITS image files (one per detector) with dimensions 2,040 x 2,040. Pixel values are 1 for pixels known to be permanently non-functioning and 0 otherwise.

### Additional Product: Nonlinearity Parameters

The Nonlinearity Parameter products are ~79 MB multi-extension FITS files (one per detector). Each file contains 5 extensions (Q_nl, b1, b2, b3, Qmax), each of which is an image with dimensions 2,040 x 2,040. These extensions are described in Section 3.2.1 of the SPHEREx Explanatory Supplement.

### Additional Product: Read Noise Parameters

The Read Noise Parameters products are ~48 MB multi-extension FITS files (one per detector). Each file has 2 extensions: READNOISE-1 and READNOISE-2. Each extension is an image with dimensions 2040 × 2040 and units of electrons.

### Additional Product: Spectral WCS

The Spectral WCS products are ~32 MB multi-extension FITS files (one per detector). Each file has 3 extensions: CWAVE, CBAND, and WCS-WAVE. 

CWAVE is an image with dimensions 2,040 x 2,040. It contains the central wavelength in microns for each pixel.

CBAND is an image with dimensions 2,040 x 2,040. It contains the bandwidth in microns for each pixel.

WCS-WAVE is a table with 3 columns (X, Y, VALUES) and 1 row. This is equivalent to the WCS-WAVE extension in the Spectral Image MEF file described above.
