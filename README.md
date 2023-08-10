# IPM Spack Package

## Introduction

This document provides instructions on how to activate a new environment and test IPM within it.

The environment is set up so that any new installations will be saved in this repository, specifically under `ipm_spack/spack`. This design allows users to install without needing write permissions for the main Spack instance. Moreover, it aims to reuse any existing packages that have already been installed or are available via Spack when possible. If the main Spack instance isn't located at `$spack/opt/spack`, adjustments may be required in the `spack.yaml` file settings.

## Adding IPM to Spack

To use and install IPM locally for an individual user, follow these steps:

```bash
git clone https://github.com/Christoph-TU/ipm_spack.git
spack env activate ./ipm_spack
```

This action will initialize a new environment with the IPM package available.

## Inspecting the IPM Package

To retrieve detailed information about the IPM package, execute:

```bash
spack info ipm
```

It is recommended to first run:

```bash
spack spec ipm
```

This command helps determine whether existing packages are correctly identified as available dependencies. Look for a green `[^]` or `[e]` square next to each dependency. If you encounter only `-` symbols, especially for packages that should be present in the main Spack instance, consider adjusting the `spack-instance-1:install_tree:` variable within the `spack.yaml` file.

## Installing IPM

With the environment active, IPM can be installed using:

```bash
spack add ipm
spack install
```

Or alternatively:

```bash
spack install --add ipm
```

It's essential to understand that only the packages (and their dependencies) added via `spack add`, and subsequently installed using `spack install`, will be accessible within the environment.

## Using IPM

In the active environment, to make use of IPM, run:

```bash
spack load ipm
LD_PRELOAD=$(spack location -i ipm)/lib/libipm.so mpirun ./a.out
```

## Removing IPM from Spack

To revert to standard Spack installations, enter:

```bash
spack env deactivate
```

For pre-deactivation cleanup, use:

```bash
spack uninstall -ay
spack remove -a
```

## Known Issues

When +parser is enabled, IPM's proprietary version will be built. Conversely, when it's disabled, the perl script will be available instead. On some machines, +parser may encounter build issues.