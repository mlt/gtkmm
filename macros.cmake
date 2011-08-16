# this will create hard links from gtk+ submodule folders for all
# CMakeLists.txt files in gtk+.local
macro(MKLINK FROM TO)
file(GLOB_RECURSE CMAKE_GTK_FILES
     RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}/${FROM}
     ${FROM}/*CMakeLists.txt ${FROM}/CMakeLists.txt) 
foreach(FILE ${CMAKE_GTK_FILES})
  set(LINK ${CMAKE_CURRENT_SOURCE_DIR}/${TO}/${FILE})
  file(TO_NATIVE_PATH ${LINK} LINK)
  if(NOT EXISTS ${LINK})
    file(TO_NATIVE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/${FROM}/${FILE} TARGET)
    execute_process(COMMAND cmd /C mklink /H "${LINK}" "${TARGET}")
  endif()
endforeach(FILE)
endmacro()

macro(GET URL)
get_filename_component(FILE ${URL} NAME)
string(REGEX REPLACE "(.+)-.+" "\\1" NAME ${FILE})
string(REGEX REPLACE ".+-([0-9]+)[.]([0-9]+)[.]([0-9]+)[.].+" "\\1.\\2.\\3" VERSION ${FILE})
if(NOT EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${NAME}-${VERSION})
  message("Source directory ${NAME}-${VERSION} is missing")
  # Download stuff
  if(NOT EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${FILE})
    message("Downloading ${URL}")
    file(DOWNLOAD ${URL}
    ${CMAKE_CURRENT_SOURCE_DIR}/${FILE} SHOW_PROGRESS)
  endif()
  string(REGEX MATCH "tar.gz$" GZ ${FILE})
  message("Unpacking ${FILE}")
  if(${GZ})
    execute_process(COMMAND ${CMAKE_COMMAND} -E tar xjz ${FILE}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
  else()
    execute_process(COMMAND ${CMAKE_COMMAND} -E tar xjf ${FILE}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
  endif()
endif()
MKLINK(${NAME} ${NAME}-${VERSION})
endmacro()

macro(VERSION DIR VER)
string(REGEX REPLACE ".+-([0-9]+)[.]([0-9]+)[.].+" "\\1.\\2" ${VER} ${DIR})
endmacro()
