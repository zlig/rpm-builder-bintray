# rpm-builder-bintray
Builder tool to create Red Hat / CentOS .rpm packages (using Travis) and upload to Bintray


# Instructions


Add repository by creating the gile /etc/yum.repos.d/zlig.repo such as:

```
[zlig]
name=zlig
baseurl=https://dl.bintray.com/zlig/rpm
gpgcheck=0
repo_gpgcheck=0
enabled=1
```

Install the package with:
```
sudo yum install rpm-builder-bintray
```
