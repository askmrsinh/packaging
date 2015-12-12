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
build_info=($(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=paper-icon-theme&build_state=all" --no-cache -O - | grep -Po "build of paper-icon-theme [0-9].[0-9]\+r[0-9]{3}" | head -n 1 | grep -Po "[0-9.]{3}"))
Version=${build_info[0]}.0
Revision=0.${build_info[1]}
if [[ $(wget "https://copr.fedoraproject.org/api/coprs/user501254/Paper/monitor/" --no-cache -O - | grep -Po "[0-9.]{5}-[0-9.]{5}" | head -n 1) != "$Version-$Revision" ]]; then
  if [[ $(wget "https://launchpad.net/paper-icon-theme/trunk" --no-cache -O - | grep -P "[0-9]{3} revisions." | grep -Po "[0-9]{3}") != "${build_info[1]}" ]]; then
    echo -e "\e[0;34mThese's a pending Launchpad import. Exiting.\e[0m"
    exit
  fi
  if [[ $(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=paper-icon-theme&build_state=building" --no-cache -O - | grep "paper-icon-theme ${build_info[0]}+r${build_info[1]}~daily~ubuntu") != "" ]]; then
    echo -e "\e[0;34mThese's a pending Launchpad build. Exiting.\e[0m"
    exit
  fi
  if [[ $(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=paper-icon-theme&build_state=built" --no-cache -O - | grep "paper-icon-theme ${build_info[0]}+r${build_info[1]}~daily~ubuntu") != "" ]]; then
    echo -e "\e[0;34mLast Launchpad build paper-icon-theme ${build_info[0]}+r${build_info[1]}~daily~ubuntu was a success.\e[0m"
  else
    echo -e "\e[0;31mLast Launchpad build paper-icon-theme ${build_info[0]}+r${build_info[1]}~daily~ubuntu was a failure. Exiting.\e[0m"
    exit
  fi
else
  echo -e "\e[0;32m\"pkg_version\" $Version-$Revision is already available in Copr repo. Exiting.\e[0m"
  exit
fi

# Make sure that there are no modified, untracked files and everything is up-to-date
if [[ "$(git status -s --ignore-submodules)" == "" ]]; then
  git submodule foreach git pull origin master
  git add paper-*-theme || true
  git commit -m "Update from origin" || true
  git push || true
  if [[ $(wget "http://bazaar.launchpad.net/~snwh/paper-icon-theme/paper-icon-theme-git/files/${build_info[1]}" --no-cache -O - | grep "git-v1" | head -n 1 | grep -Po "[0-9a-z]{40}") == "$(git ls-tree origin/master paper-icon-theme | grep -Po [a-z0-9]{40})" && "$(git rev-parse HEAD)" == "$(git rev-parse origin/HEAD)" ]]; then
    GitSha=$(git ls-tree origin/master paper-icon-theme | grep -Po "[a-z0-9]{40}")
    Checkout=20151212git${GitSha:0:7}
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
tar -czf "rpmbuild/SOURCES/paper-icon-theme-$GitSha.tar.gz" paper-icon-theme/* --transform "s/paper-icon-theme/paper-icon-theme-$GitSha/"

# Set commit0 value within spec file
sed -i "s/%global commit0 .*/%global commit0 $GitSha/" rpmbuild/SPECS/paper-icon-theme.spec

# Set version and release tag value within spec file
sed -i "s/version:    .*/version:    $Version/; s/release:    .*/release:    $Revision.$Checkout%{?dist}/" rpmbuild/SPECS/paper-icon-theme.spec

# Build only Source RPM
rpmbuild --define "_topdir $PWD/rpmbuild" -bs rpmbuild/SPECS/paper-icon-theme.spec

# Submit Source RPM to Copr
PkgVersion=$Version-$Revision.$Checkout.$(uname -a | grep -Po "fc[0-9]{2}")
echo -e "\e[0;34m\nUploading paper-icon-theme-$PkgVersion.src.rpm to Copr\e[0m"
copr-cli build Paper "rpmbuild/SRPMS/paper-icon-theme-$PkgVersion.src.rpm" -r epel-7-x86_64 -r fedora-22-i386 -r fedora-22-x86_64 -r fedora-23-i386 -r fedora-23-x86_64

# Cleanup
rm -r "rpmbuild/SRPMS/paper-icon-theme-$PkgVersion.src.rpm"
rm -r "rpmbuild/SOURCES/paper-icon-theme-$GitSha.tar.gz"

# Update
git add rpmbuild/SPECS/paper-icon-theme.spec
git commit -m "Update spec file"
git push

