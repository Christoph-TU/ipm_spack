# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.util.executable import Executable

class Ipm(AutotoolsPackage):
    """IPM is a portable profiling infrastructure for parallel codes.
       It provides a low-overhead profile of application performance
       and resource utilization in a parallel program. Communication,
       computation, and IO are the primary focus."""

    homepage = 'https://github.com/nerscadmin/IPM'
    git= 'https://github.com/nerscadmin/IPM.git'

    maintainers('Christoph-TU')

    sanity_check_is_dir = ['lib']

    version('2017-09-06', sha256='f74f6eb2d0cbe4d37f6e6efe03b123f71833dae9ffb16acc009522394891b0be', url='https://github.com/nerscadmin/IPM/tarball/02f0cdce630f0533e0aaadaccd8998a5e893968a')

    version('master', branch='master')

    version('2.0.6', tag='2.0.6')

    variant('papi', default=False, description='Enable PAPI')
    variant('cuda', default=False, description='Enable CUDA')
    variant('libunwind', default=False, description='Enable libunwind')

    variant('papi_multiplexing', default=False, when='+papi', description='Enable PAPI multiplexing')
    variant('posixio', default=False, description='Enable posixio')
    variant('pmon', default=False, description='Enable power monitoring module')
    variant('parser', default=False, description='Enable building the ipm parser')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    depends_on('mpi')
    depends_on('papi', when='+papi')
    depends_on('cuda', when='+cuda')
    depends_on('libunwind', when='+libunwind')
    depends_on('mxml', when='+parser')

    def setup_build_environment(self, env):
        spec = self.spec
        env.set('MPICC', spec['mpi'].mpicc)
        env.set('MPIFC', spec['mpi'].mpifc)

    def autoreconf(self, spec, prefix):
        script = Executable(join_path(self.stage.source_path, 'bootstrap.sh'))
        script()

    def configure_args(self):
        args = []
        spec = self.spec
        if '+papi' in spec:
            args.append('--with-papi={0}'.format(spec['papi'].prefix))

        if '+cuda' in spec:
            args.append('--with-cudapath={0}'.format(spec['cuda'].prefix))

        if '+libunwind' in spec:
            args.append('--with-libunwind={0}'.format(spec['libunwind'].prefix))

        if '+parser' in spec:
            args.append('--enable-parser')
            args.append('--with-mxmlpath={0}'.format(spec['mxml'].prefix))

        if '+papi_multiplexing' in spec:
            args.append('--enable-papi-multiplexing')

        if '+posixio' in spec:
            args.append('--enable-posixio')

        if '+pmon' in spec:
            args.append('--enable-pmon')

        args.extend(
            [
                'CFLAGS={0}'.format(self.compiler.cc_pic_flag),
                'CXXFLAGS={0}'.format(self.compiler.cxx_pic_flag),
            ]
        )
        return args
