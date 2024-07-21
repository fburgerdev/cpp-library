-- tests :: __TEST_NAME__
project "__TEST_NAME__"
   -- console
   kind "ConsoleApp"

   -- include
   includedirs {
      ROOT .. "/include",
      ROOT .. "/src",
      ROOT .. "/modules/*/include",
      ROOT .. "/vendor/*/include"
   }
   -- files
   files {
      __FILES__--[[ INSERT ADDITIONAL FILES HERE ]]
   }

   -- defines
   defines { __DEFINES__ }

   -- libraries
   links { "__PROJECT_NAME__", __LINKS__ --[[ INSERT ADDITIONAL LINKS HERE ]] }

   -- binaries
   targetdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}")
   objdir(ROOT .. "/bin/tests/%{cfg.system}_%{cfg.buildcfg}/obj")