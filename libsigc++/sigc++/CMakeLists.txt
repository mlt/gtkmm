SET(SIGC_SRCS
connection.cc
adaptors/lambda/lambda.cc
signal.cc
signal_base.cc
functors/slot.cc
functors/slot_base.cc
trackable.cc
)

add_definitions( -DSIGC_BUILD -D_WINDLL )

add_library(sigc-${SIGC_VERSION} SHARED ${SIGC_SRCS})

install(TARGETS sigc-${SIGC_VERSION}
LIBRARY DESTINATION "lib"
ARCHIVE DESTINATION "lib"
RUNTIME DESTINATION "bin")

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/sigc-${SIGC_VERSION}${POSTFIX}.pdb DESTINATION "bin" CONFIGURATIONS DEBUG)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../${EXTRA}/sigc++config.h DESTINATION "lib/sigc++-${SIGC_VERSION}/include")

install(DIRECTORY ./ DESTINATION include/sigc++-${SIGC_VERSION}/sigc++/ FILES_MATCHING PATTERN "*.h"
PATTERN "macros" EXCLUDE
)
#install(DIRECTORY functors/ DESTINATION include/sigc++-${SIGC_VERSION}/functors/ FILES_MATCHING PATTERN "*.h")
#install(DIRECTORY adaptors/ DESTINATION include/sigc++-${SIGC_VERSION}/adaptors/ FILES_MATCHING PATTERN "*.h")
#install(DIRECTORY adaptors/lambda/ DESTINATION include/sigc++-${SIGC_VERSION}/adaptors/lambda/ FILES_MATCHING PATTERN "*.h")
