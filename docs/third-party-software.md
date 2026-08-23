# Third-Party Software

What MinuteSim distributes, what it expects you to have installed, and under which licenses.
Provided for attribution and product transparency. Third-party components remain subject to their
own licenses; this page is not legal advice.

Component versions below are those of the current 0.9.0-beta.1 release package and may change
between releases.

## 1. Distributed with MinuteSim

Shipped as binaries alongside the solver executables.

| Component | Version | Role | License |
|---|---|---|---|
| [HDF5](https://www.hdfgroup.org/solutions/hdf5/) | 2.0.0 | Result file container. MinuteSim writes its results as HDF5 datasets with an XDMF index | HDF Group license (BSD-3-Clause style) |
| [zlib](https://zlib.net/) | 1.3.1 | Compression support used by HDF5 | zlib license |
| [libaec](https://gitlab.dkrz.de/k202009/libaec) | 1.1.5 | Provides HDF5's SZIP-compatible compression interface | BSD-2-Clause |

All three permit commercial use and binary redistribution. Each requires that its copyright notice
and license text accompany the distribution.

## 2. Statically linked into the solver

| Component | Role | License |
|---|---|---|
| NVIDIA CUDA Runtime | GPU execution support, linked into the MinuteSim executables | NVIDIA CUDA EULA |

No separate CUDA redistributable file is shipped.

## 3. Runtime prerequisites — installed by you, not distributed

| Component | Why it is needed |
|---|---|
| Microsoft Visual C++ Redistributable | The MinuteSim executables will not start without it. **Not bundled.** |
| NVIDIA display driver | Required for GPU execution |

## 4. Optional and planned components

| Component | Relationship | License | Status |
|---|---|---|---|
| [MMG](https://www.mmgtools.org/) | Used by the optional remeshing capability as a dynamically linked shared library. No MMG source is compiled into any MinuteSim component | LGPL-3.0-or-later | **Not part of the 0.9.0-beta.1 release package.** If the remeshing capability is distributed, MMG's license text, its notice, and an offer for the corresponding source accompany it, and the shipped MMG library can be replaced by a user-built one |
| [Gmsh](https://gmsh.info/) | An optional workflow can drive a Gmsh installation you provide, as a separate program exchanging ordinary mesh files. No Gmsh code is linked into or compiled into MinuteSim | GPL-2.0-or-later | **Not distributed with MinuteSim.** You install it yourself if you want that workflow |

## What is not listed here

Tools used only to develop, test or post-process during MinuteSim's own development are not listed,
because they are not distributed to you and impose no obligation on your use of the product. This
page covers what ships and what you must install.

## Obtaining license texts

The 0.9.0-beta.1 package does not yet bundle the license texts; adding them is tracked work for the
first commercial release. Until then, the official sources are:

- HDF5 — [hdfgroup.org](https://www.hdfgroup.org/solutions/hdf5/)
- zlib — [zlib.net](https://zlib.net/)
- libaec — [gitlab.dkrz.de/k202009/libaec](https://gitlab.dkrz.de/k202009/libaec)
- MMG — [mmgtools.org](https://www.mmgtools.org/)
- NVIDIA CUDA — [docs.nvidia.com/cuda/eula](https://docs.nvidia.com/cuda/eula/)

MinuteSim itself is proprietary software and is not open source. See [Availability](../README.md).
