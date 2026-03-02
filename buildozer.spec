[app]
title = Shadow
package.name = shadowbridge
package.domain = com.ShadowBridge
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
services = MyService:service/main.py:foreground
android.permissions = FOREGROUND_SERVICE, POST_NOTIFICATIONS
android.api = 34
android.minapi = 21
android.ndk = 25.2.9519653
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2