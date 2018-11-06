# This is a workaround in order to assume the current user.

FROM openapitools/openapi-generator-cli

ARG USERNAME
ARG UID
ARG GID

RUN adduser -D -H -u $UID -g $GID $USERNAME
USER $USERNAME
