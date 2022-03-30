#!/usr/bin/env bash

# Generate `index.html` which lists links for API endpoints

BASE_URL='http://shuuji3.xyz/tepco-forecast-api/api/'

# Print the header
cat <<EOF
<!DOCTYPE html>
<html>
  <head><title>tepco-forecast-api</title></head>
  <body>
    <h1>tepco-forecast-api</h1>
    <ul>
EOF

# Print links
cd public/api/ || exit
for f in *.json; do
		url="${BASE_URL}${f}"
		echo "      <li><a href=\"${url}\">${url}</a></li>"
done

# Print the footer
cat <<EOF
    </ul>
  </body>
</html>
EOF