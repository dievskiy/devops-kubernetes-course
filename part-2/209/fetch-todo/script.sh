#!/usr/bin/env bash

printf "Executing script...\n"

url=$(curl -Ls -o /dev/null -w %{url_effective} https://en.wikipedia.org/wiki/Special:Random)

curl http://todoapp-svc:4444/todos -X POST -H 'Content-Type: application/json' -d '{"item": "'${url}'"}'

if [ $? -eq 0 ];then
  printf "Script executed successfully\n"
else
  printf "Error adding a new todo\n"
fi