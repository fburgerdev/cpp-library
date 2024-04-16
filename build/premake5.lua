-- premake5.lua
ROOT = ".."
PRJ_NAME = "PROJECT" --[[ MODIFY ]]
DEFAULT_TEST = "test" --[[ MODIFY ]]
-- workspace
workspace(PRJ_NAME)
   -- startproject
   startproject(DEFAULT_TEST)
   -- console
   kind "ConsoleApp"
   -- cpp
   language "C++"
   cppdialect "C++Latest"
   -- includedirs
   includedirs {
      ROOT,
      ROOT .. "/src",
      ROOT .. "/vendor",
   }
   -- files
   files {
      ROOT .. "/vendor/**",
   }
   -- obj
   objdir(ROOT .. "/bin/obj")
   -- debug
   debugger "GDB"
   -- config
   configurations { "debug", "release", "dist" }
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
project(PRJ_NAME)
   -- staticlib
   kind "StaticLib"
   -- includedirs
   includedirs {
      ROOT .. "/src",
      ROOT .. "/vendor",
   }
   -- files
   files {
      ROOT .. "/src/**",
      ROOT .. "/vendor/**",
   }
   -- config
   -- config :: debug
   filter "configurations:debug"
      -- targetdir
      targetdir(ROOT .. "/lib/debug/")
   -- config :: fast
   filter "configurations:release"
      -- targetdir
      targetdir(ROOT .. "/lib/release/")
   -- config :: dist
   filter "configurations:dist"
      -- targetdir
      targetdir(ROOT .. "/lib/dist/")
-- project :: tests
-- project :: tests :: test
project "test"
   -- files
   files {
      ROOT .. "/tests/test.cpp",
      --[[ INSERT ADDITIONAL FILES HERE ]]
      ROOT .. "/vendor/**",
   }
   -- link
   links { PRJ_NAME, --[[ INSERT ADDITIONAL LINKS HERE ]] }
   -- config
   -- config :: debug
   filter "configurations:debug"
      -- targetdir
      targetdir(ROOT .. "/bin/debug/test")
   -- config :: fast
   filter "configurations:release"
      -- targetdir
      targetdir(ROOT .. "/bin/release/test")
   -- config :: dist
   filter "configurations:dist"
      -- targetdir
      targetdir(ROOT .. "/bin/dist/test")
--[[ INSERT ADDITIONAL TESTS HERE ]]