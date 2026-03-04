[app]
title = Shadow
package.name = shadowbridge
package.domain = com.ShadowBridge
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests
services = MyService:service/main.py:foreground
android.permissions = FOREGROUND_SERVICE, POST_NOTIFICATIONS,INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
orientation = portrait
[buildozer]
log_level = 2