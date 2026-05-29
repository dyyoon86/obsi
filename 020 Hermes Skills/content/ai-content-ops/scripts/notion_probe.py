#!/usr/bin/env python3
"""
Probe a Notion content DB for the AI content ops workflow.

Reads:
  NOTION_TOKEN
  NOTION_DATABASE_ID

Usage:
  python scripts/notion_probe.py schema
  python scripts/notion_probe.py test-write

The test write uses existing status/select/multi_select options discovered from the DB to avoid invalid-option errors.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date

NOTION_VERSION = "2022-06-28"
TOKEN = os.environ.get("NOTION_TOKEN")
DB_ID = (os.environ.get("NOTION_DATABASE_ID") or "").strip()


def request(path, method="GET", payload=None):
    if not TOKEN or not DB_ID:
        raise SystemExit("Missing NOTION_TOKEN or NOTION_DATABASE_ID environment variable")
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.notion.com/v1/{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        raise SystemExit(f"HTTP {e.code}: {body}")


def get_db():
    return request(f"databases/{DB_ID}")


def title_of_db(db):
    return "".join(t.get("plain_text", "") for t in db.get("title", []))


def print_schema(db):
    print("Database:", title_of_db(db))
    print("ID:", db.get("id"))
    for name, prop in db.get("properties", {}).items():
        typ = prop.get("type")
        print(f"- {name}: {typ}")
        if typ == "status":
            print("  options:", ", ".join(o["name"] for o in prop["status"].get("options", [])))
            print("  groups:", ", ".join(g["name"] for g in prop["status"].get("groups", [])))
        elif typ == "select":
            print("  options:", ", ".join(o["name"] for o in prop["select"].get("options", [])))
        elif typ == "multi_select":
            print("  options:", ", ".join(o["name"] for o in prop["multi_select"].get("options", [])))


def first_option(prop):
    typ = prop.get("type")
    opts = prop.get(typ, {}).get("options", [])
    return opts[0]["name"] if opts else None


def rich(text):
    return {"rich_text": [{"text": {"content": str(text)[:1900]}}]} if text else {"rich_text": []}


def build_test_props(db):
    props = {}
    schema = db.get("properties", {})
    for name, prop in schema.items():
        typ = prop.get("type")
        if typ == "title":
            props[name] = {"title": [{"text": {"content": "[테스트] Notion schema probe"}}]}
        elif name == "날짜" and typ == "date":
            props[name] = {"date": {"start": date.today().isoformat()}}
        elif typ == "rich_text" and name in {"핵심 한 줄", "쇼츠 훅", "쇼츠 대본", "Threads 짧은 글", "성과 메모", "출처"}:
            props[name] = rich("Hermes Notion schema probe test")
        elif typ == "number" and name in {"쇼츠 적합도", "조회수", "좋아요", "댓글", "저장/공유"}:
            props[name] = {"number": 0 if name != "쇼츠 적합도" else 1}
        elif typ == "checkbox" and name == "팩트체크 필요":
            props[name] = {"checkbox": False}
        elif typ == "url" and name in {"원문 링크", "유튜브 URL"}:
            props[name] = {"url": None}
        elif typ == "date" and name in {"쇼츠 발행일", "Threads 발행일"}:
            props[name] = {"date": None}
        elif typ == "status":
            opt = first_option(prop)
            if opt:
                props[name] = {"status": {"name": opt}}
        elif typ == "select":
            opt = first_option(prop)
            if opt:
                props[name] = {"select": {"name": opt}}
        elif typ == "multi_select":
            opts = prop.get("multi_select", {}).get("options", [])[:3]
            if opts:
                props[name] = {"multi_select": [{"name": o["name"]} for o in opts]}
    return props


def test_write(db):
    payload = {"parent": {"database_id": DB_ID}, "properties": build_test_props(db)}
    page = request("pages", method="POST", payload=payload)
    print("Created:", page.get("url"))


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "schema"
    db = get_db()
    if mode == "schema":
        print_schema(db)
    elif mode == "test-write":
        test_write(db)
    else:
        raise SystemExit("Usage: notion_probe.py [schema|test-write]")


if __name__ == "__main__":
    main()
