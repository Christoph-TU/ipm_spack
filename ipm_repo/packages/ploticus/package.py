# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ploticus(MakefilePackage):
    """Ploticus can produce various types of plots and graphs."""

    homepage = "http://ploticus.sourceforge.net/doc/welcome.html"
    url = "https://sourceforge.net/projects/ploticus/files/ploticus/2.42/ploticus242_src.tar.gz/download"

    maintainers("Christoph-TU")

    version("2.42", sha256="3f29e4b9f405203a93efec900e5816d9e1b4381821881e241c08cab7dd66e0b0")

    depends_on("zlib")
    depends_on("libpng")

    build_directory = "src"

    def setup_run_environment(self, env):
        env.set("PLOTICUS_PREFABS", self.prefix.prefabs)

    def edit(self, spec, prefix):
        makefile = FileFilter("src/Makefile")
        makefile.filter("CC = .*", "CC = {0}".format(spack_cc))

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.prefabs)
        install("src/pl", prefix.bin)
        install_tree("prefabs", prefix.prefabs)
