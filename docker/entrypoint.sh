#!/bin/bash
#
# entrypoint.sh copies the startup and management files into their proper
# locations, then fires off startup.sh

src=/opt/openoni/docker
cp $src/pip-install.sh /pip-install.sh
cp $src/load_batch.sh /load_batch.sh
cp $src/_startup_lib.sh /_startup_lib.sh

cp $src/test.sh /test.sh
cp $src/manage /usr/local/bin/manage
cp $src/django-admin /usr/local/bin/django-admin
cp $src/openoni.ini /etc/openoni.ini.orig

# Copy startup script based on whether this is a test-only container
if [[ $ONLY_RUN_TESTS == 1 ]]; then
  cp $src/test-startup.sh /startup.sh
else
  cp $src/startup.sh /startup.sh
fi

# Make all scripts executable
chmod u+x /*.sh
chmod u+x /usr/local/bin/*

/startup.sh
