-- tests :: __TEST_NAME__
project "__TEST_NAME__"
   -- console
   kind "ConsoleApp"
   -- include directories
   includedirs {
      ROOT .. "/include",
      ROOT .. "/src",
      ROOT .. "/modules/*/include",
      ROOT .. "/vendor/*/include"
   }
   -- library directories
   libdirs {
      ROOT .. "/lib/%{cfg.buildcfg}",
      ROOT .. "/modules/*/lib/%{cfg.buildcfg}",
      ROOT .. "/vendor/*/lib/%{cfg.buildcfg}"
   }
   -- files
   files {
      __FILES__ --[[ INSERT ADDITIONAL FILES HERE ]]
   }
   -- links
   links { "__PROJECT_NAME__", __LINKS__ --[[ INSERT ADDITIONAL LINKS HERE ]] }
   -- defines
   defines { __DEFINES__ }
   -- binaries
   targetdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}")
   objdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}/obj")