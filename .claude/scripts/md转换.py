#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md转换.py  —  将 .源文档/原始/ 中的任意文件转为 Markdown，
             按扩展名自动分流到 .源文档/{文章|文字稿|截图|数据}/。

用法：
    python .claude/scripts/md转换.py <文件路径-或-URL> [--force]
    python .claude/scripts/md转换.py --all               # 批量处理 原始/ 下所有文件
    python .claude/scripts/md转换.py <url-或-文件> --print  # 仅打印目标路径不转换

要求：markitdown >= 0.1.5  (pip install 'markitdown[all]')
"""
from __future__ import annotations
import argparse
import sys
import os
import shutil
import subprocess
from pathlib import Path

# 强制 stdout 用 UTF-8，避免 Windows GBK 乱码
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ------ 扩展名 → 子文件夹 路由表 ------
EXT_ROUTES = {
    ".pdf":   "文章", ".docx":  "文章", ".doc":   "文章",
    ".odt":   "文章", ".rtf":   "文章", ".epub":  "文章",
    ".html":  "文章", ".htm":   "文章", ".msg":   "文章",
    ".pptx":  "文章", ".ppt":   "文章", ".md":    "文章",
    ".txt":   "文章", ".zip":   "文章",
    ".mp3":   "文字稿", ".wav":   "文字稿", ".m4a":   "文字稿", ".flac":  "文字稿",
    ".jpg":   "截图", ".jpeg":  "截图", ".png":   "截图",
    ".gif":   "截图", ".webp":  "截图", ".bmp":   "截图", ".heic":  "截图",
    ".xlsx":  "数据", ".xls":   "数据", ".csv":   "数据",
    ".tsv":   "数据", ".json":  "数据", ".xml":   "数据",
}

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_ROOT = VAULT_ROOT / ".源文档"
RAW_DIR = SRC_ROOT / "原始"


def route_for(path_or_url: str) -> str:
    low = path_or_url.lower()
    if low.startswith(("http://", "https://")):
        if "youtube.com" in low or "youtu.be" in low:
            return "文字稿"
        return "文章"
    ext = Path(low).suffix
    return EXT_ROUTES.get(ext, "文章")


def target_path(src: str) -> Path:
    sub = route_for(src)
    if src.lower().startswith(("http://", "https://")):
        stem = src.rstrip("/").rsplit("/", 1)[-1] or "web"
        stem = stem.split("?")[0].split("#")[0] or "web"
        if "youtu" in src.lower():
            stem = "youtube-" + (Path(stem).stem or "video")
        stem = Path(stem).stem or "web"
    else:
        stem = Path(src).stem
    return SRC_ROOT / sub / f"{stem}.md"


def find_markitdown_python() -> str | None:
    """返回 Python 解释器路径，优先 3.12（依赖最全）。"""
    candidates = [
        r"C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe",
        r"C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe",
        shutil.which("python"),
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    return None


def run_markitdown(src: str, dst: Path) -> int:
    dst.parent.mkdir(parents=True, exist_ok=True)
    py = find_markitdown_python()
    if not py:
        print("ERROR: 找不到 Python。", file=sys.stderr)
        return 127
    # 用 python -m markitdown 调用，避免 .exe 入口的编码问题
    # 输出交给 markitdown 直接写文件（UTF-8）
    try:
        result = subprocess.run(
            [py, "-m", "markitdown", src, "-o", str(dst)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except Exception as e:
        print(f"ERROR: 调用失败：{e}", file=sys.stderr)
        return 1
    if result.returncode != 0:
        # 忽略 ffmpeg 警告
        err = "\n".join(l for l in (result.stderr or "").splitlines() if "ffmpeg" not in l.lower())
        if err.strip():
            print(err, file=sys.stderr)
    return result.returncode


def process_one(src: str, force: bool, only_print: bool) -> bool:
    dst = target_path(src)
    try:
        rel = dst.relative_to(VAULT_ROOT)
    except ValueError:
        rel = dst
    if only_print:
        print(f"[plan] {src}  ->  {rel}")
        return True
    if dst.exists() and not force:
        print(f"[skip] 已存在（加 --force 覆盖）: {rel}")
        return True
    print(f"[convert] {src}  ->  {rel}")
    code = run_markitdown(src, dst)
    if code != 0:
        print(f"[fail] 转换失败（退出码 {code}）: {src}", file=sys.stderr)
        return False
    size = dst.stat().st_size if dst.exists() else 0
    print(f"[ok] 完成: {rel}  ({size:,} bytes)")
    return True


def main():
    ap = argparse.ArgumentParser(description="将原始文件/URL 转换为 Obsidian vault 中的 markdown")
    ap.add_argument("target", nargs="?", help="文件路径或 URL")
    ap.add_argument("--all", action="store_true", help="批量处理 .源文档/原始/ 下全部文件")
    ap.add_argument("--force", action="store_true", help="目标已存在时覆盖")
    ap.add_argument("--print", dest="only_print", action="store_true", help="仅打印目标路径")
    args = ap.parse_args()

    os.chdir(VAULT_ROOT)

    if args.all:
        if not RAW_DIR.exists():
            print(f"ERROR: {RAW_DIR} 不存在", file=sys.stderr)
            return 1
        files = [p for p in RAW_DIR.rglob("*") if p.is_file()]
        if not files:
            print(f"[info] {RAW_DIR} 为空")
            return 0
        ok = 0
        for p in files:
            if process_one(str(p), args.force, args.only_print):
                ok += 1
        print(f"\n完成 {ok}/{len(files)}")
        return 0 if ok == len(files) else 2

    if not args.target:
        ap.print_help()
        return 2

    return 0 if process_one(args.target, args.force, args.only_print) else 1


if __name__ == "__main__":
    sys.exit(main() or 0)
