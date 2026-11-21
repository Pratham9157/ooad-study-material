#!/usr/bin/env python3
"""Command-line entry point.

  python tools/ooad.py build            render the site into dist/
  python tools/ooad.py check [FILTER]   compile & run every C++ example (needs g++)
  python tools/ooad.py serve [PORT]     build, then preview dist/ at http://localhost:PORT
"""
from __future__ import annotations

import argparse
import functools
import http.server
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ooadsite import builder, config, validator  # noqa: E402


def cmd_build(_args: argparse.Namespace) -> int:
    minutes = builder.build()
    print(f"Built {len(minutes)} lessons + index into {config.DIST_DIR} ({sum(minutes.values())} min of reading)")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    return 1 if validator.check(args.filter) else 0


def cmd_serve(args: argparse.Namespace) -> int:
    cmd_build(args)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(config.DIST_DIR))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Serving http://localhost:{args.port}  (Ctrl+C to stop)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="render the site into dist/").set_defaults(func=cmd_build)
    p_check = sub.add_parser("check", help="compile and run every C++ example")
    p_check.add_argument("filter", nargs="?", help="only lessons whose file name contains this text")
    p_check.set_defaults(func=cmd_check)
    p_serve = sub.add_parser("serve", help="build and preview locally")
    p_serve.add_argument("port", nargs="?", type=int, default=8000)
    p_serve.set_defaults(func=cmd_serve)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
