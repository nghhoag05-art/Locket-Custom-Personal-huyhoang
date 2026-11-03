#!/usr/bin/env python3
"""Sinh file module cho repository GitHub riêng. KHÔNG thay đổi nội dung 3 script."""
from pathlib import Path
import argparse
import re

parser = argparse.ArgumentParser(description="Tạo URL script-path trỏ về GitHub của bạn")
parser.add_argument("--user", required=True, help="GitHub username của bạn")
parser.add_argument("--repo", default="Locket-Custom-Personal", help="Tên repo GitHub")
parser.add_argument("--branch", default="main", help="Nhánh code")
parser.add_argument("--name", default="Locket Custom - Personal", help="Tên module")
args = parser.parse_args()
for value in (args.user, args.repo, args.branch):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", value):
        parser.error("Tên user/repo/branch chỉ được gồm chữ, số, _, -, .")
root = Path(__file__).resolve().parent.parent
base_url = f"https://raw.githubusercontent.com/{args.user}/{args.repo}/{args.branch}"
tpl = (root / "module" / "locket-custom.template.conf").read_text(encoding="utf-8")
module = tpl.replace("{{BASE_URL}}", base_url).replace("{{MODULE_NAME}}", args.name.replace("\n", " "))
out = root / "module" / "locket-custom.conf"
out.write_text(module, encoding="utf-8")
print(f"Đã tạo: {out}")
print(f"Link Raw sau khi upload: {base_url}/module/locket-custom.conf")
