[app]
title = Word of the Day
package.name = wordoftheday
package.domain = org.olexandr.word
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,googletrans==4.0.0rc1,cython
icon.filename = assets/icon.png
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1
use_venv = false
