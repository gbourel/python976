from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


exif_tag_fr = {
 11: 'ProcessingSoftware',
 254: 'NewSubfileType',
 255: 'SubfileType',
 256: 'ImageWidth',
 257: 'ImageLength',
 258: 'BitsPerSample',
 259: 'Compression',
 262: 'PhotometricInterpretation',
 263: 'Thresholding',
 264: 'CellWidth',
 265: 'CellLength',
 266: 'FillOrder',
 269: 'DocumentName',
 270: 'ImageDescription',
 271: 'Make',
 272: 'Model',
 273: 'StripOffsets',
 274: 'Orientation',
 277: 'SamplesPerPixel',
 278: 'RowsPerStrip',
 279: 'StripByteCounts',
 280: 'MinSampleValue',
 281: 'MaxSampleValue',
 282: 'XResolution',
 283: 'YResolution',
 284: 'PlanarConfiguration',
 285: 'PageName',
 288: 'FreeOffsets',
 289: 'FreeByteCounts',
 290: 'GrayResponseUnit',
 291: 'GrayResponseCurve',
 292: 'T4Options',
 293: 'T6Options',
 296: 'ResolutionUnit',
 297: 'PageNumber',
 301: 'TransferFunction',
 305: 'Software',
 306: 'DateTime',
 315: 'Artist',
 316: 'HostComputer',
 317: 'Predictor',
 318: 'WhitePoint',
 319: 'PrimaryChromaticities',
 320: 'ColorMap',
 321: 'HalftoneHints',
 322: 'TileWidth',
 323: 'TileLength',
 324: 'TileOffsets',
 325: 'TileByteCounts',
 330: 'SubIFDs',
 332: 'InkSet',
 333: 'InkNames',
 334: 'NumberOfInks',
 336: 'DotRange',
 337: 'TargetPrinter',
 338: 'ExtraSamples',
 339: 'SampleFormat',
 340: 'SMinSampleValue',
 341: 'SMaxSampleValue',
 342: 'TransferRange',
 343: 'ClipPath',
 344: 'XClipPathUnits',
 345: 'YClipPathUnits',
 346: 'Indexed',
 347: 'JPEGTables',
 351: 'OPIProxy',
 512: 'JPEGProc',
 513: 'JpegIFOffset',
 514: 'JpegIFByteCount',
 515: 'JpegRestartInterval',
 517: 'JpegLosslessPredictors',
 518: 'JpegPointTransforms',
 519: 'JpegQTables',
 520: 'JpegDCTables',
 521: 'JpegACTables',
 529: 'YCbCrCoefficients',
 530: 'YCbCrSubSampling',
 531: 'YCbCrPositioning',
 532: 'ReferenceBlackWhite',
 700: 'XMLPacket',
 4096: 'RelatedImageFileFormat',
 4097: 'RelatedImageWidth',
 4098: 'RelatedImageLength',
 18246: 'Rating',
 18249: 'RatingPercent',
 32781: 'ImageID',
 33421: 'CFARepeatPatternDim',
 33422: 'CFAPattern',
 33423: 'BatteryLevel',
 33432: 'Copyright',
 33434: 'ExposureTime',
 33437: 'FNumber',
 33723: 'IPTCNAA',
 34377: 'ImageResources',
 34665: 'ExifOffset',
 34675: 'InterColorProfile',
 34850: 'ExposureProgram',
 34852: 'SpectralSensitivity',
 34853: 'GPSInfo',
 34855: 'ISOSpeedRatings',
 34856: 'OECF',
 34857: 'Interlace',
 34858: 'TimeZoneOffset',
 34859: 'SelfTimerMode',
 36864: 'ExifVersion',
 36867: 'DateTimeOriginal',
 36868: 'DateTimeDigitized',
 37121: 'ComponentsConfiguration',
 37122: 'CompressedBitsPerPixel',
 37377: 'ShutterSpeedValue',
 37378: 'ApertureValue',
 37379: 'BrightnessValue',
 37380: 'ExposureBiasValue',
 37381: 'MaxApertureValue',
 37382: 'SubjectDistance',
 37383: 'MeteringMode',
 37384: 'LightSource',
 37385: 'Flash',
 37386: 'FocalLength',
 37387: 'FlashEnergy',
 37388: 'SpatialFrequencyResponse',
 37389: 'Noise',
 37393: 'ImageNumber',
 37394: 'SecurityClassification',
 37395: 'ImageHistory',
 37396: 'SubjectLocation',
 37397: 'ExposureIndex',
 37398: 'TIFF/EPStandardID',
 37500: 'MakerNote',
 37510: 'UserComment',
 37520: 'SubsecTime',
 37521: 'SubsecTimeOriginal',
 37522: 'SubsecTimeDigitized',
 40091: 'XPTitle',
 40092: 'XPComment',
 40093: 'XPAuthor',
 40094: 'XPKeywords',
 40095: 'XPSubject',
 40960: 'FlashPixVersion',
 40961: 'ColorSpace',
 40962: 'ExifImageWidth',
 40963: 'ExifImageHeight',
 40964: 'RelatedSoundFile',
 40965: 'ExifInteroperabilityOffset',
 41483: 'FlashEnergy',
 41484: 'SpatialFrequencyResponse',
 41486: 'FocalPlaneXResolution',
 41487: 'FocalPlaneYResolution',
 41488: 'FocalPlaneResolutionUnit',
 41492: 'SubjectLocation',
 41493: 'ExposureIndex',
 41495: 'SensingMethod',
 41728: 'FileSource',
 41729: 'SceneType',
 41730: 'CFAPattern',
 41985: 'CustomRendered',
 41986: 'ExposureMode',
 41987: 'WhiteBalance',
 41988: 'DigitalZoomRatio',
 41989: 'FocalLengthIn35mmFilm',
 41990: 'SceneCaptureType',
 41991: 'GainControl',
 41992: 'Contrast',
 41993: 'Saturation',
 41994: 'Sharpness',
 41995: 'DeviceSettingDescription',
 41996: 'SubjectDistanceRange',
 42016: 'ImageUniqueID',
 42032: 'CameraOwnerName',
 42033: 'BodySerialNumber',
 42034: 'LensSpecification',
 42035: 'LensMake',
 42036: 'LensModel',
 42037: 'LensSerialNumber',
 42240: 'Gamma',
 50341: 'PrintImageMatching',
 50706: 'DNGVersion',
 50707: 'DNGBackwardVersion',
 50708: 'UniqueCameraModel',
 50709: 'LocalizedCameraModel',
 50710: 'CFAPlaneColor',
 50711: 'CFALayout',
 50712: 'LinearizationTable',
 50713: 'BlackLevelRepeatDim',
 50714: 'BlackLevel',
 50715: 'BlackLevelDeltaH',
 50716: 'BlackLevelDeltaV',
 50717: 'WhiteLevel',
 50718: 'DefaultScale',
 50719: 'DefaultCropOrigin',
 50720: 'DefaultCropSize',
 50721: 'ColorMatrix1',
 50722: 'ColorMatrix2',
 50723: 'CameraCalibration1',
 50724: 'CameraCalibration2',
 50725: 'ReductionMatrix1',
 50726: 'ReductionMatrix2',
 50727: 'AnalogBalance',
 50728: 'AsShotNeutral',
 50729: 'AsShotWhiteXY',
 50730: 'BaselineExposure',
 50731: 'BaselineNoise',
 50732: 'BaselineSharpness',
 50733: 'BayerGreenSplit',
 50734: 'LinearResponseLimit',
 50735: 'CameraSerialNumber',
 50736: 'LensInfo',
 50737: 'ChromaBlurRadius',
 50738: 'AntiAliasStrength',
 50739: 'ShadowScale',
 50740: 'DNGPrivateData',
 50741: 'MakerNoteSafety',
 50778: 'CalibrationIlluminant1',
 50779: 'CalibrationIlluminant2',
 50780: 'BestQualityScale',
 50781: 'RawDataUniqueID',
 50827: 'OriginalRawFileName',
 50828: 'OriginalRawFileData',
 50829: 'ActiveArea',
 50830: 'MaskedAreas',
 50831: 'AsShotICCProfile',
 50832: 'AsShotPreProfileMatrix',
 50833: 'CurrentICCProfile',
 50834: 'CurrentPreProfileMatrix',
 50879: 'ColorimetricReference',
 50931: 'CameraCalibrationSignature',
 50932: 'ProfileCalibrationSignature',
 50934: 'AsShotProfileName',
 50935: 'NoiseReductionApplied',
 50936: 'ProfileName',
 50937: 'ProfileHueSatMapDims',
 50938: 'ProfileHueSatMapData1',
 50939: 'ProfileHueSatMapData2',
 50940: 'ProfileToneCurve',
 50941: 'ProfileEmbedPolicy',
 50942: 'ProfileCopyright',
 50964: 'ForwardMatrix1',
 50965: 'ForwardMatrix2',
 50966: 'PreviewApplicationName',
 50967: 'PreviewApplicationVersion',
 50968: 'PreviewSettingsName',
 50969: 'PreviewSettingsDigest',
 50970: 'PreviewColorSpace',
 50971: 'PreviewDateTime',
 50972: 'RawImageDigest',
 50973: 'OriginalRawFileDigest',
 50974: 'SubTileBlockSize',
 50975: 'RowInterleaveFactor',
 50981: 'ProfileLookTableDims',
 50982: 'ProfileLookTableData',
 51008: 'OpcodeList1',
 51009: 'OpcodeList2',
 51022: 'OpcodeList3',
 51041: 'NoiseProfile'}




def lattitude(img_path):
	"""
	Fonction qui prend en paramètre le chemin d'une image
	et renvoie la latidude en degré minute seconde.

	"""
	img = Image.open(img_path)
	exifd = {
	    TAGS[k]: v
	    for k, v in img._getexif().items()
	    if k in TAGS
	}
	gpsinfo = exifd["GPSInfo"]
	gpsd = {
	    GPSTAGS[k]: v
	    for k, v in exifd["GPSInfo"].items()
	    if k in GPSTAGS
	}

	return gpsd["GPSLatitude"]

def longitude(img_path):
	"""
	Fonction qui prend en paramètre le chemin d'une image
	et renvoie la longitude en degré minute seconde.

	"""
	img = Image.open(img_path)
	exifd = {
	    TAGS[k]: v
	    for k, v in img._getexif().items()
	    if k in TAGS
	}
	gpsinfo = exifd["GPSInfo"]
	gpsd = {
	    GPSTAGS[k]: v
	    for k, v in exifd["GPSInfo"].items()
	    if k in GPSTAGS
	}

	return gpsd["GPSLongitude"]

# lat_d = lat[0][0] + lat[1][0]/60 + lat[2][0] /(36*10**len(str(lat[2][0])))
# lon_d = lon[0][0] + lon[1][0]/60 + lon[2][0] /(36*10**len(str(lon[2][0])))
# print(lat_d)
# print(lon_d)


# m = folium.Map(location=[lat_d, lon_d])
# tooltip = 'Click me!'

# folium.Marker([lat_d, lon_d], popup='<img src="image.jpg" heigth="200px" width="150px"></img>', tooltip=tooltip).add_to(m)
# # folium.Marker([48.8798477, 2.3551638125000003], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)
# m.save("localisation.html")