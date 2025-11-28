[app]
title = GTM Game
package.name = gtmgame
package.domain = org.example

# Source code folder
source.dir = .
source.include_exts = py,kv,mp3,png,jpg,ttf,wav

# Requirements
# Python 3.10 is REQUIRED for pyjnius + Kivy (fixes your build errors)
requirements = python3==3.9.18,kivy,pyjnius==2.0.4


# App settings
orientation = portrait
fullscreen = 1

# Android SDK/NDK/API
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30
android.archs = arm64-v8a, armeabi-v7a

# Version
version = 1.0

# Permissions (add if needed)
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 0
