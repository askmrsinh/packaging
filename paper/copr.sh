#!/bin/bash

# copr.sh -- shell script to do a Copr release of Paper (GTK + Icon) Theme
#
# Copyright (C) 2015 Ashesh Kumar Singh <user501254@gmail.com>
#
# This script may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.
#

set -e
set -o pipefail

if [[ ${PWD##*/} != "paper" ]]; then
  echo -e "\e[0;31mRun script from correct directory. Exiting.\e[0m"
  exit
fi

submit_build(){
  echo -e "\e[1;44m$1\e[0m"

  # Get version and revison of the most recent succesful built from Launchpad
  SuccessfullyBuilt=($(wget "https://launchpad.net/~snwh/+archive/ubuntu/pulp/+builds?build_text=$1&build_state=built" --no-cache -O - | grep -Po "build of $1 [0-9].[0-9]\+r[0-9]{3}" | head -n 1 | grep -Po "[0-9.]{3}"))
  echo -e "\e[0;34mLast succesful Launchpad built for $1 was ${SuccessfullyBuilt[0]}+r${SuccessfullyBuilt[1]}.\n\e[0m"

  # Get corresponding Git SHA for the built
  if [[ $1 == "paper-icon-theme" ]]; then
    GitSHA=$(wget "http://bazaar.launchpad.net/~snwh/paper-icon-theme/paper-icon-theme-git/files/${SuccessfullyBuilt[1]}" --no-cache -O - | grep "git-v1" | head -n 1 | grep -Po "[0-9a-z]{40}")
  fi
  if [[ $1 == "paper-gtk-theme" ]]; then
    GitSHA=$(wget "http://bazaar.launchpad.net/~snwh/paper-gtk-theme/master/files/${SuccessfullyBuilt[1]}" --no-cache -O - | grep "git-v1" | head -n 1 | grep -Po "[0-9a-z]{40}")
  fi
  
  VersionTag=${SuccessfullyBuilt[0]}.0
  Revision=0.${SuccessfullyBuilt[1]}
  Checkout=20160501git${GitSHA:0:7}
  pkg_version=$VersionTag-$Revision.$Checkout.$(uname -a | grep -Po "fc[0-9]{2}")

  if [[ $(wget "https://copr.fedoraproject.org/api/coprs/user501254/Paper/monitor/" --no-cache -O - | grep -Po "$1-$pkg_version" | head -n 1) == "" ]]; then
    cd $1/
    git fetch
    git merge $GitSHA
    cd ..
  else
    echo -e "\e[0;32m$1 $pkg_version is already available in Copr repo. Exiting.\e[0m"
    return
  fi

  # Get commit0 value within spec file for generating Changelog
  EndCommit=$(grep -Po "commit0 [0-9a-z]{40}" rpmbuild/SPECS/$1.spec | grep -Po "[0-9a-z]{40}")
  
  # Setup directories and files
  mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

  # Generate tarball, similar in structure to those that are downloaded from GitHub
  tar -czf "rpmbuild/SOURCES/$1-$GitSHA.tar.gz" $1/* --transform "s/$1/$1-$GitSHA/"

  # Set commit0 value within spec file
  sed -i "s/%global commit0 .*/%global commit0 $GitSHA/" rpmbuild/SPECS/$1.spec

  # Set version and release tag value within spec file
  sed -i "s/version:    .*/version:    $VersionTag/; s/release:    .*/release:    $Revision.$Checkout%{?dist}/" rpmbuild/SPECS/$1.spec

  # Generate Changelog since last release
  sed -n -i '/%changelog/q;p' rpmbuild/SPECS/$1.spec
  echo '%changelog' >> rpmbuild/SPECS/$1.spec
  ReleaseDate=$(date +"%a %b %d %Y")
  PackagerInfo="Ashesh Kumar Singh <user501254@gmail.com>"
  echo "* $ReleaseDate $PackagerInfo $VersionTag-$Revision" >> rpmbuild/SPECS/$1.spec
  cd $1/
  git log --pretty=format:"- %h: %s%x09(%an <%ae>)" $GitSHA...$EndCommit >> ../rpmbuild/SPECS/$1.spec
  cd ..

  # Build only Source RPM
  rpmbuild --define "_topdir $PWD/rpmbuild" -bs rpmbuild/SPECS/$1.spec

  # Submit Source RPM to Copr
  echo ""
  echo -e "\e[0;34mSubmitting Source RPM to Copr.\e[0m"
  copr-cli build --nowait Paper "rpmbuild/SRPMS/$1-$pkg_version.src.rpm" -r epel-7-x86_64 -r fedora-22-i386 -r fedora-22-x86_64 -r fedora-23-i386 -r fedora-23-x86_64 -r fedora-24-i386 -r fedora-24-x86_64

  # Cleanup
  rm -r "rpmbuild/SRPMS/$1-$pkg_version.src.rpm"
  rm -r "rpmbuild/SOURCES/$1-$GitSHA.tar.gz"

  # Update
  git add $1/ rpmbuild/SPECS/$1.spec
  git commit -m "$1-$pkg_version"
  git push
}

submit_build paper-gtk-theme
submit_build paper-icon-theme
