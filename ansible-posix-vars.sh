#! /bin/sh -x
COLLECTION_NAMESPACE=ansible
COLLECTION_NAME=posix
COLLECTION_VERSION=1.5.4
MODULE_TEMPLATE="# Keep only required modules\\
mkdir -p plugins-tmp/callback\\
mkdir -p plugins-tmp/modules\\
mkdir -p plugins-tmp/module_utils\\
cp plugins/callback/debug.py         plugins-tmp/callback/\\
cp plugins/callback/profile_tasks.py plugins-tmp/callback/\\
cp plugins/modules/mount.py          plugins-tmp/modules\\
cp plugins/module_utils/__init__.py  plugins-tmp/module_utils\\
cp plugins/module_utils/mount.py     plugins-tmp/module_utils\\
rm -rf plugins \\
mv plugins-tmp plugins"
