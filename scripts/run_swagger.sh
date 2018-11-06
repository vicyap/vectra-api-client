#!/bin/bash

set -u

OUTPUT_DIR=.

docker run -v $(pwd):/local openapi-generator-cli generate \
    --config /local/"${SWAG_DIR}"/config.json \
    --input-spec /local/"${SWAG_DIR}"/swagger.yml \
    --generator-name "${GENERATOR_NAME}" \
    --output /local/"${OUTPUT_DIR}"
