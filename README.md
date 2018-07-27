# rpm-builder-bintray

## Status

[![Download](ihttps://bintray.com/zlig/rpm/rpm-builder-bintray/images/download.svg)](https://bintray.com/zlig/rpm/rpm-builder-bintray#files)
[![Build Status](https://travis-ci.org/zlig/rpm-builder-bintray.svg?branch=master)](https://travis-ci.org/zlig/rpm-builder-bintray)
[![License](https://img.shields.io/badge/License-LGPL%202.1-blue.svg)](https://opensource.org/licenses/LGPL-2.1)

## Description

Builder tool to create Red Hat / CentOS .rpm packages (using Travis) and upload to Bintray


## Instructions

* Install the repository by creating the file /etc/yum.repos.d/zlig.repo:

```
echo "[zlig]
name=zlig
baseurl=https://dl.bintray.com/zlig/rpm
gpgcheck=0
repo_gpgcheck=0
enabled=1" | sudo tee -a /etc/yum.repos.d/zlig.repo
```

* Install the package
```
sudo yum install rpm-builder-bintray
```
