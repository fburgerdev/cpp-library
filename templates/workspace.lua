-- premake5.lua
ROOT = ".."
-- workspace
workspace "__PROJECT_NAME__"
   -- build options
   configurations { "debug", "release", "dist" }
   -- startproject
   startproject "__START_PROJECT__"
   -- cpp
   language "C++"
   cppdialect "C++Latest"
   -- debug
   debugger "GDB"
   -- defines
   defines { __DEFINES__ }
   -- config
   -- config :: debug
   filter "configurations:debug"
      symbols "On"
      defines { "CONFIG_DEBUG" }
   -- config :: fast
   filter "configurations:release"
      optimize "On"
      defines { "CONFIG_RELEASE" }
      linkoptions{ "-Ofast" }
   -- config :: dist
   filter "configurations:dist"
      optimize "On"
      defines { "CONFIG_DIST" }
      linkoptions { "-Ofast" }
-- project lib
project "__PROJECT_NAME__"
   -- static library
   kind "StaticLib"
   -- include directories
   includedirs {
      ROOT,
      ROOT .. "/src",
      ROOT .. "/modules/*/include",
      ROOT .. "/vendor/*/include"
   }
   -- files
   files {
      ROOT .. "/src/**",
      ROOT .. "/vendor/**",
   }
   -- binaries
   targetdir(ROOT .. "/lib/%{cfg.buildcfg}")
   objdir(ROOT .. "/bin/%{cfg.system}_%{cfg.buildcfg}")