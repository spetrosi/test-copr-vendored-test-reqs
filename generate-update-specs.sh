#!/bin/bash
# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Red Hat, Inc.
# SPDX-License-Identifier: MITset -euo pipefail

# Run this file at the root of the repository then manually commit changes
# You need ansible-galaxy cli available
export COLLECTION_NAMESPACE COLLECTION_NAME COLLECTION_VERSION MODULE_TEMPLATE

generate_spec() {
    local COLLECTION_NAME COLLECTION_NAMESPACE COLLECTION_VERSION MODULE_TEMPLATE SPEC PACKAGE_NAME
    COLLECTION_NAME=$1
    COLLECTION_NAMESPACE=$2
    COLLECTION_VERSION=$3
    MODULE_TEMPLATE=$4
    SPEC=generated-spec.spec
    PACKAGE_NAME=lsr-ansible-collection-"${COLLECTION_NAMESPACE}"-"${COLLECTION_NAME}"

    cp lsr-ansible-collection-template.spec "${SPEC}"

    sed -i -e "s|COLLECTION_NAMESPACE|$COLLECTION_NAMESPACE|g" \
    -e "s|COLLECTION_NAME|$COLLECTION_NAME|g" \
    -e "s|COLLECTION_VERSION|$COLLECTION_VERSION|g" \
    -e "s|MODULE_TEMPLATE|$MODULE_TEMPLATE|g" "${SPEC}"

    cp "${SPEC}" "${PACKAGE_NAME}/${PACKAGE_NAME}.spec"

    rm "${SPEC}"
}

update_ansible_coll_vers() {
    local coll coll_dash coll_ver lsr_name
    coll=$1
    coll_dash="${coll//./-}"
    lsr_name="lsr-ansible-collection-${coll_dash}"
    ansible-galaxy collection download -p . "${coll}"
    coll_ver=$(ls ${coll_dash}-*.tar.gz | grep -oP "${coll_dash}-\K.*(?=.tar.gz)")
    sed -i "s/COLLECTION_VERSION=.*/COLLECTION_VERSION=$coll_ver/g" "${coll_dash}-vars.sh"
    sed -i "s/Version:.*/Version:        $coll_ver/g" "${lsr_name}/${lsr_name}.spec"
    rm -f ${coll_dash}-*.tar.gz requirements.yml
}

update_pywinrm_ver() {
    local ver
    ver=$(python3 -m pip index versions pywinrm | grep -oP 'LATEST:\s*\K.*')
    sed -i "s|^\%global srcver.*|%global srcver $ver|g" lsr-python3-pywinrm-src/lsr-python3-pywinrm-src.spec
}

update_pywinrm_ver

for coll in ansible.posix ansible.windows microsoft.ad; do
    update_ansible_coll_vers "$coll"
done

for vars_file in ansible-posix-vars.sh ansible-windows-vars.sh microsoft-ad-vars.sh; do
    source ./"${vars_file}"
    generate_spec "$COLLECTION_NAME" "$COLLECTION_NAMESPACE" "$COLLECTION_VERSION" "$MODULE_TEMPLATE"
done
