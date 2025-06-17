## SPHEREx Data Products Available at IRSA

A detailed description of SPHEREx data products available to the public is provided in Section 2 ("The SPHEREx Data Products") of the SPHEREx Explanatory Supplement. Here we provide a concise summary.

### Spectral Multi-Extension FITS Files (MEF)

The main Quick Release data product is the Spectral MEF. The Level 2 pipeline produces 6 Spectral MEFs (one for each band) for each sky pointing. Each Spectral MEF is approximately 70 MB and contains 6 extensions:

1. **IMAGE** - Calibrated surface brightness flux density in units of MJy/sr, stored as a 2040 x 2040 image. No zodiacal light subtraction is applied.

2. **FLAG** - Bitmap of per-pixel status and processing flags, stored as a 2040 x 2040 image. The definition of the flags are provided in Table 8 of the SPHEREx Explanatory Supplement.

3. **VARIANCE** - Variance of calibrated surface brightness flux in units of (MJy/sr)^2, stored as a 2,040 x 2,040 image.

4. **ZODI** - Estimated zodiacal light background flux in units of MJy/sr, stored as a 2040 x 2040 image.

5. **PSF** - 121 Point-spread functions (PSFs); each PSF is represented as a 101 x 101 image and all 121 are assembled together into a cube.

6. **WCS-WAVE** - Spectral World Coordinate System (WCS) lookup table that maps spectral image pixel coordinates to central wavelengths and bandwidths. The lookup table consists of 1 row with 3 columns (X, Y, VALUES). X and Y are each arrays of length 7, defining a 7x7 grid of control points in spectral image pixel space. VALUES is a 7x7 array of two-element arrays: at each (X, Y) control point, the two-element array contains the central wavelength and the corresponding bandwidth. To determine the central wavelength or bandwidth at an arbitrary pixel location, identify the four nearest control points and apply bilinear interpolation. This method yields values accurate to within approximately 1 nm.
