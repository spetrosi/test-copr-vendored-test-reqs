#! /bin/sh -x
COLLECTION_NAMESPACE=ansible
COLLECTION_NAME=posix
COLLECTION_VERSION=1.5.2
MODULE_TEMPLATE="# Keep only required modules\\
mkdir -p plugins-tmp/modules\\
cp plugins/modules/group.py plugins-tmp/modules\\
cp plugins/modules/group.ps1 plugins-tmp/modules\\
cp plugins/modules/user.py plugins-tmp/modules\\
cp plugins/modules/user.ps1 plugins-tmp/modules\\
rm -rf plugins \\
mv plugins-tmp plugins"
