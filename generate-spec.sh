#! /bin/sh -x
export COLLECTION_NAMESPACE COLLECTION_NAME COLLECTION_VERSION MODULE_TEMPLATE

SPEC=generated-spec.spec
PACKAGE_NAME=lsr-ansible-collection-"${COLLECTION_NAMESPACE}"-"${COLLECTION_NAME}"

rm -rf results "${SPEC}"
cp lsr-ansible-collection-template.spec "${SPEC}"

sed -i "s|COLLECTION_NAMESPACE|$COLLECTION_NAMESPACE|g" "${SPEC}"
sed -i "s|COLLECTION_NAME|$COLLECTION_NAME|g" "${SPEC}"
sed -i "s|COLLECTION_VERSION|$COLLECTION_VERSION|g" "${SPEC}"
sed -i "s|MODULE_TEMPLATE|$MODULE_TEMPLATE|g" "${SPEC}"

mkdir results
cp "${SPEC}" results
cp "${SPEC}" "${PACKAGE_NAME}/${PACKAGE_NAME}.spec"

rm "${SPEC}"
