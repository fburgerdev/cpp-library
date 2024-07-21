-- premake5.lua
ROOT = ".."

-- workspace
workspace "__PROJECT_NAME__"
   -- startproject
   startproject "__START_PROJECT__"
   -- cpp
   language "C++"
   cppdialect "C++20"

   -- debug
   debugger "GDB"

   -- defines
   defines { __DEFINES__ }

   -- dependancies
   -- :: directories
   libdirs {
      ROOT .. "/lib/%{cfg.buildcfg}",
      ROOT .. "/modules/*/lib/%{cfg.buildcfg}",
      ROOT .. "/vendor/*/lib/%{cfg.buildcfg}"
   }
   -- :: libraries
   links { "__PROJECT_NAME__", __LINKS__ --[[ INSERT ADDITIONAL LINKS HERE ]] }

   -- config
   configurations { "debug", "release", "dist" }
   -- :: debug
   filter "configurations:debug"
      symbols "On"
      defines { "CONFIG_DEBUG" }
      -- precompiled headers
      pchheader "common.hpp"
      pchsource "common.cpp"
   -- :: release
   filter "configurations:release"
      optimize "On"
      defines { "CONFIG_RELEASE" }
      linkoptions{ "-Ofast" }
   -- :: dist
   filter "configurations:dist"
      optimize "On"
      defines { "CONFIG_DIST" }
      linkoptions { "-Ofast" }
   
   -- system
   -- :: windows
   filter "system:windows"
      defines { "SYSTEM_WINDOWS" }
   -- :: linux
   filter "system:linux"
      defines { "SYSTEM_LINUX" }
   
   -- toolset
   -- :: gcc
   filter "toolset:gcc"
      buildoptions { "-Wall", "-Wextra", "-Wpedantic" }

-- project lib
project "__PROJECT_NAME__"
   -- static library
   kind "StaticLib"

   -- include
   includedirs {
      ROOT,
      ROOT .. "/src",
      ROOT .. "/modules/*/include",
      ROOT .. "/vendor/*/include"
   }
   -- files
   files {
      ROOT .. "/src/**",
      ROOT .. "/vendor/*/src/**",
   }
   
   -- binaries
   targetdir(ROOT .. "/lib/%{cfg.buildcfg}")
   objdir(ROOT .. "/bin/%{cfg.system}_%{cfg.buildcfg}")