#!/bin/sh
echo $VAULT_PASS > /vault_pass.txt
echo $(ansible-vault view --vault-password-file=/vault_pass.txt env-secrets)|xargs -n1 >> $GITHUB_ENV 
rm /vault_pass.txt