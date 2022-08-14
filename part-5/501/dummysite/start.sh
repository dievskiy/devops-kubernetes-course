#!/bin/bash

if [ -n "$website_url" ]; then
  printf "Copying $website_url website...\n"
  httrack $website_url -O /usr/share/nginx/html
  /usr/sbin/nginx -g 'daemon off;'
else
  printf "Website url was empty, exiting\n"
  exit 1
fi
