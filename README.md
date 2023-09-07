# IPM Spack Package

## Introduction

This git repo contains minimal configuration files and instructions for users to install the profiler IPM locally with Spack without needing write access to the main Spack instance. New installations will be stored under `ipm_spack/spack` in this repository. Although packages will be installed in a different directory, it will still attempt to reuse pre-existing packages already installed or accessible via Spack. If the primary Spack instance is not located at `$spack/opt/spack`, modifications in the `ipm_spack/upstreams.yaml` file may be necessary.

## Adding IPM to Spack

For individual user installation and use the following two command are sufficent:

```bash
git clone https://github.com/Christoph-TU/ipm_spack.git
export SPACK_USER_CONFIG_PATH=$(pwd)/ipm_spack/ipm_scopes/
```

This command sequence sets the user configurations to the specified directory. Once set, all subsequent package installations will be saved to the local filesystem. This change remains effective until the environment variable is unset. By executing the above, IPM will also be added to the list of available packages. After this, IPM can be used like any other package.

Alternatively, each Spack command can be precede like so:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/
```

For example:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/ info ipm
spack -C /path/to/ipm_spack/ipm_scopes/ install ipm
```

This approach may be desireable if the user config was modified and one wishes to keep using some of the features. With this approach only the necessary configurations needed for the installation will be overwritten with the rest remaining unchanged.

## Inspecting the IPM Package

To obtain additional information about the IPM package:

```bash
spack info ipm
```

## Using IPM

For usage, preloading IPM can be done via:

```bash
LD_PRELOAD=$(spack location -i ipm)/lib/libipm.so mpirun ./a.out
```

## Using the Parser

When building, the option `+parser` can be used to install the dependencies required for the parser. This includes ploticus.

After installation, the parser can easily be used by loading IPM with `spack load ipm`. Afterwards, the parser can be invoked like so:

```bash
ipm_parse -h
```

Example of using the html option:

```bash
export IPM_LOG=full
LD_PRELOAD=$(spack location -i ipm)/lib/libipm.so mpirun ./a.out

export IPM_KEYFILE=$(spack location -i ipm)/etc/ipm_key_mpi
ipm_parse -html output.ipm.xml
```

## Cleanup

While the environment is set, `spack uninstall ipm` can be used for cleanup or alternatively:

```bash
spack -C /path/to/ipm_spack/ipm_scopes/ uninstall ipm
```

can be used.

If desired, the entire Spack directory inside the git repo can be deleted.

To unset the environment variable:

```bash
unset SPACK_USER_CONFIG_PATH
```
