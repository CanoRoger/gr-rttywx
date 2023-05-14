find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_RTTYWX gnuradio-rttywx)

FIND_PATH(
    GR_RTTYWX_INCLUDE_DIRS
    NAMES gnuradio/rttywx/api.h
    HINTS $ENV{RTTYWX_DIR}/include
        ${PC_RTTYWX_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_RTTYWX_LIBRARIES
    NAMES gnuradio-rttywx
    HINTS $ENV{RTTYWX_DIR}/lib
        ${PC_RTTYWX_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-rttywxTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_RTTYWX DEFAULT_MSG GR_RTTYWX_LIBRARIES GR_RTTYWX_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_RTTYWX_LIBRARIES GR_RTTYWX_INCLUDE_DIRS)
