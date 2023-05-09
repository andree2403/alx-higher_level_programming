#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sIX OPTIONS "$1" | grep Allow: | cut -b 8-100
