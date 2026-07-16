#!/usr/bin/env python3
# a local stand-in for vercel's cleanUrls: /parts serves parts.html, / serves index.html.
# run:  python3 serve.py   →  http://localhost:8000
import http.server, os, socketserver, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class CleanURLs(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = super().translate_path(path)
        bare = p.split('?')[0].split('#')[0]
        if not os.path.exists(bare) and os.path.exists(bare + '.html'):
            return bare + '.html'
        return p

with socketserver.TCPServer(('', PORT), CleanURLs) as httpd:
    print(f'grove, locally → http://localhost:{PORT}')
    httpd.serve_forever()
