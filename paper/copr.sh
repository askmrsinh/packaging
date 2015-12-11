#!/bin/bash

# copr.sh -- shell script to do a Copr release of paper-icon-theme
#
# Copyright (C) 2015 Ashesh Kumar Singh <user501254@gmail.com>
#
# This script may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.
#

set -e
set -o pipefail

# Mirror Project's latest Launchpad build if it was successful and is not available in Copr
REVISION=$(wget "https://launchpad.net/paper-icon-theme/trunk" -O - | grep -P "[0-9]{3} revisions." | grep -Po "[0-9]{3}")
if [[ $(wget "https://copr.fedoraproject.org/api/coprs/user501254/Paper/monitor/" -O - | grep -Po '"pkg_version": "0-0.[0-9]{3}' | head -n 1| cut -c 21-) != "$REVISION" ]]; then
  if [[ $(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=&build_state=failed" -O - | grep "paper-icon-theme 1.0+r$REVISION~daily~ubuntu") == "" && $(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=&build_state=built" -O - | grep "paper-icon-theme 1.0+r$REVISION~daily~ubuntu") != "" ]]; then
    echo -e "\e[0;34mLast Launchpad build $REVISION was successful.\e[0m"
  else
    echo -e "\e[0;31mLast Launchpad build $REVISION failed or is being built. Exiting.\e[0m"
    exit
  fi
else
  echo -e "\e[0;32m$REVISION is already available in Copr repo. Exiting.\e[0m"
  exit
fi

# Make sure that there are no modified, untracked files and everything is up-to-date
if [[ "$(git status -s --ignore-submodules)" == "" ]]; then
  git submodule foreach git pull origin master
  git add paper-*-theme
  git commit -m "Update from origin"
  git push
  if [[ $(wget "http://bazaar.launchpad.net/~snwh/paper-icon-theme/paper-icon-theme-git/files/$REVISION" -O - | grep "git-v1" | head -n 1 | grep -Po "[0-9a-z]{40}") == "$(git ls-tree origin/master paper-icon-theme | grep -Po [a-z0-9]{40})" && "$(git rev-parse packaging)" == "$(git rev-parse origin/packaging)" ]]; then
    GIT_SHA=$(git ls-tree origin/master paper-icon-theme | grep -Po "[a-z0-9]{40}")
    CHECKOUT=20151211git${GIT_SHA:0:7}
  else
    git status
    echo -e "\e[0;31m\nExiting.\e[0m"
    exit
  fi
else 
  git submodule status
  echo -e "\e[0;31m\nExiting.\e[0m"
  exit
fi

# Setup directories and files
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

# Generate tarball, similar in structure to those that are downloaded from GitHub
tar -czf "rpmbuild/SOURCES/paper-icon-theme-$GIT_SHA.tar.gz" paper-icon-theme/* --transform s/paper-icon-theme/paper-icon-theme-$GIT_SHA/

# Set commit0 value within spec file
sed -i "s/%global commit0 .*/$GIT_SHA/" rpmbuild/SPECS/paper-icon-theme.spec

# Set version and release tag value within spec file
sed -i "s/version:    .*/version:    0/; s/release:    .*/release:    0.$REVISION.$CHECKOUT%{?dist}/" rpmbuild/SPECS/paper-icon-theme.spec

# Build only Source RPM
rpmbuild --define "_topdir $PWD/rpmbuild" -bs rpmbuild/SPECS/paper-icon-theme.spec

# Submit Source RPM to Copr
PKG_VERSION=0-0.$REVISION.$CHECKOUT.$(uname -a | grep -Po "fc[0-9]{2}")
echo -e "\e[0;34m\nUploading paper-icon-theme-$PKG_VERSION.src.rpm to Copr\e[0m"
copr-cli build Paper "rpmbuild/SRPMS/paper-icon-theme-$PKG_VERSION.src.rpm" -r epel-7-x86_64 -r fedora-22-i386 -r fedora-22-x86_64 -r fedora-23-i386 -r fedora-23-x86_64

# Cleanup
rm -r rpmbuild/SRPMS/paper-icon-theme-$PKG_VERSION.src.rpm
rm -r rpmbuild/SOURCES/paper-icon-theme-$GIT_SHA.tar.gz

# Update
git add rpmbuild/SPECS/paper-icon-theme.spec
git commit -m "Update spec file"
git push

