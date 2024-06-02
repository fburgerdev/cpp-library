-- premake5.lua
ROOT = ".."
PROJECT_NAME = "PROJECT" --[[ MODIFY ]]
DEFAULT_TEST = "test" --[[ MODIFY ]]
-- workspace
workspace(PROJECT_NAME)
   -- build options
   configurations { "debug", "release", "dist" }
   -- startproject
   startproject(DEFAULT_TEST)
   -- console
   kind "ConsoleApp"
   -- cpp
   language "C++"
   cppdialect "C++20"
   -- includedirs
   includedirs {
      ROOT .. "/src",
      ROOT .. "/vendor/*/include",
   }
   -- bin
   -- bin :: targetdir
   targetdir(ROOT .. "/bin/%{cfg.buildcfg}_%{prj.name}")
   -- bin :: objdir
   objdir(ROOT .. "/bin/obj/%{cfg.system}_%{cfg.buildcfg}/%{prj.name}")
   -- debug
   debugger "GDB"
   -- config
   -- config :: debug
   filter "configurations:debug"
      -- symbols
      symbols "On"
      -- define
      defines { "CONFIG_DEBUG" }
   -- config :: fast
   filter "configurations:release"
      -- optimize
      optimize "On"
      -- define
      defines { "CONFIG_RELEASE" }
      -- linkoptions
      linkoptions{ "-Ofast" }
   -- config :: dist
   filter "configurations:dist"
      -- optimize
      optimize "On"
      -- define
      defines { "CONFIG_DIST" }
      -- linkoptions
      linkoptions { "-Ofast" }
-- project
-- project :: lib
project(PROJECT_NAME)
   -- staticlib
   kind "StaticLib"
   -- includedirs
   includedirs {
      ROOT .. "/vendor/*/include",
   }
   -- files
   files {
      ROOT .. "/src/**",
   }
   -- bin
   -- bin :: targetdir
   targetdir(ROOT .. "/lib/%{cfg.buildcfg}")
   -- bin :: obj
   objdir(ROOT .. "/bin/obj/%{cfg.system}_%{cfg.buildcfg}")
-- project :: tests
project "test"
   -- files
   files {
      ROOT .. "/tests/%{prj.name}.cpp",
      --[[ INSERT ADDITIONAL FILES HERE ]]
   }
   -- libdirs
   libdirs {
      ROOT .. "lib/%{cfg.system}",
      ROOT .. "/vendor/*/lib/%{cfg.buildcfg}",
      --[[ INSERT ADDITIONAL LIB DIRECTORIES HERE ]]
   }
   -- links
   links { PROJECT_NAME, --[[ INSERT ADDITIONAL LIBS HERE ]] }
--[[ INSERT ADDITIONAL TESTS HERE ]]