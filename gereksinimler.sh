#!/bin/bash
pkg update -y && pkg upgrade -y
pkg install python2 -y
pkg install python3 -y
pkg install git -y
pkg install curl -y
pkg install openssh-server -y
pkg install wget -y
pkg install zip -y