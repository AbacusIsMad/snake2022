
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 410 > 0
static unsigned char *bytecode_data[410];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_game(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_instructions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_level(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_map(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$__config__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_distributor_init(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_globals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_pytesttester(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat$_inspect(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$compat$py3k(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_add_newdocs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_add_newdocs_scalars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_asarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_dtype(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_dtype_ctypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_internal(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_machar(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_methods(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_string_helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_type_aliases(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$_ufunc_config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$arrayprint(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$defchararray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$einsumfunc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$fromnumeric(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$function_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$getlimits(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$memmap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$multiarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$numeric(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$numerictypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$overrides(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$records(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$shape_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$core$umath(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ctypeslib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft$_pocketfft(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$fft$helper(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_datasource(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_iotools(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arraypad(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arraysetops(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$arrayterator(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$format(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$function_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$histograms(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$index_tricks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$mixins(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$nanfunctions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$npyio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$scimath(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$shape_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$stride_tricks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$twodim_base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$type_check(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$ufunclike(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$lib$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$linalg(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$linalg$linalg(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$extras(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$ma$mrecords(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$matrixlib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$matrixlib$defmatrix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$_polybase(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$chebyshev(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$hermite(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$hermite_e(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$laguerre(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$legendre(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$polynomial(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$polynomial$polyutils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$random(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$random$_pickle(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_add_docstring(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_array_like(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_char_codes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_dtype_like(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_generic_alias(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_nbit(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_nested_sequence(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_scalars(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$typing$_shape(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_numpy$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$colordict(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$cursors(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$fastevent(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$ftfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$locals(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$macosx(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$pkgdata(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sndarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sprite(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$surfarray(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$sysfont(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$threads(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pygame$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_snake(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"__main__", modulecode___main__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"_asyncio", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_bz2", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_cn", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_hk", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_iso2022", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_jp", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_kr", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_codecs_tw", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_contextvars", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_crypt", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_ctypes", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_dbm", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_decimal", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_hashlib", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_json", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_lzma", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_multibytecodec", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_opcode", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_queue", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_ssl", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"_uuid", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"audioop", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"bdb", NULL, 0, 24886, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"config", modulecode_config, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"dbm", NULL, 1, 4148, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"dbm.ndbm", NULL, 2, 167, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email", NULL, 3, 1647, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email._encoded_words", NULL, 4, 5651, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._header_value_parser", NULL, 5, 79898, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._parseaddr", NULL, 6, 12419, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email._policybase", NULL, 7, 14775, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.base64mime", NULL, 8, 3200, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.charset", NULL, 9, 11424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.contentmanager", NULL, 10, 7326, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.encoders", NULL, 11, 1577, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.errors", NULL, 12, 5870, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.feedparser", NULL, 13, 10607, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.generator", NULL, 14, 12489, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.header", NULL, 15, 16404, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.headerregistry", NULL, 16, 22009, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.iterators", NULL, 17, 1885, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.message", NULL, 18, 37843, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.parser", NULL, 19, 5687, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.policy", NULL, 20, 9623, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.quoprimime", NULL, 21, 7643, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"email.utils", NULL, 22, 9507, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"game", modulecode_game, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"http", NULL, 23, 6020, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"http.client", NULL, 24, 34872, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"http.server", NULL, 25, 34357, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"instructions", modulecode_instructions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"level", modulecode_level, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"map", modulecode_map, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"mmap", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"ntpath", NULL, 26, 14622, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"numpy", modulecode_numpy, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.__config__", modulecode_numpy$__config__, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy._distributor_init", modulecode_numpy$_distributor_init, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy._globals", modulecode_numpy$_globals, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy._pytesttester", modulecode_numpy$_pytesttester, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy._version", modulecode_numpy$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.compat", modulecode_numpy$compat, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.compat._inspect", modulecode_numpy$compat$_inspect, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.compat.py3k", modulecode_numpy$compat$py3k, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core", modulecode_numpy$core, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.core._add_newdocs", modulecode_numpy$core$_add_newdocs, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._add_newdocs_scalars", modulecode_numpy$core$_add_newdocs_scalars, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._asarray", modulecode_numpy$core$_asarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._dtype", modulecode_numpy$core$_dtype, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._dtype_ctypes", modulecode_numpy$core$_dtype_ctypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._exceptions", modulecode_numpy$core$_exceptions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._internal", modulecode_numpy$core$_internal, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._machar", modulecode_numpy$core$_machar, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._methods", modulecode_numpy$core$_methods, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._multiarray_tests", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.core._multiarray_umath", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.core._string_helpers", modulecode_numpy$core$_string_helpers, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._type_aliases", modulecode_numpy$core$_type_aliases, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core._ufunc_config", modulecode_numpy$core$_ufunc_config, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.arrayprint", modulecode_numpy$core$arrayprint, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.defchararray", modulecode_numpy$core$defchararray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.einsumfunc", modulecode_numpy$core$einsumfunc, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.fromnumeric", modulecode_numpy$core$fromnumeric, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.function_base", modulecode_numpy$core$function_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.getlimits", modulecode_numpy$core$getlimits, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.memmap", modulecode_numpy$core$memmap, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.multiarray", modulecode_numpy$core$multiarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.numeric", modulecode_numpy$core$numeric, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.numerictypes", modulecode_numpy$core$numerictypes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.overrides", modulecode_numpy$core$overrides, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.records", modulecode_numpy$core$records, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.shape_base", modulecode_numpy$core$shape_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.core.umath", modulecode_numpy$core$umath, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.ctypeslib", modulecode_numpy$ctypeslib, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.fft", modulecode_numpy$fft, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.fft._pocketfft", modulecode_numpy$fft$_pocketfft, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.fft._pocketfft_internal", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.fft.helper", modulecode_numpy$fft$helper, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib", modulecode_numpy$lib, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.lib._datasource", modulecode_numpy$lib$_datasource, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib._iotools", modulecode_numpy$lib$_iotools, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib._version", modulecode_numpy$lib$_version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.arraypad", modulecode_numpy$lib$arraypad, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.arraysetops", modulecode_numpy$lib$arraysetops, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.arrayterator", modulecode_numpy$lib$arrayterator, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.format", modulecode_numpy$lib$format, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.function_base", modulecode_numpy$lib$function_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.histograms", modulecode_numpy$lib$histograms, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.index_tricks", modulecode_numpy$lib$index_tricks, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.mixins", modulecode_numpy$lib$mixins, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.nanfunctions", modulecode_numpy$lib$nanfunctions, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.npyio", modulecode_numpy$lib$npyio, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.polynomial", modulecode_numpy$lib$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.scimath", modulecode_numpy$lib$scimath, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.shape_base", modulecode_numpy$lib$shape_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.stride_tricks", modulecode_numpy$lib$stride_tricks, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.twodim_base", modulecode_numpy$lib$twodim_base, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.type_check", modulecode_numpy$lib$type_check, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.ufunclike", modulecode_numpy$lib$ufunclike, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.lib.utils", modulecode_numpy$lib$utils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.linalg", modulecode_numpy$linalg, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.linalg._umath_linalg", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.linalg.linalg", modulecode_numpy$linalg$linalg, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.ma", modulecode_numpy$ma, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.ma.core", modulecode_numpy$ma$core, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.ma.extras", modulecode_numpy$ma$extras, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.ma.mrecords", modulecode_numpy$ma$mrecords, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.matrixlib", modulecode_numpy$matrixlib, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.matrixlib.defmatrix", modulecode_numpy$matrixlib$defmatrix, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial", modulecode_numpy$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.polynomial._polybase", modulecode_numpy$polynomial$_polybase, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.chebyshev", modulecode_numpy$polynomial$chebyshev, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.hermite", modulecode_numpy$polynomial$hermite, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.hermite_e", modulecode_numpy$polynomial$hermite_e, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.laguerre", modulecode_numpy$polynomial$laguerre, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.legendre", modulecode_numpy$polynomial$legendre, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.polynomial", modulecode_numpy$polynomial$polynomial, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.polynomial.polyutils", modulecode_numpy$polynomial$polyutils, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.random", modulecode_numpy$random, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.random._bounded_integers", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._common", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._generator", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._mt19937", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._pcg64", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._philox", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random._pickle", modulecode_numpy$random$_pickle, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.random._sfc64", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random.bit_generator", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.random.mtrand", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"numpy.testing", NULL, 27, 981, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.typing", modulecode_numpy$typing, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"numpy.typing._add_docstring", modulecode_numpy$typing$_add_docstring, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._array_like", modulecode_numpy$typing$_array_like, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._char_codes", modulecode_numpy$typing$_char_codes, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._dtype_like", modulecode_numpy$typing$_dtype_like, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._generic_alias", modulecode_numpy$typing$_generic_alias, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._nbit", modulecode_numpy$typing$_nbit, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._nested_sequence", modulecode_numpy$typing$_nested_sequence, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._scalars", modulecode_numpy$typing$_scalars, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.typing._shape", modulecode_numpy$typing$_shape, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"numpy.version", modulecode_numpy$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pdb", NULL, 28, 47191, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources", NULL, 29, 100338, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor", NULL, 30, 99, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor.appdirs", NULL, 31, 20461, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging", NULL, 32, 487, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources._vendor.packaging.__about__", NULL, 33, 658, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging._compat", NULL, 34, 932, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging._structures", NULL, 35, 2714, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.markers", NULL, 36, 8870, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.requirements", NULL, 37, 3829, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.specifiers", NULL, 38, 19738, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.packaging.version", NULL, 39, 10585, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.pyparsing", NULL, 40, 201585, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources._vendor.six", NULL, 41, 24381, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources.extern", NULL, 42, 2348, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pkg_resources.py2_warn", NULL, 43, 882, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkg_resources.py31compat", NULL, 44, 551, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"plistlib", NULL, 45, 27130, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pydoc", NULL, 46, 83573, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pygame", modulecode_pygame, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygame._freetype", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.base", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.bufferproxy", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.color", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.colordict", modulecode_pygame$colordict, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.constants", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.cursors", modulecode_pygame$cursors, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.display", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.draw", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.event", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.fastevent", modulecode_pygame$fastevent, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.font", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.ftfont", modulecode_pygame$ftfont, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.image", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.imageext", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.joystick", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.key", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.locals", modulecode_pygame$locals, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.macosx", modulecode_pygame$macosx, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.mask", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.math", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.mixer", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.mixer_music", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.mouse", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.pixelarray", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.pixelcopy", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.pkgdata", modulecode_pygame$pkgdata, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.rect", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.rwobject", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.scrap", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.sndarray", modulecode_pygame$sndarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.sprite", modulecode_pygame$sprite, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.surface", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.surfarray", modulecode_pygame$surfarray, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.surflock", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.sysfont", modulecode_pygame$sysfont, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"pygame.threads", modulecode_pygame$threads, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_PACKAGE_FLAG},
    {"pygame.time", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.transform", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"pygame.version", modulecode_pygame$version, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"readline", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"runpy", NULL, 47, 8146, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"snake", modulecode_snake, 0, 0, NUITKA_TRANSLATED_FLAG},
    {"termios", NULL, 0, 0, NUITKA_TRANSLATED_FLAG | NUITKA_EXTENSION_MODULE_FLAG},
    {"__future__", NULL, 48, 4123, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_bootlocale", NULL, 49, 1208, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_collections_abc", NULL, 50, 28706, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_compat_pickle", NULL, 51, 5466, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_compression", NULL, 52, 4111, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_dummy_thread", NULL, 53, 6002, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_markupbase", NULL, 54, 7755, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_osx_support", NULL, 55, 11558, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_py_abc", NULL, 56, 4635, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_pyio", NULL, 57, 74044, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_sitebuiltins", NULL, 58, 3446, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_strptime", NULL, 59, 16009, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_sysconfigdata__linux_x86_64-linux-gnu", NULL, 60, 21086, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_sysconfigdata__x86_64-linux-gnu", NULL, 61, 21080, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_threading_local", NULL, 62, 6411, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"_weakrefset", NULL, 63, 7565, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"abc", NULL, 64, 5299, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"aifc", NULL, 65, 25439, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ast", NULL, 66, 16728, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asynchat", NULL, 67, 6816, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio", NULL, 68, 706, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"asyncio.base_events", NULL, 69, 50985, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_futures", NULL, 70, 1863, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_subprocess", NULL, 71, 9381, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.base_tasks", NULL, 72, 1909, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.constants", NULL, 73, 546, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.coroutines", NULL, 74, 6619, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.events", NULL, 75, 28022, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.exceptions", NULL, 76, 2514, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.format_helpers", NULL, 77, 2297, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.futures", NULL, 78, 11158, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.locks", NULL, 79, 16333, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.log", NULL, 80, 191, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.proactor_events", NULL, 81, 24110, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.protocols", NULL, 82, 8579, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.queues", NULL, 83, 8346, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.runners", NULL, 84, 1912, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.selector_events", NULL, 85, 29650, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.sslproto", NULL, 86, 21583, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.staggered", NULL, 87, 4083, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.streams", NULL, 88, 20605, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.subprocess", NULL, 89, 7323, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.tasks", NULL, 90, 24246, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.transports", NULL, 91, 12227, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.trsock", NULL, 92, 8448, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncio.unix_events", NULL, 93, 39301, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"asyncore", NULL, 94, 15993, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"base64", NULL, 95, 17036, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"binhex", NULL, 96, 12099, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"bisect", NULL, 97, 2319, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"bz2", NULL, 98, 11410, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"calendar", NULL, 99, 27029, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cgi", NULL, 100, 26509, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cgitb", NULL, 101, 10115, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"chunk", NULL, 102, 4804, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"cmd", NULL, 103, 12591, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"code", NULL, 104, 9878, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"codecs", NULL, 105, 33921, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"codeop", NULL, 106, 6382, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"collections", NULL, 107, 46392, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"collections.abc", NULL, 108, 28705, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"colorsys", NULL, 109, 3205, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent", NULL, 110, 88, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures", NULL, 111, 1064, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures._base", NULL, 112, 21905, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.process", NULL, 113, 20265, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.thread", NULL, 114, 5783, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"configparser", NULL, 115, 45683, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"contextlib", NULL, 116, 20194, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"contextvars", NULL, 117, 208, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"copy", NULL, 118, 6952, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"copyreg", NULL, 119, 4283, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"crypt", NULL, 120, 3352, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"csv", NULL, 121, 11875, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes", NULL, 122, 16328, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes._aix", NULL, 123, 9809, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes._endian", NULL, 124, 1894, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ctypes.util", NULL, 125, 8096, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dataclasses", NULL, 126, 23618, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"datetime", NULL, 127, 57138, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"decimal", NULL, 128, 160697, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"difflib", NULL, 129, 59403, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dis", NULL, 130, 15773, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"dummy_threading", NULL, 131, 1075, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings", NULL, 132, 3859, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"encodings.aliases", NULL, 133, 6295, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.ascii", NULL, 134, 1846, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.base64_codec", NULL, 135, 2364, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.big5", NULL, 136, 1374, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.big5hkscs", NULL, 137, 1384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.bz2_codec", NULL, 138, 3255, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.charmap", NULL, 139, 2856, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp037", NULL, 140, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1006", NULL, 141, 2463, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1026", NULL, 142, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1125", NULL, 143, 8094, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1140", NULL, 144, 2377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1250", NULL, 145, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1251", NULL, 146, 2411, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1252", NULL, 147, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1253", NULL, 148, 2427, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1254", NULL, 149, 2416, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1255", NULL, 150, 2435, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1256", NULL, 151, 2413, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1257", NULL, 152, 2421, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp1258", NULL, 153, 2419, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp273", NULL, 154, 2373, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp424", NULL, 155, 2417, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp437", NULL, 156, 7811, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp500", NULL, 157, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp720", NULL, 158, 2484, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp737", NULL, 159, 8133, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp775", NULL, 160, 7841, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp850", NULL, 161, 7472, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp852", NULL, 162, 7849, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp855", NULL, 163, 8102, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp856", NULL, 164, 2449, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp857", NULL, 165, 7452, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp858", NULL, 166, 7442, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp860", NULL, 167, 7790, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp861", NULL, 168, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp862", NULL, 169, 7994, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp863", NULL, 170, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp864", NULL, 171, 7949, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp865", NULL, 172, 7805, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp866", NULL, 173, 8138, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp869", NULL, 174, 7829, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp874", NULL, 175, 2515, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp875", NULL, 176, 2384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp932", NULL, 177, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp949", NULL, 178, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.cp950", NULL, 179, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jis_2004", NULL, 180, 1390, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jisx0213", NULL, 181, 1390, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jp", NULL, 182, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.euc_kr", NULL, 183, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gb18030", NULL, 184, 1380, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gb2312", NULL, 185, 1378, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.gbk", NULL, 186, 1372, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hex_codec", NULL, 187, 2351, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hp_roman8", NULL, 188, 2588, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.hz", NULL, 189, 1370, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.idna", NULL, 190, 5582, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp", NULL, 191, 1391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_1", NULL, 192, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2", NULL, 193, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2004", NULL, 194, 1401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_3", NULL, 195, 1395, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_ext", NULL, 196, 1399, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_kr", NULL, 197, 1391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_1", NULL, 198, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_10", NULL, 199, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_11", NULL, 200, 2485, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_13", NULL, 201, 2394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_14", NULL, 202, 2412, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_15", NULL, 203, 2391, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_16", NULL, 204, 2393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_2", NULL, 205, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_3", NULL, 206, 2393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_4", NULL, 207, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_5", NULL, 208, 2387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_6", NULL, 209, 2431, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_7", NULL, 210, 2394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_8", NULL, 211, 2425, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_9", NULL, 212, 2386, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.johab", NULL, 213, 1376, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_r", NULL, 214, 2438, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_t", NULL, 215, 2349, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_u", NULL, 216, 2424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.kz1048", NULL, 217, 2401, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.latin_1", NULL, 218, 1858, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_arabic", NULL, 219, 7705, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_centeuro", NULL, 220, 2425, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_croatian", NULL, 221, 2433, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_cyrillic", NULL, 222, 2423, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_farsi", NULL, 223, 2367, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_greek", NULL, 224, 2407, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_iceland", NULL, 225, 2426, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_latin2", NULL, 226, 2567, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_roman", NULL, 227, 2424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_romanian", NULL, 228, 2434, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.mac_turkish", NULL, 229, 2427, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.palmos", NULL, 230, 2414, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.ptcp154", NULL, 231, 2508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.punycode", NULL, 232, 6280, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.quopri_codec", NULL, 233, 2380, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.raw_unicode_escape", NULL, 234, 1727, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.rot_13", NULL, 235, 2966, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis", NULL, 236, 1384, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis_2004", NULL, 237, 1394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jisx0213", NULL, 238, 1394, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.tis_620", NULL, 239, 2476, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.undefined", NULL, 240, 2060, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.unicode_escape", NULL, 241, 1707, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16", NULL, 242, 4837, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_be", NULL, 243, 1615, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_le", NULL, 244, 1615, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32", NULL, 245, 4730, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_be", NULL, 246, 1508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_le", NULL, 247, 1508, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_7", NULL, 248, 1536, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8", NULL, 249, 1595, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8_sig", NULL, 250, 4511, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.uu_codec", NULL, 251, 3214, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"encodings.zlib_codec", NULL, 252, 3074, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"enum", NULL, 253, 25927, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"filecmp", NULL, 254, 8392, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fileinput", NULL, 255, 13338, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fnmatch", NULL, 256, 3320, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"formatter", NULL, 257, 17510, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"fractions", NULL, 258, 18704, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ftplib", NULL, 259, 27972, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"functools", NULL, 260, 27866, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"genericpath", NULL, 261, 3966, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"getopt", NULL, 262, 6236, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"getpass", NULL, 263, 4143, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"gettext", NULL, 264, 17965, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"glob", NULL, 265, 4308, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"gzip", NULL, 266, 18149, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"hashlib", NULL, 267, 6692, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"heapq", NULL, 268, 14035, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"hmac", NULL, 269, 6353, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"html", NULL, 270, 3574, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"html.entities", NULL, 271, 50494, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"html.parser", NULL, 272, 11163, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imaplib", NULL, 273, 41307, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imghdr", NULL, 274, 4083, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"imp", NULL, 275, 9774, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib", NULL, 276, 3714, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"importlib._bootstrap", NULL, 277, 28570, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib._bootstrap_external", NULL, 278, 45148, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.abc", NULL, 279, 13538, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.machinery", NULL, 280, 927, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.metadata", NULL, 281, 20841, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.resources", NULL, 282, 6475, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"importlib.util", NULL, 283, 9257, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"inspect", NULL, 284, 80558, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"io", NULL, 285, 3419, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ipaddress", NULL, 286, 59942, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json", NULL, 287, 12564, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"json.decoder", NULL, 288, 9809, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.encoder", NULL, 289, 11136, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.scanner", NULL, 290, 1916, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"json.tool", NULL, 291, 1861, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"keyword", NULL, 292, 963, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"linecache", NULL, 293, 3832, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"locale", NULL, 294, 34639, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"logging", NULL, 295, 65234, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"logging.config", NULL, 296, 23189, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"logging.handlers", NULL, 297, 43163, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"lzma", NULL, 298, 11983, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mailbox", NULL, 299, 60229, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mailcap", NULL, 300, 6441, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"mimetypes", NULL, 301, 15996, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"modulefinder", NULL, 302, 16080, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"netrc", NULL, 303, 3742, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"nturl2path", NULL, 304, 1709, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"numbers", NULL, 305, 12167, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"opcode", NULL, 306, 5385, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"operator", NULL, 307, 13656, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"os", NULL, 308, 31362, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pathlib", NULL, 309, 44174, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pickle", NULL, 310, 46873, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pickletools", NULL, 311, 67169, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pipes", NULL, 312, 7760, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pkgutil", NULL, 313, 16274, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"platform", NULL, 314, 24291, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"poplib", NULL, 315, 13424, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"posixpath", NULL, 316, 10393, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pprint", NULL, 317, 16246, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pstats", NULL, 318, 22031, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pty", NULL, 319, 3920, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"pyclbr", NULL, 320, 10416, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"queue", NULL, 321, 10591, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"quopri", NULL, 322, 5713, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"random", NULL, 323, 20073, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"re", NULL, 324, 14387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"reprlib", NULL, 325, 5268, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"rlcompleter", NULL, 326, 5720, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sched", NULL, 327, 6497, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"secrets", NULL, 328, 2155, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"selectors", NULL, 329, 16900, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shelve", NULL, 330, 9455, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shlex", NULL, 331, 7501, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"shutil", NULL, 332, 37184, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"signal", NULL, 333, 2808, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"smtpd", NULL, 334, 26428, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sndhdr", NULL, 335, 6954, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"socket", NULL, 336, 27752, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"socketserver", NULL, 337, 25326, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_compile", NULL, 338, 15107, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_constants", NULL, 339, 6324, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sre_parse", NULL, 340, 21612, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"ssl", NULL, 341, 44561, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"stat", NULL, 342, 4337, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"statistics", NULL, 343, 33618, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"string", NULL, 344, 7265, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"stringprep", NULL, 345, 10982, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"struct", NULL, 346, 295, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"subprocess", NULL, 347, 41932, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"symbol", NULL, 348, 2369, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"symtable", NULL, 349, 11287, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"sysconfig", NULL, 350, 15802, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tarfile", NULL, 351, 62626, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tempfile", NULL, 352, 26417, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"textwrap", NULL, 353, 13484, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"threading", NULL, 354, 39941, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"timeit", NULL, 355, 11742, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"token", NULL, 356, 2450, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tokenize", NULL, 357, 17125, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"trace", NULL, 358, 19991, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"traceback", NULL, 359, 19903, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tracemalloc", NULL, 360, 17328, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"tty", NULL, 361, 1041, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"types", NULL, 362, 9142, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"typing", NULL, 363, 62385, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib", NULL, 364, 84, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib.error", NULL, 365, 2774, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.parse", NULL, 366, 34388, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.request", NULL, 367, 72578, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.response", NULL, 368, 3254, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"urllib.robotparser", NULL, 369, 7292, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"uu", NULL, 370, 3570, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"uuid", NULL, 371, 23648, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"warnings", NULL, 372, 13617, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wave", NULL, 373, 18114, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"weakref", NULL, 374, 19483, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"webbrowser", NULL, 375, 17085, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref", NULL, 376, 680, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"wsgiref.handlers", NULL, 377, 16411, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.headers", NULL, 378, 7721, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.simple_server", NULL, 379, 5226, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.util", NULL, 380, 5377, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"wsgiref.validate", NULL, 381, 14720, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xdrlib", NULL, 382, 8186, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml", NULL, 383, 648, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom", NULL, 384, 5486, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom.NodeFilter", NULL, 385, 932, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.domreg", NULL, 386, 2815, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.expatbuilder", NULL, 387, 27306, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.minicompat", NULL, 388, 2707, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.minidom", NULL, 389, 55339, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.pulldom", NULL, 390, 10656, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.dom.xmlbuilder", NULL, 391, 12459, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree", NULL, 392, 87, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.etree.ElementInclude", NULL, 393, 1544, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementPath", NULL, 394, 8399, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementTree", NULL, 395, 55587, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.etree.cElementTree", NULL, 396, 138, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.parsers", NULL, 397, 261, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.parsers.expat", NULL, 398, 299, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax", NULL, 399, 3175, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.sax._exceptions", NULL, 400, 5409, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.expatreader", NULL, 401, 12460, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.handler", NULL, 402, 12387, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.saxutils", NULL, 403, 12884, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xml.sax.xmlreader", NULL, 404, 16809, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xmlrpc", NULL, 405, 84, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xmlrpc.client", NULL, 406, 34504, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"xmlrpc.server", NULL, 407, 29373, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zipapp", NULL, 408, 5819, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {"zipfile", NULL, 409, 58479, NUITKA_TRANSLATED_FLAG | NUITKA_BYTECODE_FLAG},
    {NULL, NULL, 0, 0, 0}
};

static void _loadBytesCodesBlob()
{
    static bool init_done = false;

    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode");

        init_done = true;
    }
}


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        _loadBytesCodesBlob();
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {
    {"_collections_abc", 50, 28706},
    {"abc", 64, 5299},
    {"codecs", 105, 33921},
    {"collections", 107, -46392},
    {"collections.abc", 108, 28705},
    {"copyreg", 119, 4283},
    {"dis", 130, 15773},
    {"encodings", 132, -3859},
    {"encodings.aliases", 133, 6295},
    {"encodings.ascii", 134, 1846},
    {"encodings.big5", 136, 1374},
    {"encodings.big5hkscs", 137, 1384},
    {"encodings.charmap", 139, 2856},
    {"encodings.cp037", 140, 2387},
    {"encodings.cp1006", 141, 2463},
    {"encodings.cp1026", 142, 2391},
    {"encodings.cp1125", 143, 8094},
    {"encodings.cp1140", 144, 2377},
    {"encodings.cp1250", 145, 2414},
    {"encodings.cp1251", 146, 2411},
    {"encodings.cp1252", 147, 2414},
    {"encodings.cp1253", 148, 2427},
    {"encodings.cp1254", 149, 2416},
    {"encodings.cp1255", 150, 2435},
    {"encodings.cp1256", 151, 2413},
    {"encodings.cp1257", 152, 2421},
    {"encodings.cp1258", 153, 2419},
    {"encodings.cp273", 154, 2373},
    {"encodings.cp424", 155, 2417},
    {"encodings.cp437", 156, 7811},
    {"encodings.cp500", 157, 2387},
    {"encodings.cp720", 158, 2484},
    {"encodings.cp737", 159, 8133},
    {"encodings.cp775", 160, 7841},
    {"encodings.cp850", 161, 7472},
    {"encodings.cp852", 162, 7849},
    {"encodings.cp855", 163, 8102},
    {"encodings.cp856", 164, 2449},
    {"encodings.cp857", 165, 7452},
    {"encodings.cp858", 166, 7442},
    {"encodings.cp860", 167, 7790},
    {"encodings.cp861", 168, 7805},
    {"encodings.cp862", 169, 7994},
    {"encodings.cp863", 170, 7805},
    {"encodings.cp864", 171, 7949},
    {"encodings.cp865", 172, 7805},
    {"encodings.cp866", 173, 8138},
    {"encodings.cp869", 174, 7829},
    {"encodings.cp874", 175, 2515},
    {"encodings.cp875", 176, 2384},
    {"encodings.cp932", 177, 1376},
    {"encodings.cp949", 178, 1376},
    {"encodings.cp950", 179, 1376},
    {"encodings.euc_jis_2004", 180, 1390},
    {"encodings.euc_jisx0213", 181, 1390},
    {"encodings.euc_jp", 182, 1378},
    {"encodings.euc_kr", 183, 1378},
    {"encodings.gb18030", 184, 1380},
    {"encodings.gb2312", 185, 1378},
    {"encodings.gbk", 186, 1372},
    {"encodings.hp_roman8", 188, 2588},
    {"encodings.hz", 189, 1370},
    {"encodings.iso2022_jp", 191, 1391},
    {"encodings.iso2022_jp_1", 192, 1395},
    {"encodings.iso2022_jp_2", 193, 1395},
    {"encodings.iso2022_jp_2004", 194, 1401},
    {"encodings.iso2022_jp_3", 195, 1395},
    {"encodings.iso2022_jp_ext", 196, 1399},
    {"encodings.iso2022_kr", 197, 1391},
    {"encodings.iso8859_1", 198, 2386},
    {"encodings.iso8859_10", 199, 2391},
    {"encodings.iso8859_11", 200, 2485},
    {"encodings.iso8859_13", 201, 2394},
    {"encodings.iso8859_14", 202, 2412},
    {"encodings.iso8859_15", 203, 2391},
    {"encodings.iso8859_16", 204, 2393},
    {"encodings.iso8859_2", 205, 2386},
    {"encodings.iso8859_3", 206, 2393},
    {"encodings.iso8859_4", 207, 2386},
    {"encodings.iso8859_5", 208, 2387},
    {"encodings.iso8859_6", 209, 2431},
    {"encodings.iso8859_7", 210, 2394},
    {"encodings.iso8859_8", 211, 2425},
    {"encodings.iso8859_9", 212, 2386},
    {"encodings.johab", 213, 1376},
    {"encodings.koi8_r", 214, 2438},
    {"encodings.koi8_t", 215, 2349},
    {"encodings.koi8_u", 216, 2424},
    {"encodings.kz1048", 217, 2401},
    {"encodings.latin_1", 218, 1858},
    {"encodings.mac_arabic", 219, 7705},
    {"encodings.mac_centeuro", 220, 2425},
    {"encodings.mac_croatian", 221, 2433},
    {"encodings.mac_cyrillic", 222, 2423},
    {"encodings.mac_farsi", 223, 2367},
    {"encodings.mac_greek", 224, 2407},
    {"encodings.mac_iceland", 225, 2426},
    {"encodings.mac_latin2", 226, 2567},
    {"encodings.mac_roman", 227, 2424},
    {"encodings.mac_romanian", 228, 2434},
    {"encodings.mac_turkish", 229, 2427},
    {"encodings.palmos", 230, 2414},
    {"encodings.ptcp154", 231, 2508},
    {"encodings.punycode", 232, 6280},
    {"encodings.quopri_codec", 233, 2380},
    {"encodings.raw_unicode_escape", 234, 1727},
    {"encodings.shift_jis", 236, 1384},
    {"encodings.shift_jis_2004", 237, 1394},
    {"encodings.shift_jisx0213", 238, 1394},
    {"encodings.tis_620", 239, 2476},
    {"encodings.undefined", 240, 2060},
    {"encodings.unicode_escape", 241, 1707},
    {"encodings.utf_16", 242, 4837},
    {"encodings.utf_16_be", 243, 1615},
    {"encodings.utf_16_le", 244, 1615},
    {"encodings.utf_32", 245, 4730},
    {"encodings.utf_32_be", 246, 1508},
    {"encodings.utf_32_le", 247, 1508},
    {"encodings.utf_7", 248, 1536},
    {"encodings.utf_8", 249, 1595},
    {"encodings.utf_8_sig", 250, 4511},
    {"encodings.uu_codec", 251, 3214},
    {"encodings.zlib_codec", 252, 3074},
    {"enum", 253, 25927},
    {"functools", 260, 27866},
    {"genericpath", 261, 3966},
    {"heapq", 268, 14035},
    {"importlib", 276, -3714},
    {"importlib._bootstrap", 277, 28570},
    {"importlib._bootstrap_external", 278, 45148},
    {"importlib.machinery", 280, 927},
    {"inspect", 284, 80558},
    {"io", 285, 3419},
    {"keyword", 292, 963},
    {"linecache", 293, 3832},
    {"locale", 294, 34639},
    {"opcode", 306, 5385},
    {"operator", 307, 13656},
    {"os", 308, 31362},
    {"posixpath", 316, 10393},
    {"quopri", 322, 5713},
    {"re", 324, 14387},
    {"reprlib", 325, 5268},
    {"sre_compile", 338, 15107},
    {"sre_constants", 339, 6324},
    {"sre_parse", 340, 21612},
    {"stat", 342, 4337},
    {"token", 356, 2450},
    {"tokenize", 357, 17125},
    {"types", 362, 9142},
    {"warnings", 372, 13617},
    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    _loadBytesCodesBlob();

    struct frozen_desc *current = _frozen_modules;

    for (;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}

