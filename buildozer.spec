[app]
title = AuraWay TTS
package.name = aurawaytts
package.domain = org.auraway
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Keep it simple: let the action handle the specific sub-versions
requirements = python3, kivy, kivymd==1.2.0, plyer

orientation = portrait
fullscreen = 0

# TARGET ONLY ONE ARCHITECTURE (This is the secret fix for memory errors!)
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
