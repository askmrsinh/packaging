#!/bin/bash

# copr.sh -- shell script to do a Copr release of Arc Theme
#
# Copyright (C) 2015 Ashesh Kumar Singh <user501254@gmail.com>
#
# This script may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.
#

set -e
set -o pipefail

if [[ ${PWD##*/} != "arc" ]]; then
  echo -e "\e[0;31mRun script from correct directory. Exiting.\e[0m"
  exit
fi

submit_build(){
  echo -e "\e[1;44m$1\e[0m"

  # Get version and revison of the most recent succesful built from OBS
  if [[ $1 == "arc-theme" ]]; then  
    SuccessfullyBuilt=$(wget "http://software.opensuse.org/download.html?project=home%3AHorst3180&package=arc-theme" --no-cache -O - | grep -Po "arc-theme-[0-9]{10}.[0-9a-z]{7}-[0-9.]{4}.noarch.rpm" | head -n 1 | grep -Po "[0-9]{10}.[0-9a-z]{7}-[0-9.]{4}")
  echo -e "\e[0;34mLast succesful OBS built for $1 was $SuccessfullyBuilt.\n\e[0m"
  fi
  if [[ $1 == "arc-theme-solid" ]]; then
    SuccessfullyBuilt=$(wget "http://software.opensuse.org/download.html?project=home%3AHorst3180&package=arc-theme-solid" --no-cache -O - | grep -Po "arc-theme-solid-[0-9]{10}.[0-9a-z]{7}-[0-9.]{4}.noarch.rpm" | head -n 1 | grep -Po "[0-9]{10}.[0-9a-z]{7}-[0-9.]{4}")
  echo -e "\e[0;34mLast succesful OBS built for $1 was $SuccessfullyBuilt.\n\e[0m"
  fi
  
  VersionTag=${SuccessfullyBuilt%-*}
  ReleaseTag=${SuccessfullyBuilt#*-}
  pkg_version=$VersionTag-$ReleaseTag.$(uname -a | grep -Po "fc[0-9]{2}")

  if [[ $(wget "https://copr.fedoraproject.org/api/coprs/user501254/Arc/monitor/" --no-cache -O - | grep -Po "$1-$VersionTag-$ReleaseTag" | head -n 1) == "" ]]; then
    cd arc-theme/
    # Get corresponding Git SHA for the built
    git fetch
    GitSHA=$(git log --pretty=format:"%H" ${SuccessfullyBuilt:11:7} -1)
    git merge $GitSHA
    cd ..
  else
    echo -e "\e[0;32m$1 $VersionTag-$ReleaseTag is already available in Copr repo. Exiting.\e[0m"
    return
  fi

  # Get commit0 value within spec file for generating Changelog
  EndCommit=$(grep -Po "commit0 [0-9a-z]{40}" rpmbuild/SPECS/$1.spec | grep -Po "[0-9a-z]{40}")
  
  # Setup directories and files
  mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

  # Generate tarball
  tar -czf "rpmbuild/SOURCES/$1-$VersionTag.tar.gz" arc-theme/* --transform "s/arc-theme/$1-$VersionTag/"

  # Set commit0 value within spec file
  sed -i "s/%global commit0 .*/%global commit0 $GitSHA/" rpmbuild/SPECS/$1.spec

  # Set version and release tag value within spec file
  sed -i "s/Version:    .*/Version:    $VersionTag/; s/Release:    .*/Release:    $ReleaseTag%{?dist}/" rpmbuild/SPECS/$1.spec

  # Generate Changelog since last release
  sed -n -i '/%changelog/q;p' rpmbuild/SPECS/$1.spec
  echo '%changelog' >> rpmbuild/SPECS/$1.spec
  ReleaseDate=$(date +"%a %b %d %Y")
  PackagerInfo="Ashesh Kumar Singh <user501254@gmail.com>"
  echo "* $ReleaseDate $PackagerInfo $VersionTag-$ReleaseTag" >> rpmbuild/SPECS/$1.spec
  cd arc-theme/
  git log --pretty=format:"- %h: %s%x09(%an <%ae>)" $GitSHA...$EndCommit >> ../rpmbuild/SPECS/$1.spec
  cd ..

  # Build only Source RPM
  rpmbuild --define "_topdir $PWD/rpmbuild" -bs rpmbuild/SPECS/$1.spec

  # Submit Source RPM to Copr
  echo ""
  echo -e "\e[0;34mSubmitting Source RPM to Copr.\e[0m"
  copr-cli build --nowait Arc "rpmbuild/SRPMS/$1-$pkg_version.src.rpm"

  # Cleanup
  rm -r "rpmbuild/SRPMS/$1-$pkg_version.src.rpm"
  rm -r "rpmbuild/SOURCES/$1-$VersionTag.tar.gz"

  # Update
  git add arc-theme/ rpmbuild/SPECS/$1.spec
  git commit -m "$1-$pkg_version"
  git push
}

submit_build arc-theme
submit_build arc-theme-solid
