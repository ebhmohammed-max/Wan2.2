#!/usr/bin/env python3
"""Stream a file into a pre-authorised Google Drive resumable-upload session (runs on CI).

usage: ci_drive_upload.py FILE SESSION_URI_FILE  -> prints the Drive file JSON
The session URI is created from Arena with google_drive.initiate_resumable_upload; it only
allows uploading this one new file and expires after 7 days.
"""
import json, os, sys, time, urllib.error, urllib.request

CH = 32 * 256 * 1024  # 8 MiB, a multiple of 256 KiB as Drive requires


def main():
    path, sess_file = sys.argv[1], sys.argv[2]
    uri = open(sess_file).read().strip()
    total = os.path.getsize(path)
    off = 0
    with open(path, 'rb') as f:
        while off < total:
            f.seek(off)
            data = f.read(CH)
            end = off + len(data) - 1
            req = urllib.request.Request(uri, data=data, method='PUT', headers={
                'Content-Length': str(len(data)), 'Content-Range': f'bytes {off}-{end}/{total}'})
            for k in range(6):
                try:
                    with urllib.request.urlopen(req, timeout=300) as r:
                        print(json.dumps(json.loads(r.read() or b'{}')))  # 200/201 = done
                        return
                except urllib.error.HTTPError as e:
                    if e.code == 308:  # chunk accepted, continue from the reported Range
                        rng = e.headers.get('Range')
                        off = int(rng.split('-')[1]) + 1 if rng else 0
                        break
                    if e.code >= 500 and k < 5:
                        time.sleep(2 ** k); continue
                    raise SystemExit(f'upload failed: HTTP {e.code} {e.read()[:300]}')
                except Exception as e:  # noqa
                    if k < 5:
                        time.sleep(2 ** k); continue
                    raise
            print(f'{off}/{total}', file=sys.stderr)


if __name__ == '__main__':
    main()
