#!from collections import OrderedDict


#! boss_json = ['_dr',
#!  'dec',
#!  'ra',
#!  'redshift',
#!  'specid',
#!  'spectra.coadd.FLUX',
#!  'spectra.coadd.IVAR']
#!
#! boss_numpy = ['_dr', 'nparr']
#!
#! boss_pandas = ['_dr', 'df']
#!
#! boss_spectrum1d = ['_dr', 'redshift', 'spec1d']
#!
#! boss_spectrum1d_redshift = 0.570779085159302
#! everest_numpy = ['_dr', 'dec', 'nparr', 'ra', 'specid']
#!
#! everest_pandas = ['_dr', 'b_df', 'r_df', 'z_df']
#!
#! everest_spectrum1d = ['_dr', 'b_spec1d', 'r_spec1d', 'z_spec1d']
#!
#! everest_b_spectrum1d_redshift = 0.17526327367673789

fields_available = {'BOSS-DR16': ['_dr', 'flux', 'uuid', 'wavelength']}

record_examples = {'BOSS-DR16': ['_dr',
               'data_release_id',
               'datasetgroup_id',
               'dec',
               'ra',
               'redshift',
               'specid',
               'spectra.coadd.FLUX',
               'spectra.coadd.IVAR',
               'spectra.coadd.LOGLAM']}

get_vectordata  = ['flux', 'and_mask', 'ivar', 'loglam']

get_metadata  = [{'FIBERID': 892,
  'MJD': 58466,
  'PLATEID': 10660,
  'RUN1D': 'v5_13_0',
  'RUN2D': 'v5_13_0',
  'SPECOBJID': 12002338340072607744,
  '_dr': 'BOSS-DR16',
  'data_release_id': 'BOSS-DR16',
  'datasetgroup_id': 'SDSS_BOSS',
  'dec': 28.751204,
  'instrument_id': 'BOSS',
  'ra': 133.46096,
  'redshift_err': -1.0,
  'redshift_warning': 5,
  'site': 'apo',
  'specid': 1429933274376612,
  'specprimary': True,
  'spectype_id': 'STAR',
  'targetid': 0,
  'telescope_id': 'sloan25m',
  'uuid': 'bf0b1583-2d27-4b66-b2c7-7e7177e25c01',
  'wavemax': 10356.189453125,
  'wavemin': 3601.63745117188,
  'z': -0.00413607759401202}]


rename_fields = ['_dr', 'data_set', 'f', 'ivar', 'loglam', 'specid', 'x', 'y', 'z']
rename_fields_internal = ['_dr', 'data_release_id', 'f2', 'redshift', 'specid', 'spectra.coadd.IVAR', 'spectra.coadd.LOGLAM', 'x', 'y']


get_field_names_internal = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 '_dr',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

get_field_names = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 '_dr',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

orig_field = 'flux'
client_field = 'flux'

normalize_field_names = [['_dr', 'flux', 'ivar']]

#!df_lut_internal=OrderedDict([('FIBERID', {'default': False, 'new': 'FIBERID'}),
#!             ('MJD', {'default': False, 'new': 'MJD'}),
#!             ('PLATEID', {'default': False, 'new': 'PLATEID'}),
#!             ('RUN1D', {'default': False, 'new': 'RUN1D'}),
#!             ('RUN2D', {'default': False, 'new': 'RUN2D'}),
#!             ('SPECOBJID', {'default': False, 'new': 'SPECOBJID'}),
#!             ('_dr', {'default': True, 'new': '_dr'}),
#!             ('data_release_id', {'default': False, 'new': 'data_release_id'}),
#!             ('datasetgroup_id', {'default': False, 'new': 'datasetgroup_id'}),
#!             ('dateobs', {'default': False, 'new': 'dateobs'}),
#!             ('dateobs_center', {'default': False, 'new': 'dateobs_center'}),
#!             ('dec', {'default': False, 'new': 'dec'}),
#!             ('dirpath', {'default': False, 'new': 'dirpath'}),
#!             ('exptime', {'default': False, 'new': 'exptime'}),
#!             ('extra_files', {'default': False, 'new': 'extra_files'}),
#!             ('filename', {'default': False, 'new': 'filename'}),
#!             ('filesize', {'default': False, 'new': 'filesize'}),
#!             ('flux', {'default': True, 'new': 'flux'}),
#!             ('id', {'default': True, 'new': 'id'}),
#!             ('instrument_id', {'default': False, 'new': 'instrument_id'}),
#!             ('ivar', {'default': False, 'new': 'ivar'}),
#!             ('mask', {'default': False, 'new': 'mask'}),
#!             ('model', {'default': False, 'new': 'model'}),
#!             ('ra', {'default': False, 'new': 'ra'}),
#!             ('redshift', {'default': False, 'new': 'redshift'}),
#!             ('redshift_err', {'default': False, 'new': 'redshift_err'}),
#!             ('redshift_warning',
#!              {'default': False, 'new': 'redshift_warning'}),
#!             ('site_id', {'default': False, 'new': 'site_id'}),
#!             ('sky', {'default': False, 'new': 'sky'}),
#!             ('specid', {'default': False, 'new': 'specid'}),
#!             ('specprimary', {'default': False, 'new': 'specprimary'}),
#!             ('spectype_id', {'default': False, 'new': 'spectype_id'}),
#!             ('targetid', {'default': False, 'new': 'targetid'}),
#!             ('telescope_id', {'default': False, 'new': 'telescope_id'}),
#!             ('wave_sigma', {'default': False, 'new': 'wave_sigma'}),
#!             ('wavelength', {'default': True, 'new': 'wavelength'}),
#!             ('wavemax', {'default': False, 'new': 'wavemax'}),
#!             ('wavemin', {'default': False, 'new': 'wavemin'})])
#!
#!df_lut=OrderedDict([('FIBERID', {'default': False, 'new': 'FIBERID'}),
#!             ('MJD', {'default': False, 'new': 'MJD'}),
#!             ('PLATEID', {'default': False, 'new': 'PLATEID'}),
#!             ('RUN1D', {'default': False, 'new': 'RUN1D'}),
#!             ('RUN2D', {'default': False, 'new': 'RUN2D'}),
#!             ('SPECOBJID', {'default': False, 'new': 'SPECOBJID'}),
#!             ('_dr', {'default': True, 'new': '_dr'}),
#!             ('data_release_id', {'default': False, 'new': 'data_release_id'}),
#!             ('datasetgroup_id', {'default': False, 'new': 'datasetgroup_id'}),
#!             ('dateobs', {'default': False, 'new': 'dateobs'}),
#!             ('dateobs_center', {'default': False, 'new': 'dateobs_center'}),
#!             ('dec', {'default': False, 'new': 'dec'}),
#!             ('dirpath', {'default': False, 'new': 'dirpath'}),
#!             ('exptime', {'default': False, 'new': 'exptime'}),
#!             ('extra_files', {'default': False, 'new': 'extra_files'}),
#!             ('filename', {'default': False, 'new': 'filename'}),
#!             ('filesize', {'default': False, 'new': 'filesize'}),
#!             ('flux', {'default': True, 'new': 'flux'}),
#!             ('id', {'default': True, 'new': 'id'}),
#!             ('instrument_id', {'default': False, 'new': 'instrument_id'}),
#!             ('ivar', {'default': False, 'new': 'ivar'}),
#!             ('mask', {'default': False, 'new': 'mask'}),
#!             ('model', {'default': False, 'new': 'model'}),
#!             ('ra', {'default': False, 'new': 'ra'}),
#!             ('redshift', {'default': False, 'new': 'redshift'}),
#!             ('redshift_err', {'default': False, 'new': 'redshift_err'}),
#!             ('redshift_warning',
#!              {'default': False, 'new': 'redshift_warning'}),
#!             ('site_id', {'default': False, 'new': 'site_id'}),
#!             ('sky', {'default': False, 'new': 'sky'}),
#!             ('specid', {'default': False, 'new': 'specid'}),
#!             ('specprimary', {'default': False, 'new': 'specprimary'}),
#!             ('spectype_id', {'default': False, 'new': 'spectype_id'}),
#!             ('targetid', {'default': False, 'new': 'targetid'}),
#!             ('telescope_id', {'default': False, 'new': 'telescope_id'}),
#!             ('wave_sigma', {'default': False, 'new': 'wave_sigma'}),
#!             ('wavelength', {'default': True, 'new': 'wavelength'}),
#!             ('wavemax', {'default': False, 'new': 'wavemax'}),
#!             ('wavemin', {'default': False, 'new': 'wavemin'})])

retrieve_0 = [1429831265344501, 1429831265410037]

retrieve_0b = ['_dr', 'flux', 'uuid', 'wavelength']

retrieve_4 = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'exptime',
 'flux',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift_err',
 'redshift_warning',
 'site',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'uuid',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin',
 'z']

retrieve_5 = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']


find_0 = [{'_dr': 'BOSS-DR16',
           'dec': -0.37900273,
           'ra': 208.02613,
           'uuid': 'cc49c317-d8c4-4324-9b1d-c3b590e7f8d7'}]

find_1 = [{'_dr': 'SDSS-DR16',
           'dec': 27.081405,
           'ra': 240.42064,
           'uuid': '1642a45c-11c5-42ef-8ee6-064169f51e5e'}]

find_2 = 4   # DEV
#find_2 = 926622 # PAT

find_3 = [{'_dr': 'SDSS-DR16',
           'dec': 27.081405,
           'ra': 240.42064,
           'uuid': '1642a45c-11c5-42ef-8ee6-064169f51e5e'},
          {'_dr': 'BOSS-DR16',
           'dec': 28.751204,
           'ra': 133.46096,
           'uuid': '4ef1d16b-3a16-4cf2-b533-a91b2795cc79'},
          {'_dr': 'BOSS-DR16',
           'dec': -0.37900273,
           'ra': 208.02613,
           'uuid': 'cc49c317-d8c4-4324-9b1d-c3b590e7f8d7'}]

find_3_pat = [{'_dr': 'DESI-edr',
           'dec': 54.0581773035796,
           'ra': 174.578243924582,
           'uuid': '000005ad-e1b0-4132-b25f-d3aa6acb08de'},
          {'_dr': 'SDSS-DR16',
           'dec': 43.635286,
           'ra': 145.1597,
           'uuid': '000008b3-e3ad-4e40-9fc1-feb18a42227c'},
          {'_dr': 'BOSS-DR16',
           'dec': 0.46353569,
           'ra': 322.51088,
           'uuid': '00002089-eaf2-44fc-948e-d90210bca3da'}]

find_6 = []
