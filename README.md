# IPM Spack Package

## Introduction

This document provides instructions on how to add, inspect, and remove the IPM package within Spack.

## Adding IPM to Spack

To add IPM to your available Spack packages, execute the following commands:

```bash
git clone https://github.com/Christoph-TU/ipm_spack.git
spack repo add ./ipm_spack/ipm_repo
```

## Inspecting the IPM Package

Once added, you can retrieve more information about the IPM package with the following command:

```bash
spack info ipm
```

## Installing IPM

To install the IPM package, use the command:

```bash
spack install ipm
```

## Removing IPM from Spack

If you wish to remove IPM from your list of available Spack packages, execute these commands:

```bash
spack uninstall -a -y ipm
spack repo remove ipm_repo
```