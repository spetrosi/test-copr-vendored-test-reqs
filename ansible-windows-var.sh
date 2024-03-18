#! /bin/sh -x
COLLECTION_NAMESPACE=ansible
COLLECTION_NAME=windows
COLLECTION_VERSION=2.2.0
MODULE_TEMPLATE="mkdir -p plugins-tmp/modules \\
cp plugins/modules/win_shell.py plugins/modules/win_shell.ps1 \ \\
    plugins/modules/win_command.py plugins/modules/win_command.ps1 \ \\
    plugins-tmp/modules/ \\
rm -rf plugins \\
mv plugins-tmp plugins"
