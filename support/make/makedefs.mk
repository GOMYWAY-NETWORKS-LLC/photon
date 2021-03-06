MKDIR=/bin/mkdir
RM=/bin/rm
RMDIR=/bin/rm -rf
CP=/bin/cp
MV=/bin/mv
TAR=/bin/tar
RPMBUILD=/usr/bin/rpmbuild
SED=/usr/bin/sed
SHASUM=/usr/bin/shasum
ARCH?=$(shell uname -m)

SRCROOT := $(realpath $(SRCROOT))
MAKEROOT := $(realpath $(MAKEROOT))

PHOTON_BUILD_TYPE?=chroot
PHOTON_STAGE?=$(SRCROOT)/stage
PHOTON_LOGS_DIR=$(PHOTON_STAGE)/LOGS
PHOTON_RPMS_DIR=$(PHOTON_STAGE)/RPMS
PHOTON_SRPMS_DIR=$(PHOTON_STAGE)/SRPMS
PHOTON_UPDATED_RPMS_DIR?=$(PHOTON_STAGE)/UPDATED_RPMS
PHOTON_SPECS_DIR?=$(SRCROOT)/SPECS
PHOTON_COMMON_DIR?=$(SRCROOT)/common
PHOTON_DATA_DIR?=$(PHOTON_COMMON_DIR)/data
PHOTON_SRCS_DIR=$(PHOTON_STAGE)/SOURCES
PHOTON_PUBLISH_RPMS_DIR=$(PHOTON_STAGE)/PUBLISHRPMS
PHOTON_PUBLISH_XRPMS_DIR=$(PHOTON_STAGE)/PUBLISHXRPMS
PHOTON_GENERATED_DATA_DIR=$(PHOTON_STAGE)/common/data

PHOTON_PKG_BUILDER_DIR=$(SRCROOT)/support/package-builder
PHOTON_PULL_PUBLISH_RPMS_DIR=$(SRCROOT)/support/pullpublishrpms
PHOTON_IMAGE_BUILDER_DIR=$(SRCROOT)/support/image-builder

PHOTON_INSTALLER_DIR=$(SRCROOT)/installer
PHOTON_INSTALLER=$(PHOTON_INSTALLER_DIR)/photonInstaller.py
PHOTON_SPECDEPS_DIR=$(SRCROOT)/support/package-builder
PHOTON_SPECDEPS=$(PHOTON_SPECDEPS_DIR)/SpecDeps.py
PHOTON_PACKAGE_BUILDER=$(PHOTON_PKG_BUILDER_DIR)/builder.py
PHOTON_DISTRIBUTED_BUILDER=$(PHOTON_PKG_BUILDER_DIR)/DistributedBuilder.py
PHOTON_GENERATE_OSS_FILES=$(PHOTON_PKG_BUILDER_DIR)/GenerateOSSFiles.py
ifdef PHOTON_PULLSOURCES_CONFIG
PHOTON_PULLSOURCES_CONFIG:=$(abspath $(PHOTON_PULLSOURCES_CONFIG))
else
PHOTON_PULLSOURCES_CONFIG?=$(PHOTON_PKG_BUILDER_DIR)/bintray.conf
endif
PHOTON_PULL_PUBLISH_RPMS=$(PHOTON_PULL_PUBLISH_RPMS_DIR)/pullpublishrpms.sh
PHOTON_PULL_PUBLISH_X_RPMS=$(PHOTON_PULL_PUBLISH_RPMS_DIR)/pullpublishXrpms.sh
PHOTON_IMAGE_BUILDER=$(PHOTON_IMAGE_BUILDER_DIR)/imagebuilder.py
PHOTON_PKGINFO_FILE=$(PHOTON_STAGE)/pkg_info.json

PHOTON_CHROOT_CLEANER=$(PHOTON_PKG_BUILDER_DIR)/clean-up-chroot.py
PHOTON_RPMS_DIR_NOARCH=$(PHOTON_RPMS_DIR)/noarch
PHOTON_RPMS_DIR_ARCH=$(PHOTON_RPMS_DIR)/$(ARCH)
PHOTON_UPDATED_RPMS_DIR_NOARCH?=$(PHOTON_UPDATED_RPMS_DIR)/noarch
PHOTON_UPDATED_RPMS_DIR_ARCH?=$(PHOTON_UPDATED_RPMS_DIR)/$(ARCH)

PHOTON_CHROOT_PATH:=$(PHOTON_STAGE)/photonroot
PHOTON_FS_ROOT=/usr/src/photon
PHOTON_DIST_TAG?=.ph3
PHOTON_INPUT_RPMS_DIR?=$(SRCROOT)/inputRPMS

ifdef INPUT_PHOTON_BUILD_NUMBER
PHOTON_BUILD_NUMBER=$(INPUT_PHOTON_BUILD_NUMBER)
else
PHOTON_BUILD_NUMBER=$(shell git rev-parse --short HEAD)
endif
PHOTON_RELEASE_MAJOR_ID=3.0
PHOTON_RELEASE_MINOR_ID=
PHOTON_RELEASE_VERSION=$(PHOTON_RELEASE_MAJOR_ID)$(PHOTON_RELEASE_MINOR_ID)
PHOTON_DOCKER_PY_VER=2.3.0

PHOTON_PKG_BLACKLIST_FILE=""
PHOTON_REPO_TOOL?="createrepo"
