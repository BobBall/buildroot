#!/bin/bash
set -eu

echo "Configuring RPM-based build"

. scripts/rpm/functions

get_distro
check_install_epel $DISTRO $MAJ_REL

DEPS="mock rpm-build createrepo python-argparse"
rpm -q $DEPS >/dev/null 2>&1 || sudo yum install -y $DEPS

echo -n "Writing mock configuration..."
mkdir -p mock
rm -f mock/mock_repos

# Replace the repositories
cat /etc/yum.repos.d/* >> mock/mock_repos
if [ "$DISTRO" == "CentOS" -a "$MAJ_REL" == "6" ]; then
cat scripts/rpm/centos-xen-4-4.repo >> mock/mock_repos
fi
sed -i -e "s/\$releasever/$MAJ_REL/g" \
       -e "s/\$basearch/$ARCH/g" mock/mock_repos

sed -e '/#REPOS/ r mock/mock_repos' -e "s|@PWD@|$PWD|g" scripts/rpm/mock-default.cfg.in > mock/default.cfg

ln -fs /etc/mock/site-defaults.cfg mock/
ln -fs /etc/mock/logging.ini mock/
echo " done"

echo -n "Initializing repository..."
mkdir -p RPMS SRPMS
createrepo --quiet RPMS
createrepo --quiet SRPMS
echo " done"

