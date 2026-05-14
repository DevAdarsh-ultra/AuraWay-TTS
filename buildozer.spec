[app]
title = AuraWay TTS
package.name = aurawaytts
package.domain = org.auraway
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Critical requirements for KivyMD 1.2.0 and Plyer
requirements = python3, kivy==2.3.0, kivymd==1.2.0, plyer, sdl2_ttf==2.0.15

orientation = portrait
fullscreen = 0

# Android specific (Fixed versions to bypass license errors)
android.archs = arm64-v8a, armeabi-v7a
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Permissions for TTS and Audio
android.permissions = INTERNET, WAKE_LOCK

[buildozer]
log_level = 2
warn_on_root = 1
