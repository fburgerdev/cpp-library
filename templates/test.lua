-- tests :: PROJECT_NAME
project "TEST_NAME"
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
      --[[ INSERT ADDITIONAL FILES HERE ]]
   }
   -- links
   links { "WORKSPACE_NAME", --[[ INSERT ADDITIONAL LINKS HERE ]] }
   -- binaries
   targetdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}")
   objdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}/obj")