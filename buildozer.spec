[app]
title = AuraWay TTS
package.name = aurawaytts
package.domain = org.auraway
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Keep requirements simple
requirements = python3==3.11.0, kivy==2.3.0, kivymd==1.2.0, plyer

orientation = portrait
fullscreen = 0

# CHANGE THIS LINE: Only one architecture to save memory/time
android.archs = arm64-v8a

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.permissions = INTERNET, WAKE_LOCK

[buildozer]
log_level = 2
warn_on_root = 1
