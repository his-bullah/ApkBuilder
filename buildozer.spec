[app]

title = MyForegroundServiceApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,pyjnius,requests

orientation = portrait

fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk_api = 21

android.permissions = FOREGROUND_SERVICE,WAKE_LOCK,INTERNET

services = myservice:service/main.py

android.archs = arm64-v8a 

log_level = 2

buildozer.log_level = 2

android.allow_backup = True
android.accept_sdk_license = True