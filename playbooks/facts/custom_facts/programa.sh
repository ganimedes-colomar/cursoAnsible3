#!/bin/bash
export nginx_corrindo=true 
# Aqui hacemos una llamada a ver si nginx está orriendo o no

cat <<EOF
{
    "nginx_corrindo": ${nginx_corrindo}
}
EOF