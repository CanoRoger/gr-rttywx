find_package(PkgConfig)

PKG_CHECK_MODULES(PC_RTTYWX rttywx)

FIND_PATH(
    RTTYWX_INCLUDE_DIRS
    NAMES rttywx/api.h
    HINTS $ENV{RTTYWX_DIR}/include
        ${PC_RTTYWX_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RTTYWX_LIBRARIES
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

include("${CMAKE_CURRENT_LIST_DIR}/rttywxTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RTTYWX DEFAULT_MSG RTTYWX_LIBRARIES RTTYWX_INCLUDE_DIRS)
MARK_AS_ADVANCED(RTTYWX_LIBRARIES RTTYWX_INCLUDE_DIRS)
