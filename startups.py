#!/usr/bin/env python
import os
import sys

if len(sys.argv) <= 1 or (len(sys.argv) - 1) % 2 != 0:
	print("Hi.")
	exit()

# Folders
startupPlistFolders = [
	"/Library/StartupItems",  # not use anymore
	"/System/Library/StartupItems",  # not use anymore
	"/Library/LaunchDaemons",  # load when Mac starts up, run as root.
	"/System/Library/LaunchDaemons",  # load when Mac starts up, run as root.
	"/Library/LaunchAgents",  # load when any user logs in, run as that user.
	"/System/Library/LaunchAgents",  # load when any user logs in, run as that user.
	"~/Library/LaunchAgents"  # load when particular user logs in, run as that user.
]

advancedPlistFolders = [
	"/System/Library/LaunchDaemons",  # macOS dependency
	"/System/Library/LaunchAgents"  # macOS dependency
]

kernelModulesFolders = [
	"/System/Library/Extensions"
]

# Parse options
args = sys.argv
options = {}

for index in range(1, len(args)):
	if args[index][:1] == "-":
		options[args[index]] = args[index + 1]

# List
doList = "--list" in options
if doList:
	doListArgs = options["--list"].split(",")

	listFolders = []
	if "user" in doListArgs:
		listFolders += startupPlistFolders
	if "advance" in doListArgs:
		listFolders += advancedPlistFolders
	if "kext" in doListArgs:
		listFolders += kernelModulesFolders
	noapple = "noapple" in doListArgs

	for folder in listFolders:
		f = folder if folder[:1] != "~" else os.path.expanduser("~") + folder[1:]
		r = os.listdir(f)
		print(
			folder,
			"=>\n\t",
			"\n\t".join(r) if not noapple else "\n\t".join([name for name in r if "com.apple" not in name])
		)
