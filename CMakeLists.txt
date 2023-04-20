cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)
project(test_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()
add_executable(air-con
  air-con.c
)
pico_enable_stdio_usb(air-con 1)
pico_enable_stdio_uart(air-con 1)
pico_add_extra_outputs(air-con)
target_include_directories(air-con PRIVATE ${CMAKE_CURRENT_LIST_DIR} )
target_link_libraries(air-con pico_cyw43_arch_lwip_threadsafe_background pico_stdlib)