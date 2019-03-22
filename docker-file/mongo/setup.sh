#!/bin/bash

mongo <<EOF
use admin;
db.auth('root', '123456');
show dbs;
db.createUser({user:'test',pwd:'test',roles:[{role:'readWrite',db:'test'}]});
use test;
db.createCollection("user");
EOF