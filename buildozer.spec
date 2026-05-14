[app]
title = AuraWay TTS
package.name = aurawaytts
package.domain = org.auraway
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# IMPORTANT: Requirements for your specific app
requirements = python3, kivy==2.3.0, kivymd==1.2.0, plyer, sdl2_ttf==2.0.15

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Permissions for Text-to-Speech
android.permissions = INTERNET, WAKE_LOCK

[buildozer]
log_level = 2
warn_on_root = 15