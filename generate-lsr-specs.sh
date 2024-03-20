#! /bin/sh -x

for vars_file in ansible-posix-vars.sh ansible-windows-vars.sh microsoft-ad-vars.sh; do
    source ./"${vars_file}"
    sh generate-spec.sh
done
