[app]
title = AuraWay TTS
# USE SIMPLE NAMES (No special characters or spaces)
package.name = aurawaytts
package.domain = org.auraway
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Lock these versions tightly
requirements = python3, kivy==2.3.0, kivymd==1.2.0, plyer, sdl2_ttf==2.0.15

orientation = portrait
fullscreen = 0

# TARGET ONLY ONE (Saves memory on the server)
android.archs = arm64-v8a

# Best settings for API 34
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Standard permissions
android.permissions = INTERNET, WAKE_LOCK

[buildozer]
log_level = 2
warn_on_root = 1
