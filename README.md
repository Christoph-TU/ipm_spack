# IPM Spack Package

## Introduction

This readme provides guidance on locally installing and utilizing IPM with Spack.

When you use these instructions, Spack's configurations will be temporarily altered. New installations will be stored under `ipm_spack/spack` in this repository. This approach is designed for users to install IPM without needing write permissions on the main Spack instance. Additionally, it will try to reuse pre-existing packages already installed or accessible via Spack. If your primary Spack instance isn't found at `$spack/opt/spack`, modifications in the `ipm_scope/upstreams.yaml` file may be needed.

## Adding IPM to Spack

For individual user installation and use, follow these steps:

```bash
git clone https://github.com/Christoph-TU/ipm_spack.git
export SPACK_USER_CONFIG_PATH=$(pwd)/ipm_spack/ipm_scopes/
```

This command sequence sets your user configurations to the specified directory. Once set, all subsequent package installations will be saved to the local filesystem. This change remains effective until the environment variable is unset. By executing the above, IPM will also be added to the roster of available packages, and it will establish a reference to the location of the main Spack installation packages.

Alternatively, you can precede each Spack command with:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/
```

For example:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/ info ipm
spack -C /path/to/ipm_spack/ipm_scopes/ install ipm
```

After this, you can use the IPM like any other package.

## Inspecting the IPM Package

To obtain detailed information about the IPM package, run:

```bash
spack info ipm
```

## Using IPM

Use IPM as follows:

```bash
LD_PRELOAD=$(spack location -i ipm)/lib/libipm.so mpirun ./a.out
```

## Cleanup

To remove IPM while the environment is active, use `spack uninstall ipm` or:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/ uninstall ipm
```

If desired, you can also delete the entire Spack directory inside the git repo.

To unset the environment variable:

```bash
unset SPACK_USER_CONFIG_PATH
```

## Known Issues

When the `+parser` option is enabled, IPM will build its proprietary version. If disabled, the perl script will be used instead. Note: On certain machines, enabling `+parser` may result in build complications.